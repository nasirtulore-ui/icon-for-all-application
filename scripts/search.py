"""Search the nasui icon collection.

Examples
  python scripts/search.py home
  python scripts/search.py user --style fill
  python scripts/search.py github --pack simple-icons
  python scripts/search.py settings --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACK_ORDER = [
    "tabler",
    "lucide",
    "phosphor",
    "heroicons",
    "bootstrap",
    "fluent",
    "material",
    "simple-icons",
    "hugeicons",
]


def safe_id(value: str) -> str:
    text = value.lower().replace("&", " and ").replace("_", " ")
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-")


def style_ok(variants: dict, wanted: str | None) -> bool:
    if not wanted:
        return True
    return any(key == wanted or key.startswith(wanted + "-") for key in variants)


def has_tag(tags: set[str], term: str) -> bool:
    return term in tags or f"{term}s" in tags


def score(icon: dict, terms: list[str]) -> int:
    icon_id = icon["id"]
    family = icon["family"]
    name = icon["name"].lower()
    tags = set(icon.get("tags") or [])
    best = 0
    for term in terms:
        parts = icon_id.split("-")
        tagged = has_tag(tags, term)
        if icon_id == term:
            best += 100
        elif family == term:
            best += 90
        elif tagged and "-" not in icon_id:
            best += 85
        elif term in parts or term in family.split("-"):
            best += 50
        elif term in name.split():
            best += 40
        elif tagged:
            best += 30
        elif any(term in tag.split("-") or f"{term}s" in tag.split("-") for tag in tags):
            best += 15
        else:
            return 0
    return best


def load(pack: str | None) -> list[dict]:
    icons = []
    with (ROOT / "catalog.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            icon = json.loads(line)
            if pack and icon["pack"] != pack:
                continue
            icons.append(icon)
    return icons


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Search nasui icons by name, family, or tag.")
    parser.add_argument("query", help="Words to search, such as home or user")
    parser.add_argument("--pack", choices=PACK_ORDER, help="Limit the search to one set")
    parser.add_argument("--style", help="Only icons that have this style, such as outline, fill, or duotone")
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--json", action="store_true", help="Print JSON for scripts and AI tools")
    args = parser.parse_args()
    terms = [safe_id(part) for part in args.query.split() if safe_id(part)]
    if not terms:
        raise SystemExit("Give a search word, such as home")
    wanted = safe_id(args.style) if args.style else None
    ranked = []
    for icon in load(args.pack):
        if not style_ok(icon["variants"], wanted):
            continue
        value = score(icon, terms)
        if value:
            ranked.append((value, PACK_ORDER.index(icon["pack"]), icon["id"], icon))
    ranked.sort(key=lambda item: (-item[0], len(item[2]), item[1], item[2]))
    matches = [item[3] for item in ranked[: args.limit]]
    if args.json:
        print(json.dumps(matches, indent=2, ensure_ascii=False))
        return
    if not matches:
        print("No icons matched.")
        return
    print(f"{len(matches)} match(es). Showing up to {args.limit}.\n")
    for icon in matches:
        styles = ", ".join(icon["variants"])
        print(f"{icon['pack']}  {icon['id']}  {icon['name']}  [{icon['category']}]  family {icon['family']}")
        print(f"  styles: {styles}")
        for style, path in icon["variants"].items():
            print(f"  {style}: {path}")
        print()


if __name__ == "__main__":
    main()
