#!/usr/bin/env python3
"""Download public Google Drive image files from a manifest TSV.

Manifest format: file_id<TAB>filename<TAB>mime_type<TAB>size_bytes
This script intentionally avoids Google auth so it works for public/shared folders.
"""
from __future__ import annotations
import argparse, csv, pathlib, sys, time, urllib.request, urllib.error

BASE = "https://drive.google.com/uc?export=download&id={id}"

def download(fid: str, out: pathlib.Path, retries: int = 3) -> tuple[bool, str]:
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists() and out.stat().st_size > 0:
        return True, "exists"
    url = BASE.format(id=fid)
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                ctype = r.headers.get("content-type", "")
                data = r.read()
            if not data.startswith(b"\xff\xd8") and "image" not in ctype:
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
    args = ap.parse_args()
    rows = []
    with open(args.manifest, newline="", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="\t"):
            if len(row) >= 2:
                rows.append(row)
    if args.limit:
        rows = rows[: args.limit]
    ok = 0
    for fid, name, *_ in rows:
        success, msg = download(fid, pathlib.Path(args.out) / name)
        print(f"{name}\t{success}\t{msg}")
        ok += int(success)
    print(f"SUMMARY\t{ok}/{len(rows)} downloaded")
    return 0 if ok == len(rows) else 2

if __name__ == "__main__":
    raise SystemExit(main())
