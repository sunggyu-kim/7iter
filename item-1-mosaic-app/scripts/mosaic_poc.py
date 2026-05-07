#!/usr/bin/env python3
"""Low-distortion photo mosaic PoC for Mosaic Year.

Core principle: preserve each source photo as a real mini-photo. We only EXIF-rotate,
center-crop to the cell aspect ratio, and resize. No tinting, hue shifting, or opacity
overlay is applied. If color coverage is missing, the report calls out gaps so new
photos/assets can be generated instead of recoloring existing memories.
"""
from __future__ import annotations
import argparse, json, math, pathlib, random, re
from collections import Counter
from PIL import Image, ImageOps, ImageStat, ImageDraw

IMG_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
STANDARD_EXTS = {".jpg", ".jpeg", ".png"}

IMAGENETTE_LABELS = {
    "n01440764": "tench",
    "n02102040": "English springer",
    "n02979186": "cassette player",
    "n03000684": "chain saw",
    "n03028079": "church",
    "n03394916": "French horn",
    "n03417042": "garbage truck",
    "n03425413": "gas pump",
    "n03445777": "golf ball",
    "n03888257": "parachute",
}


def infer_dataset_label(path: pathlib.Path) -> dict[str, str] | None:
    """Infer an ImageNet/Imagenette class from a parent directory or copied filename.

    Supports original paths such as ``val/n03028079/ILSVRC...JPEG`` and prepared
    flat filenames such as ``n03028079_church_000.JPEG``.
    """
    candidates = [path.parent.name, path.name]
    for text in candidates:
        m = re.search(r"n\d{8}", text)
        if m:
            wnid = m.group(0)
            return {"wnid": wnid, "name": IMAGENETTE_LABELS.get(wnid, "unknown")}
    return None


def find_standard_image(tile_dir: pathlib.Path) -> pathlib.Path | None:
    """Find standard/STANDARD jpg/jpeg/png in the tile directory, case-insensitively."""
    matches = sorted(
        p for p in tile_dir.iterdir()
        if p.is_file() and p.stem.lower() == "standard" and p.suffix.lower() in STANDARD_EXTS
    )
    return matches[0] if matches else None


def mean_rgb(img: Image.Image) -> tuple[float, float, float]:
    small = img.convert("RGB").resize((1, 1), Image.Resampling.BOX)
    return tuple(ImageStat.Stat(small).mean)  # type: ignore[return-value]


def open_rgb(path: pathlib.Path) -> Image.Image:
    return ImageOps.exif_transpose(Image.open(path)).convert("RGB")


def crop_cover(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    tw, th = size
    w, h = img.size
    src_ratio, dst_ratio = w / h, tw / th
    if src_ratio > dst_ratio:
        nw = int(h * dst_ratio)
        left = (w - nw) // 2
        img = img.crop((left, 0, left + nw, h))
    else:
        nh = int(w / dst_ratio)
        top = (h - nh) // 2
        img = img.crop((0, top, w, top + nh))
    return img.resize(size, Image.Resampling.LANCZOS)


def dist(a, b):
    # Slightly weight luminance via RGB; intentionally simple/explainable for PoC.
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))


def label_rgb(rgb):
    r, g, b = rgb
    mx, mn = max(rgb), min(rgb)
    if mx < 55: return "near-black"
    if mn > 205: return "near-white"
    if mx - mn < 28: return "neutral-gray"
    if r == mx and g > 130: return "warm-yellow/orange"
    if r == mx: return "red/warm"
    if g == mx: return "green"
    return "blue/cool"


