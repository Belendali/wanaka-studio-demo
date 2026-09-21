# Wanaka Studio · Create panel demo

Interactive HTML/CSS/JS reproduction of the Wanaka Studio "Create" flow from the Figma file
(section `0902/0903` + detail screens), built 1:1 at 1920×1080 and scaled to fit the browser window.

## Plan B · chat generation (3D flow)

`plan-b.html` explores the alternative layout: the left panel keeps the categories and the asset library, and generation happens in a dedicated **Create Assets** chat on the right so style stays continuous across assets.

Flow: pick **3D Model** (or **2D & UI** / **Character**) → **Generate now** opens `Create Assets 01` → describe what you need → result card → **Add to scene**. 2D results offer **Create 3D model**, which continues in the same chat. Review any step with `plan-b.html?step=1..7&cat=3D%20Model|2D%20%26%20UI|Character` (matches the Figma frames in sections 0909/0910 and the 2D & Character draft).

Live: https://belendali.github.io/wanaka-studio-demo/plan-b.html

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

### Asset chat management (Plan B)

- **Reuse by default**: Generate now jumps to the chat of that category the user opened most recently, and a small card asks “Continue in …?” with **Continue here** / **Start a new chat**. Sending a message also counts as continuing. If the user is already in that chat, no card is shown.
- **Drafts**: a new chat shows a Draft tag and is discarded if you leave before sending the first message.
- **Auto name** from the first prompt; rename inline from the row menu (F2, Enter to save, Esc to cancel).
- **Switcher**: Game / Assets tabs (opens on the tab of the current chat). Assets has search, All · 3D · 2D · Character filters, Pinned and Recent (by last activity); rows show first-result thumbnail, category badge, asset count, last activity. Game lists game chats with New game chat.
- **Row menu**: Rename · Pin to top / Unpin · Archive · Delete chat. Pin and archive toasts include Undo. Delete asks for confirmation and keeps the chat's assets in the library.
- **Archived** view with Restore.
- **Library card menu**: Add to scene · Continue in chat (reopens the chat that made the asset; disabled if that chat was deleted) · Download.

Review states: `plan-b.html?chats=menu|games|rowmenu|rename|archived|delete|lib|resume|draft`

## Layout

- `index.html` — page + styles + logic (`renderShell`, `renderPanel`, `generate`, `renderModal`)
- `assets/` — icons and images exported from Figma, plus processed cat resources
