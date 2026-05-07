#!/usr/bin/env python3
"""Prepare a small labeled Imagenette subset for the public mosaic demo.

Uses the validation split of fast.ai's Imagenette 160px archive, an ImageNet-derived
public subset. The selection is deterministic and label-first: one target label and a
balanced tile pool from the other labels.
"""
from __future__ import annotations
import argparse
import csv
import json
import pathlib
import shutil
from PIL import Image, ImageOps

LABELS = {
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


def image_score(path: pathlib.Path) -> tuple[int, int, str]:
    """Prefer valid, relatively detailed landscape-ish images; stable tie-break by name."""
    try:
        img = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        w, h = img.size
        small = img.resize((24, 24))
        pixels = list(small.getdata())
        mean = tuple(sum(px[i] for px in pixels) / len(pixels) for i in range(3))
        variance = int(sum(sum((px[i] - mean[i]) ** 2 for i in range(3)) for px in pixels) / len(pixels))
        area = w * h
        return (variance, area, path.name)
    except Exception:
        return (-1, -1, path.name)


def copy_jpeg(src: pathlib.Path, dst: pathlib.Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    img.save(dst, quality=92)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset-root", default="public_data/imagenette2-160")
    ap.add_argument("--out", default="public_data/imagenette_mosaic")
    ap.add_argument("--target-wnid", default="n03028079", choices=sorted(LABELS))
    ap.add_argument("--tiles-per-label", type=int, default=12)
    args = ap.parse_args()

    root = pathlib.Path(args.dataset_root)
    val = root / "val"
    if not val.exists():
        raise SystemExit(f"Missing Imagenette validation split: {val}")

    out = pathlib.Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    target_dir = out / "target"
    tiles_dir = out / "tiles"
    assets_dir = pathlib.Path("../docs/item1/assets")
    if not assets_dir.exists():
        assets_dir = pathlib.Path("docs/item1/assets")

    manifest_rows = []
    selected = {}
    for wnid, label in LABELS.items():
        imgs = sorted((val / wnid).glob("*.JPEG")) + sorted((val / wnid).glob("*.jpg"))
        if not imgs:
            raise SystemExit(f"No images found for {wnid} {label}")
        ranked = sorted(imgs, key=image_score, reverse=True)
        selected[wnid] = ranked

    target_src = selected[args.target_wnid][0]
    target_name = f"{args.target_wnid}_{LABELS[args.target_wnid].replace(' ', '-')}_target.jpg"
    target_dst = target_dir / target_name
    copy_jpeg(target_src, target_dst)
    copy_jpeg(target_src, assets_dir / "imagenette-target-church.jpg")
    manifest_rows.append({"role": "target", "wnid": args.target_wnid, "label": LABELS[args.target_wnid], "source": str(target_src), "prepared": str(target_dst)})

    for wnid, label in LABELS.items():
        if wnid == args.target_wnid:
            continue
        for i, src in enumerate(selected[wnid][: args.tiles_per_label]):
            safe_label = label.lower().replace(" ", "-")
            dst = tiles_dir / f"{wnid}_{safe_label}_{i:03d}.jpg"
            copy_jpeg(src, dst)
            manifest_rows.append({"role": "tile", "wnid": wnid, "label": label, "source": str(src), "prepared": str(dst)})

    out.mkdir(parents=True, exist_ok=True)
    with (out / "selection_manifest.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["role", "wnid", "label", "source", "prepared"])
        writer.writeheader(); writer.writerows(manifest_rows)
    (out / "selection_summary.json").write_text(json.dumps({
        "dataset": "Imagenette 2 160px validation split (fast.ai), ImageNet-derived public subset",
        "target": {"wnid": args.target_wnid, "label": LABELS[args.target_wnid], "count": 1},
        "tile_pool": [{"wnid": wnid, "label": label, "count": args.tiles_per_label} for wnid, label in LABELS.items() if wnid != args.target_wnid],
        "selection_rule": "Target is the highest-detail validation image from the chosen target label; tile pool is a balanced deterministic set from every non-target Imagenette label.",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"target: {target_dst}")
    print(f"tiles: {len(manifest_rows)-1} in {tiles_dir}")
    print(f"manifest: {out/'selection_manifest.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
