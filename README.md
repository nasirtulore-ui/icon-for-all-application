# nasui

nasui is an icon collection made by nasui. The brand is nasmedia.

The drawings come from other open-source sets. nasui keeps each set in its own folder with the original license, the SVG files, and metadata so a person or a script can search by name, category, tag, and style.

Copy a pack into a project, or publish this folder on GitHub and link to the files from there.

## Pack layout

```
tabler/
├── svg/
│   ├── home.svg
│   └── home-fill.svg
├── metadata.json
└── LICENSE
```

`svg` holds the files. `metadata.json` describes them. `LICENSE` is the upstream license for that set. Keep that file with the icons if you copy the pack out.

## Metadata

The keys in `metadata.json` are icon ids. `_pack` identifies the set.

`name` is the label. `category` is the group. `tags` are the search words. `style` and `file` point at the default SVG. Outline is the default when the set has one.

`variants` lists every style of that same icon. Fill, duotone, and the other weights are not separate icons.

`family` ties drawings that only differ by a small variant. `home-01` and `home-02` share the family `home`. A circle form and a square form share a family too.

Paths inside a pack are relative to that pack. `catalog.jsonl` at the repo root uses paths from the repo root, one icon per line. `families.json` lists every pack that has the same family name.

```json
{
  "home": {
    "name": "Home",
    "category": "buildings",
    "tags": ["home", "house"],
    "family": "home",
    "style": "outline",
    "file": "svg/home.svg",
    "variants": {
      "outline": "svg/home.svg",
      "fill": "svg/home-fill.svg"
    }
  }
}
```

## Styles

You will see `outline`, `fill`, and `duotone`. Phosphor also has `thin`, `light`, and `bold`. Material also has `round` and `sharp`. Heroicons also has `fill-20` and `fill-16`. Simple Icons uses `brand`. Fluent color icons use `color`.

A search returns every matching pack and every style that pack actually ships.

## Find an icon

From this folder:

```
python scripts/search.py home
python scripts/search.py user --style fill
python scripts/search.py github --pack simple-icons
python scripts/search.py settings --json
```

A match can come from the id, the family, the label, or a tag. Lucide calls its house icon `house` and tags it `home`, so a search for home still returns it.

`--json` prints the matches for scripts and AI tools.

## Use a file

```
tabler/svg/home.svg
```

After you push this repo, the raw URL looks like this.

```
https://raw.githubusercontent.com/<you>/nasui/main/tabler/svg/home.svg
```

Most stroke icons already use `currentColor`, so CSS color changes them. Hugeicons in this repo were changed from the fixed stroke `#141B34` to `currentColor`. Every other SVG is copied from upstream unchanged.

## What nasui adds

nasui does not redraw the icons. The folder layout, the metadata, and the search index are the nasui work. Copyright in each SVG stays with the original project. See the `LICENSE` file in that pack.

`README.md`, `nasui.json`, `catalog.jsonl`, `families.json`, and `scripts/search.py` are MIT, copyright nasmedia. See the root `LICENSE`.

## Packs

25001 icons.

| Set | Folder | License | Icons | Source |
| --- | --- | --- | --- | --- |
| Tabler Icons | `tabler` | MIT | 5166 | https://github.com/tabler/tabler-icons |
| Lucide | `lucide` | ISC | 1857 | https://github.com/lucide-icons/lucide |
| Phosphor Icons | `phosphor` | MIT | 1512 | https://github.com/phosphor-icons/core |
| Heroicons | `heroicons` | MIT | 324 | https://github.com/tailwindlabs/heroicons |
| Bootstrap Icons | `bootstrap` | MIT | 1409 | https://github.com/twbs/icons |
| Fluent System Icons | `fluent` | MIT | 2919 | https://github.com/microsoft/fluentui-system-icons |
| Material Design Icons | `material` | Apache-2.0 | 2209 | https://github.com/google/material-design-icons |
| Simple Icons | `simple-icons` | CC0-1.0 | 3464 | https://github.com/simple-icons/simple-icons |
| Hugeicons | `hugeicons` | MIT | 6141 | https://github.com/hugeicons/hugeicons |

## Not in this repo

Remix Icon is not included. Its license allows the icons inside an app, and it forbids distributing them as a standalone icon library or a competing icon set. Putting the full set in this public repo would break that rule. Use the upstream project if you want those icons inside your own product: https://github.com/Remix-Design/RemixIcon

Simple Icons are brand marks. The SVG code is CC0. The names are still trademarks of their owners. Read `simple-icons/DISCLAIMER.md` before you use a logo.

## Identity

```json
{
  "name": "nasui",
  "make": "nasui",
  "brand": "nasmedia"
}
```
