# Wanaka Studio · Create panel demo

Interactive HTML/CSS/JS reproduction of the Wanaka Studio "Create" flow from the Figma file
(section `0902/0903` + detail screens), built 1:1 at 1920×1080 and scaled to fit the browser window.

## Run

- Open `index.html` in a browser (assets are loaded from `assets/`), or
- open `wanaka-studio-single-file.html` — everything inlined, works from anywhere.

No build step, no dependencies. Fonts (Poppins, Bitcount Grid Single) load from Google Fonts.

## What it covers

- Create panel: Character / 2D & UI / 3D Model categories, Generate + My Assets tabs
- Prompt input with live counter, reference images (up to 5, wraps at 5/5), ratio / variants / toggles / pose
- Generate → generating cards with progress → results revealed in My Assets (grouped by batch)
- Asset detail modal: 2D (Create 3D model / Create Character), 3D (grid backdrop, Add Animation, Create Character), Character (turnaround animation, Add Animation)
- Add to scene: the asset lands in the viewport in an edit state (selection box, move gizmo, name tag); drag to move, Esc to deselect, Delete to remove
- Empty states, hover actions (favorite / add to scene), toasts
- Character flow uses the cat resources (`assets/cat.png`, `assets/cat-turn.webp`)

## URL hooks

- `?cat=3D%20Model` — open a category (`2D%20%26%20UI`, `3D%20Model`, `Character`)
- `?tab=assets` — open My Assets
- `?demo=I%20want%20a%20cute%20dog` — prefill the prompt and generate
- `?detail=1` — open the first result's detail after generation
- `?add=1` — place the first result into the scene after generation

## Layout

- `index.html` — page + styles + logic (`renderShell`, `renderPanel`, `generate`, `renderModal`)
- `assets/` — icons and images exported from Figma, plus processed cat resources
