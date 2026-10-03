# nasui

nasui is an icon collection made by nasui. The brand is nasmedia.

Each set lives in its own folder with the SVG files and metadata, so a person or a script can search by name, category, tag, and style.

## Pack layout

```
tabler/
├── svg/
│   ├── home.svg
│   └── home-fill.svg
├── metadata.json
└── LICENSE
```

`svg` holds the files. `metadata.json` describes them. `LICENSE` sits with that set. Keep that file with the icons if you copy the pack out.

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

You will see `outline`, `fill`, and `duotone`. Some sets also have `thin`, `light`, `bold`, `round`, `sharp`, `fill-20`, `fill-16`, `brand`, or `color`.

A search returns every matching pack and every style that pack actually ships.

## Find an icon

From this folder:

```
python scripts/search.py home
python scripts/search.py user --style fill
python scripts/search.py settings --json
```

A match can come from the id, the family, the label, or a tag. `--json` prints the matches for scripts and AI tools.

## Use a file

```
tabler/svg/home.svg
```

```
https://raw.githubusercontent.com/nasirtulore-ui/icon/main/tabler/svg/home.svg
```

Most stroke icons use `currentColor`, so CSS color changes them.

## Packs

25001 icons.

| Set | Folder | License | Icons |
| --- | --- | --- | --- |
| Tabler Icons | `tabler` | MIT | 5166 |
| Lucide | `lucide` | ISC | 1857 |
| Phosphor Icons | `phosphor` | MIT | 1512 |
| Heroicons | `heroicons` | MIT | 324 |
| Bootstrap Icons | `bootstrap` | MIT | 1409 |
| Fluent System Icons | `fluent` | MIT | 2919 |
| Material Design Icons | `material` | Apache-2.0 | 2209 |
| Simple Icons | `simple-icons` | CC0-1.0 | 3464 |
| Hugeicons | `hugeicons` | MIT | 6141 |

## Identity

```json
{
  "name": "nasui",
  "make": "nasui",
  "brand": "nasmedia"
}
```
