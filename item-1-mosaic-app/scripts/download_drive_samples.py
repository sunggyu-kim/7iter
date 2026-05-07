#!/usr/bin/env python3
"""Download public Google Drive image files and locate the representative STANDARD image.

Manifest format: file_id<TAB>filename<TAB>mime_type<TAB>size_bytes
This script intentionally avoids Google auth so it works for public/shared folders.

Round-2 upgrade:
- can refresh the manifest from a public Google Drive folder URL/ID by parsing the
  anonymous Drive folder page payload;
- matches STANDARD/standard with .jpg/.jpeg/.png case-insensitively;
- can download/copy the first matching representative image to sample/STANDARD.<ext>.
"""
from __future__ import annotations
import argparse, csv, html, json, pathlib, re, sys, time, urllib.request
from urllib.parse import unquote

BASE = "https://drive.google.com/uc?export=download&id={id}"
DEFAULT_FOLDER_URL = "https://drive.google.com/drive/folders/14IWC2gPyujpCyC8OOJCP7dtIGBW4dWoS?usp=sharing"
IMG_EXTS = {".jpg", ".jpeg", ".png"}
STANDARD_RE = re.compile(r"^standard\.(jpe?g|png)$", re.IGNORECASE)


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read().decode("utf-8", errors="replace")


def decode_drive_ivd(page: str) -> list:
    m = re.search(r"window\['_DRIVE_ivd'\]\s*=\s*'((?:\\.|[^'])*)'", page)
    if not m:
        raise ValueError("Could not find _DRIVE_ivd payload in Drive folder page")
    raw = m.group(1)
    # Drive embeds a JS string containing \x5b/\u003d escapes plus JS-only \/.
    # Decode only the escape families Drive uses so Python does not warn on \/.
    decoded = re.sub(r"\\x([0-9a-fA-F]{2})", lambda m: chr(int(m.group(1), 16)), raw)
    decoded = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), decoded)
    # JavaScript permits identity escapes such as \= in strings; JSON does not.
    decoded = re.sub(r'\\([^"\\/bfnrtu])', r'\1', decoded)
    decoded = decoded.replace(r"\/", "/")
    return json.loads(decoded)


def rows_from_ivd(ivd: list) -> list[list[str]]:
    rows: list[list[str]] = []
    seen: set[str] = set()

    def walk(x):
        if isinstance(x, list):
            if len(x) >= 14 and isinstance(x[0], str) and isinstance(x[2], str) and isinstance(x[3], str):
                fid, name, mime = x[0], x[2], x[3]
                size = x[13] if len(x) > 13 and isinstance(x[13], int) else ""
                if mime.startswith("image/") and pathlib.Path(name).suffix.lower() in IMG_EXTS and fid not in seen:
                    seen.add(fid)
                    rows.append([fid, name, mime, str(size)])
            for y in x:
                walk(y)
    walk(ivd)
    rows.sort(key=lambda r: r[1].lower())
    return rows


def refresh_manifest(folder_url: str, manifest: pathlib.Path, html_log: pathlib.Path | None = None, decoded_log: pathlib.Path | None = None) -> list[list[str]]:
    page = fetch_text(folder_url)
    if html_log:
        html_log.parent.mkdir(parents=True, exist_ok=True)
        html_log.write_text(page, encoding="utf-8")
    ivd = decode_drive_ivd(page)
    rows = rows_from_ivd(ivd)
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerows(rows)
    if decoded_log:
        decoded_log.parent.mkdir(parents=True, exist_ok=True)
        decoded_log.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    return rows


def load_manifest(path: pathlib.Path) -> list[list[str]]:
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="\t"):
            if len(row) >= 2:
                rows.append(row)
    return rows


def find_standard(rows: list[list[str]]) -> list[list[str]]:
    return [r for r in rows if len(r) >= 2 and STANDARD_RE.match(r[1])]


def download(fid: str, out: pathlib.Path, retries: int = 3, overwrite: bool = False) -> tuple[bool, str]:
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists() and out.stat().st_size > 0 and not overwrite:
        return True, "exists"
    url = BASE.format(id=fid)
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                ctype = r.headers.get("content-type", "")
                data = r.read()
            suffix = out.suffix.lower()
            valid_signature = data.startswith(b"\xff\xd8") or data.startswith(b"\x89PNG\r\n\x1a\n")
            if not valid_signature and "image" not in ctype:
                return False, f"unexpected response content-type={ctype!r} bytes={len(data)}"
            tmp = out.with_suffix(out.suffix + ".tmp")
            tmp.write_bytes(data)
            tmp.replace(out)
            return True, f"downloaded {len(data)} bytes"
        except Exception as e:  # network/API errors are reported in manifest output
            if attempt == retries:
                return False, f"{type(e).__name__}: {e}"
            time.sleep(1.5 * attempt)
    return False, "unreachable"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="sample/drive_manifest.tsv")
    ap.add_argument("--out", default="sample")
    ap.add_argument("--limit", type=int, default=0, help="0 means all")
    ap.add_argument("--drive-url", default=DEFAULT_FOLDER_URL, help="public Drive folder URL or folders/<id> URL")
    ap.add_argument("--refresh-manifest", action="store_true", help="fetch Drive folder page and rebuild manifest")
    ap.add_argument("--html-log", default="logs/drive_folder_page.html")
    ap.add_argument("--decoded-log", default="logs/drive_ivd_decoded.json")
    ap.add_argument("--find-standard", action="store_true", help="print STANDARD/standard jpg/jpeg/png matches")
    ap.add_argument("--download-standard", action="store_true", help="download matching representative image to sample/STANDARD.<ext>")
    ap.add_argument("--skip-download", action="store_true", help="only refresh/inspect manifest")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    manifest = pathlib.Path(args.manifest)
    if args.refresh_manifest:
        rows = refresh_manifest(args.drive_url, manifest, pathlib.Path(args.html_log), pathlib.Path(args.decoded_log))
        print(f"REFRESHED_MANIFEST\t{manifest}\t{len(rows)} rows")
    else:
        rows = load_manifest(manifest)

    standard_rows = find_standard(rows)
    if args.find_standard or args.refresh_manifest:
        if standard_rows:
            for fid, name, *rest in standard_rows:
                print(f"STANDARD_MATCH\t{name}\t{fid}\t{rest[0] if rest else ''}")
        else:
            candidates = [r[1] for r in rows if len(r) >= 2 and "standard" in r[1].lower()]
            print(f"STANDARD_MATCH\tNONE\tchecked={len(rows)}\tcandidates={candidates}")

    if args.download_standard:
        if not standard_rows:
            print("STANDARD_DOWNLOAD\tFalse\tno STANDARD.jpg/jpeg/png found in manifest")
            return 3
        fid, name, *_ = standard_rows[0]
        suffix = pathlib.Path(name).suffix.lower()
        success, msg = download(fid, pathlib.Path(args.out) / f"STANDARD{suffix}", overwrite=args.overwrite)
        print(f"STANDARD_DOWNLOAD\t{name}\t{success}\t{msg}")
        return 0 if success else 2

    if args.skip_download:
        return 0

    if args.limit:
        rows = rows[: args.limit]
    ok = 0
    for fid, name, *_ in rows:
        success, msg = download(fid, pathlib.Path(args.out) / name, overwrite=args.overwrite)
        print(f"{name}\t{success}\t{msg}")
        ok += int(success)
    print(f"SUMMARY\t{ok}/{len(rows)} downloaded")
    return 0 if ok == len(rows) else 2


if __name__ == "__main__":
    raise SystemExit(main())