def choose_tile(target_rgb, tile_meta, usage, max_reuse):
    scored = []
    for meta in tile_meta:
        penalty = 18 * usage[meta["path"]]
        if max_reuse and usage[meta["path"]] >= max_reuse:
            penalty += 9999
        scored.append((dist(target_rgb, meta["mean_rgb"]) + penalty, meta))
    scored.sort(key=lambda x: x[0])
    return scored[0][1], scored[0][0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", default="", help="representative image; if omitted, finds standard/STANDARD .jpg/.jpeg/.png in --tiles")
    ap.add_argument("--tiles", default="sample", help="folder of mosaic tile photos")
    ap.add_argument("--out", default="mockup/generated/mosaic_demo.jpg")
    ap.add_argument("--report", default="mockup/generated/mosaic_report.json")
    ap.add_argument("--cols", type=int, default=42)
    ap.add_argument("--cell", type=int, default=28)
    ap.add_argument("--max-reuse", type=int, default=0, help="0 allows reuse with soft penalty")
    ap.add_argument("--allow-fallback-target", action="store_true", help="if standard.jpg is missing, use first tile as demo target")
    ap.add_argument("--dataset-name", default="", help="optional public dataset name to include in the JSON report")
    args = ap.parse_args()

    tile_dir = pathlib.Path(args.tiles)
    target = pathlib.Path(args.target) if args.target else (find_standard_image(tile_dir) or pathlib.Path("sample/STANDARD.jpg"))
    all_imgs = sorted(p for p in tile_dir.iterdir() if p.suffix.lower() in IMG_EXTS and p.is_file())
    fallback_note = None
    if not target.exists():
        if not args.allow_fallback_target or not all_imgs:
            raise SystemExit(f"Target missing: {target}. Put standard/STANDARD jpg/jpeg/png in {tile_dir} or pass --allow-fallback-target for demo.")
        target = all_imgs[0]
        fallback_note = f"standard/STANDARD jpg/jpeg/png was missing; demo target substituted with {target.name}"

    tile_paths = [p for p in all_imgs if p.resolve() != target.resolve()]
    if not tile_paths:
        raise SystemExit("No tile images available after excluding target")

    target_img = open_rgb(target)
    aspect = target_img.height / target_img.width
    rows = max(1, round(args.cols * aspect))
    cell = (args.cell, args.cell)
    out_size = (args.cols * args.cell, rows * args.cell)
    target_small = target_img.resize((args.cols, rows), Image.Resampling.BOX)

    tile_meta = []
    tile_cache = {}
    for p in tile_paths:
        img = open_rgb(p)
        avg_img = crop_cover(img, cell)
        tile_cache[str(p)] = avg_img
        tile_meta.append({"path": str(p), "name": p.name, "mean_rgb": mean_rgb(avg_img), "size": img.size, "label": infer_dataset_label(p)})

    out = Image.new("RGB", out_size, "white")
    usage = Counter()
    matches = []
    for y in range(rows):
        for x in range(args.cols):
            rgb = target_small.getpixel((x, y))
            meta, selection_score = choose_tile(rgb, tile_meta, usage, args.max_reuse)
            actual_distance = dist(rgb, meta["mean_rgb"])
            usage[meta["path"]] += 1
            out.paste(tile_cache[meta["path"]], (x * args.cell, y * args.cell))
            matches.append({"x": x, "y": y, "target_rgb": rgb, "tile": meta["name"], "distance": round(actual_distance, 2), "selection_score": round(selection_score, 2)})

    out_path = pathlib.Path(args.out); out_path.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_path, quality=92)

    # Thumbnail index / QA sheet: shows raw tile palette with no color mutation.
    sw = 160; sh = 120; pad = 12
    sheet_cols = min(8, len(tile_meta)); sheet_rows = math.ceil(len(tile_meta) / sheet_cols)
    sheet = Image.new("RGB", (sheet_cols * (sw + pad) + pad, sheet_rows * (sh + 34) + pad), "#f6f4ef")
    draw = ImageDraw.Draw(sheet)
    for i, meta in enumerate(tile_meta):
        p = pathlib.Path(meta["path"])
        thumb = crop_cover(open_rgb(p), (sw, sh))
        sx = pad + (i % sheet_cols) * (sw + pad); sy = pad + (i // sheet_cols) * (sh + 34)
        sheet.paste(thumb, (sx, sy)); draw.text((sx, sy + sh + 4), meta["name"][:22], fill=(45,45,45))
    sheet_path = out_path.with_name("tile_contact_sheet.jpg")
    sheet.save(sheet_path, quality=90)

    labels_target = Counter(label_rgb(m["target_rgb"]) for m in matches)
    labels_tiles = Counter(label_rgb(m["mean_rgb"]) for m in tile_meta)
    avg_distance = sum(m["distance"] for m in matches) / len(matches)
    hard_cells = [m for m in matches if m["distance"] > 95]
    report = {
        "dataset": args.dataset_name or None,
        "target": str(target),
        "target_label": infer_dataset_label(target),
        "fallback_note": fallback_note,
        "tile_count": len(tile_meta),
        "tile_label_counts": Counter((m.get("label") or {}).get("name", "unlabeled") for m in tile_meta),
        "tile_wnid_counts": Counter((m.get("label") or {}).get("wnid", "unlabeled") for m in tile_meta),
        "grid": {"cols": args.cols, "rows": rows, "cell_px": args.cell, "output_px": out_size},
        "method": "EXIF transpose + center crop + resize only; no hue/tint/opacity color transform",
        "avg_match_distance_rgb": round(avg_distance, 2),
        "hard_match_cell_ratio": round(len(hard_cells) / len(matches), 4),
        "target_color_mix": labels_target,
        "tile_color_mix": labels_tiles,
        "most_reused_tiles": [(pathlib.Path(k).name, v) for k, v in usage.most_common(10)],
        "recommendation": "If hard_match_cell_ratio is high or a target_color_mix bucket is missing in tile_color_mix, generate/acquire new photos in those color families rather than recoloring existing photos.",
    }
    report_path = pathlib.Path(args.report); report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out_path}")
    print(f"wrote {sheet_path}")
    print(f"wrote {report_path}")
    print(f"avg_distance={report['avg_match_distance_rgb']} hard_ratio={report['hard_match_cell_ratio']}")
    if fallback_note:
        print(f"NOTE: {fallback_note}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
