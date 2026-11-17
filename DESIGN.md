---
name: Portal Documentation
description: Community documentation for the Battlefield Portal editor — a dark, steel-and-signal system built for long reading.
colors:
  # Primary — the one thing to act on
  signal-violet: "#bd4ffd"
  signal-violet-hi: "#d18bfd"
  signal-violet-ink: "#150222"
  # Teal replaces the accent inside the 2042 docs, and nowhere else
  teal-2042: "#2fe0c8"
  teal-2042-hi: "#7af2e1"
  teal-2042-ink: "#021a17"
  # Secondary — steel for headlines and secondary controls
  cold-steel: "#a9b9c9"
  cold-steel-hi: "#c9d4de"
  cold-steel-ink: "#0b0e11"
  # State signals
  warn: "#f2b233"
  danger: "#f0524d"
  # Neutral surfaces, darkest first
  ink-base: "#090a0b"
  ink-1: "#0f1113"
  ink-2: "#15181b"
  ink-3: "#1c2024"
  rule: "#22272c"
  rule-strong: "#363d44"
  text: "#e9edf0"
  text-quiet: "#a4aeb9"
  text-muted: "#7a8591"
  # Code, the five colors of the site
  code-text: "#c8d1da"
  code-keyword: "#ff8a65"
  code-string: "#9fd6a0"
  code-comment: "#5d6873"
  code-name: "#8fc1ea"
typography:
  display:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(38px, 4.6vw, 60px)"
    fontWeight: 800
    lineHeight: 0.93
    letterSpacing: "0.005em"
  headline:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(30px, 3vw, 42px)"
    fontWeight: 800
    lineHeight: 0.98
    letterSpacing: "0.005em"
  title:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "0.02em"
  body:
    fontFamily: "Barlow, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "15.5px"
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: "0em"
  label:
    fontFamily: "JetBrains Mono, ui-monospace, SF Mono, Menlo, monospace"
    fontSize: "11px"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.14em"
  nav:
    fontFamily: "Barlow, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.09em"
  code:
    fontFamily: "JetBrains Mono, ui-monospace, SF Mono, Menlo, monospace"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"
rounded:
  none: "0px"
spacing:
  hair: "6px"
  gap: "10px"
  pad: "14px"
  gutter: "22px"
  inline-sm: "16px"
  inline-md: "24px"
  inline-lg: "32px"
  section: "44px"
components:
  button:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    typography: "{typography.nav}"
    rounded: "{rounded.none}"
    padding: "0 18px"
    height: "40px"
  button-hover:
    backgroundColor: "rgb(169 185 201 / 0.06)"
    textColor: "{colors.text}"
  button-accent:
    backgroundColor: "{colors.signal-violet}"
    textColor: "{colors.signal-violet-ink}"
    typography: "{typography.nav}"
    rounded: "{rounded.none}"
    padding: "0 18px"
    height: "40px"
  button-accent-hover:
    backgroundColor: "{colors.signal-violet-hi}"
    textColor: "{colors.signal-violet-ink}"
  card:
    backgroundColor: "{colors.ink-1}"
    rounded: "{rounded.none}"
    padding: "13px 15px 14px"
  card-hover:
    backgroundColor: "{colors.ink-2}"
  hint:
    backgroundColor: "{colors.ink-1}"
    rounded: "{rounded.none}"
    padding: "12px 15px 13px"
  icon-button:
    backgroundColor: "transparent"
    textColor: "{colors.text-quiet}"
    rounded: "{rounded.none}"
    size: "36px"
  sidenav-link:
    backgroundColor: "transparent"
    textColor: "{colors.text-quiet}"
    rounded: "{rounded.none}"
    padding: "6px 10px"
  search-result:
    backgroundColor: "{colors.ink-2}"
    rounded: "{rounded.none}"
    padding: "9px 11px"
---

# Design System: Portal Documentation

## Overview

**Creative North Star: "The Mission Briefing"**

The site is a dark command deck that has already read the file and is telling you what matters. Steel headlines are set in condensed uppercase, the small print is mono, and the whole surface is square, hairline-ruled, and quiet — until something is actionable, at which point one signal violet appears and nothing else does. It is industrial and high-contrast without raising its voice: the palette is nearly black, the type carries the hierarchy, and every border is a single pixel.

Atmosphere is built from two moves and no more. Tonal surfaces step from ink-base through ink-3 so that a card, a callout, or a search field sits on the page rather than floating above it. And a hairline rule (#22272c) separates every region, doubling on hover to rule-strong (#363d44). The page itself is flat ink — no texture, no pattern, nothing behind the type.

Motion is small and instrumental: 0.12–0.2s transitions on a single curve, buttons and cards shifting border color, cards lifting 2px on hover with corner ticks fading in. Nothing bounces, nothing glows, nothing scrolls itself. The system is for readers who arrive mid-task, so every choice above the fold earns its place by making the answer easier to find, and anything decorative that does not is absent.

**Key Characteristics:**
- Dark ink base (#090a0b) with four deliberate surface steps and no shadows at all.
- Square everywhere: radius 0, 1px hairlines, corner brackets, no pills.
- Condensed uppercase display type against 15.5px body copy capped at 54em.
- Mono for every caption, label, table head, and tab — the instrument layer.
- One accent per page: signal violet (#bd4ffd), or 2042 teal (#2fe0c8) inside the 2042 docs, never both.

## Colors

The palette is a near-black instrument panel with one heated accent and a cool steel for type.

### Primary
- **Signal Violet** (#bd4ffd): the accent for the things to act on — the primary button, the active section underline, the sidebar's current-page rail, search match highlights, focus rings. Accent-hover is **Signal Violet Hot** (#d18bfd); text placed on the accent is **Signal Ink** (#150222).
- **2042 Teal** (#2fe0c8): the same role, swapped wholesale under `[data-game="bf2042"]` — the teal is applied to entire 2042 doc pages at the body element. Light variant **2042 Teal High** (#7af2e1), ink **Teal Ink** (#021a17).

### Secondary
- **Cold Steel** (#a9b9c9): the structural secondary — the default hint rail, hint titles, and the border a quiet button reaches for on hover. **Cold Steel High** (#c9d4de) is the display-type color: hero and page H1, prose H4–H6, prose links, card titles, the footer wordmark, and the 404 numeral. **Steel Ink** (#0b0e11) is defined for text placed on a steel fill and is not used anywhere yet.

### Tertiary
- **Amber Warning** (#f2b233): important/warning/caution hints only — the left rail and the hint's mono title.
- **Alert Red** (#f0524d): danger hints, deletions in diffs, and error lines. Never used for emphasis.

### Neutral
- **Ink Base** (#090a0b): the page, and the sticky header, which is the same flat ink with no rule under it.
- **Ink 1** (#0f1113): resting containers — cards, code blocks, hints, tables, the preview of a tab panel.
- **Ink 2** (#15181b): hover state for those containers, inline code, the code-copy button, the drawer's navigation.
- **Ink 3** (#1c2024): the fourth surface step, defined but not yet used — reach for it only when ink-2 is not a sufficient step away from its surroundings.
- **Rule** (#22272c): every default border and divider. **Rule Strong** (#363d44): a border that has been reached for — hover, table head underline, keycap outlines, scrollbars.
- **Body Ink** (#e9edf0) at full strength for prose headings and strong text; **Quiet Text** (#a4aeb9) for body copy and navigation; **Muted Text** (#7a8591) for metadata, captions, and list markers.

### Code
Five colors and no rainbow: **Code Body** (#c8d1da), **Code Keyword** (#ff8a65, also the operator family), **Code String** (#9fd6a0, also insertions), **Code Comment** (#5d6873, italic), **Code Name** (#8fc1ea, functions, types, headings). Syntax highlighting that needs a sixth color is using the wrong color.

### Named Rules
**The One Signal Rule.** Accent appears on ≤10% of any viewport and only where the reader can act or is already standing: primary actions, the current item, the focused element, the matched search term. Its rarity is the whole point — a screen with two violet things has no signal.

**The Teal Means 2042 Rule.** Teal exists to mark Battlefield 2042 documentation and never appears as a second accent on a 2042 page. No page shows both violet and teal.

**The Steel Is Type Rule.** Cold steel is a typographic color, not a background or a border fill. Surfaces are ink; steel is what is written on them.

## Typography

**Display Font:** Big Shoulders Display (with Arial Narrow, sans-serif)
**Body Font:** Barlow (with system-ui, -apple-system, Segoe UI, sans-serif)
**Label/Mono Font:** JetBrains Mono (with ui-monospace, SF Mono, Menlo, monospace)

**Character:** A condensed industrial display face does all the shouting in uppercase, a plain grotesk does all the reading at a comfortable 15.5px, and a mono carries every instrument caption — labels, table heads, tab names, keycaps, code. The pairing reads as signage + manual + readout, which is exactly the three jobs the site does.

### Hierarchy
- **Display** (800, `clamp(38px, 4.6vw, 60px)`, line-height 0.93): the home hero only. Uppercase, steel-high, letter-spacing 0.005em — condensed enough that tight tracking is the default, not a trick.
- **Headline** (800, `clamp(30px, 3vw, 42px)`, line-height 0.98): the page title in the page head. Same uppercase steel-high treatment one step down.
- **Title** (700, 22px / h1 28px, line-height 1.08, letter-spacing 0.02em): prose headings. Uppercase, full-strength `text`, so a page's structure is legible at a scan.
- **Body** (400, 15.5px, line-height 1.65, max 54em): all prose. Quiet Text (#a4aeb9), never pure white — the contrast sits at a level that survives 40 minutes of reading on ink-base.
- **Label** (500, 11px, letter-spacing 0.14em, uppercase, mono, Muted Text): eyebrows, section titles, hint titles, footer column heads, table headers, card metadata. The instrument layer.
- **Nav** (600, 13px, letter-spacing 0.09em, uppercase, Barlow): buttons and the prev/next labels. Slightly less tracked than the mono label so a nav element does not read as caption.
- **Code** (400, 13px, line-height 1.6, mono, Code Body): fenced blocks; inline code drops to 0.87em with a 1px rule and ink-2 fill.

### Named Rules
**The Two-Face Rule.** Uppercase belongs to Big Shoulders and mono labels. Body copy is never tracked, never uppercase, never condensed — Barlow at 15.5px/1.65 is the reading voice and it does not get a costume.

**The 54em Rule.** Prose never exceeds 54em (roughly 70 characters at this size); the hero body caps at 46em. Widening a text column is not a way to fill space — the third rail column exists for that.

## Layout

A three-column documentation grid inside a 1424px wrap: a 272px sticky nav column, a fluid content column, and a 216px sticky rail for on-page headings — the rail appearing only at ≥1360px, where the content column still clears a readable measure beside it. The nav pins under the header and scrolls up under it again at the end of a short page, once the footer takes the rest of main. Below 1024px the nav column becomes a drawer (min(320px, 86vw), sliding from the left, ink-base, with a 60% black scrim) and the page headings fold into a single `details` block above the article.

Horizontal padding steps 16px → 24px (≥640px) → 32px (≥1024px) on the wrap and the grid, and the grid gap is 44px between nav column and content, 40px before the rail. Vertical rhythm is set by the content, not a token scale: a 60px sticky header, 22px padding above the page head, 18px below it, and 0.9em between prose blocks — with 1.7em above headings, which is what makes a long reference page scannable.

Responsive breaks: 639px (header sheds the community icons), 720px (footer grid goes three columns), 1024px (nav column appears, the drawer button goes), 1100px (the search button gains its label and `/` keycap), 1360px (rail column appears, mobile TOC hides).

## Elevation & Depth

There are no shadows in this system. Depth is tonal and it is delivered by exactly three mechanisms: a step up the ink ladder (base → ink-1 → ink-2 → ink-3), a hairline border that darkens from rule to rule-strong when the element is reached for, and a 2px upward translation on card hover. The only `box-shadow` in the entire stylesheet is an inset 2px accent underline on the active tab — a rule, not a shadow.

Two exceptions, both atmosphere rather than depth: the sticky header sits on ink-base with no border under it, so it reads as part of the page, and the page head keeps a hairline rule under the title to close the top of the article.

### Named Rules
**The Flat-By-Decree Rule.** No outer shadows, no glows, no blurs, no textures or patterns on the page. If an element needs to come forward, it changes surface color or border color, or it moves 2px. A shadow is a bug.

## Shapes

Radius is 0 everywhere: buttons, cards, hints, tabs, tables, code blocks, the search dialog, the drawer, icon buttons. Borders are 1px, and the only 2px line in the system is a semantic one (the left rail of a hint, the top of the active tab underline).

The form language is bracketed and angular. Cards grow accent corner ticks on hover — four 12px L-brackets drawn with gradients at their corners, like a targeting reticle settling on the target. Chevrons are 14px, drawn at 1.6px stroke, and rotate 90° to open a section. The brand mark is the Portal chevron: an angular, two-segment arrow, fill-current, 40×35px in the header. Nothing in the system is a pill, a blob, or a circle; even the icon button is a 36px square.

### Named Rules
**The Dead Square Rule.** Radius 0. A new component that would look better rounded does not belong in this system; find the edge, the bracket, or the rule instead.

**The Bracket Rule.** Corner ticks mark the element under the cursor, and they are the only chrome that ever appears on hover besides a border and a background step. They do not animate on entry beyond a 0.16s opacity fade, and they never appear at rest.

## Components

### Buttons
- **Shape:** square (0 radius), 1px border, 40px tall (`btn--large` 44px), 18px inline padding (`btn--large` 22px).
- **Quiet (default):** transparent fill, rule-strong border, `text` color, uppercase Nav type at 13px/600/0.09em.
- **Hover:** border to cold-steel (#a9b9c9), background to a 6% steel wash (`rgb(169 185 201 / 0.06)`) — a border lighting up, not a fill arriving.
- **Primary (`btn--accent`):** solid signal violet, signal ink text, border same as fill; hover moves fill and border to signal-violet-hi. Used once per view, for the single primary action — on the home hero, that is the search button.
- **Focus:** a 2px accent outline at 2px offset, global, never a ring inside the button.

### Cards
- **Corner style:** square, 1px rule border, ink-1 fill, 13px/15px/14px padding.
- **Structure:** display-face card title (17px/700, uppercase, steel-high), optional mono meta line (10.5px, 0.12em, muted), optional Barlow description (13.5px/1.45, quiet).
- **Hover:** border to rule-strong, fill to ink-2, 2px lift, corner brackets fade in (0.16s).

### Hints / Callouts
- **Style:** ink-1 fill, 1px rule border on three sides and a 2px semantic rail on the left — steel for note, violet for tip, amber for important/warning/caution, red for danger.
- **Title:** mono 11px/0.14em uppercase, colored with the rail's color, preceded by a 15px icon (info for note, alert otherwise).
- **Body:** 14.5px quiet text, not the 15.5px prose measure — a callout is a margin note, not a chapter.
- Hints keep their rail color and never carry a background tint; a tinted callout would fight the tonal ladder.

### Tabs
- **Style:** a bordered grid inside ink-1, labels as mono 11px/0.12em uppercase in muted text, separated by 1px rules; panels sit below, full width, 15–16px padding.
- **State:** the checked label gets full `text` color, ink-2 fill, and the system's one inset shadow — a 2px accent underline. Focus draws a 2px accent outline inset by −2px.
- **Hidden radios** give keyboard and screen-reader behavior for free; a single-tab group renders its content with no labels at all.

### Navigation
- **Header:** the mark alone on the left, search and the two community links on the right, nothing between. The sections live in the sidebar and the site is named by the page itself, so neither is repeated here; below 1024px the sidebar is the drawer behind the menu button. The mark and the sidebar's number column sit on the same 16px inset from the wrap, so that edge never moves between pages.
- **Sidebar:** the home page's section list and the document sidebar are one component, the rail (`rail__list` / `rail__item`): mono, 15px/600 steel, a `<n>` pointer in a 34px column and nothing drawn around the row. Only the eight sections are numbered — the number has to mean something. Everything under a section steps in 36px to sit under the section's name (16px for each level below), drops to 13px/500 quiet text, and loses the number. Hover fills ink-2 from 8px into the gutter so the label never moves; the current page is the only row that draws a line, a 2px accent tick at its edge. Sections are `<details>` with a 90°-rotating chevron, and rows fall back to 44px targets under `(pointer: coarse)`.
- **Page nav (prev/next):** two equal cards above the footer, mono direction label over the page title, next aligned right and pinned to column 2 when alone.

### Search
- **Surface:** a native `<dialog>` at min(720px, 100vw − 32px), ink-base fill, rule-strong border, 62% black backdrop, square. No radius, no shadow.
- **Field:** 16px input on ink-base with a bare icon, a placeholder in muted text, and a bordered `Esc` keycap.
- **Results:** each row a 2px transparent left rail that turns accent on hover/selection with an ink-2 fill; title at 14.5px/600 with an inline mono section tag, plus a two-line clamped excerpt in muted text. Matched text is accent-colored and bold, never highlighted with a background.

### Code Blocks
- **Surface:** ink-1 with a 1px rule, 16px padding, 13px mono at 1.6 line-height, thin scrollbars.
- **Tools:** language label and copy button appear on hover at 0.15s, and are permanently visible under `@media (hover: none)`. The copy button confirms by turning its border and label accent for as long as `data-copied="true"`.
- **Inline code:** 0.87em mono with a 1px rule and ink-2 fill — a chip made of lines, not a rounded tag.

### Block Pages
A generated rule-editor block page (`layout: block_documentation`) has its own anatomy, because most of its content is produced, not written.

- **Title:** the `<h1>` is generated content, not page chrome — `page-head.html` deliberately omits it here, along with the breadcrumb's current item. It renders at prose-h1 scale (28px) rather than the 30–42px headline, and the crumbs end at the section.
- **Source row:** because the title is generated, the source link follows the article (`.page-meta`, 13px quiet text, 34px of air) instead of sitting above it. Its label reads **Add a note**, not *Edit this page*, because the file it opens is the block's `extra.md`.
- **Community notes:** always rendered as an `h2`, above the source row. The empty state is one 1px-ruled ink-1 panel with a single paragraph of invitation and no button inside it — the source row below carries the only action, so the page never offers the same link twice.
- **Illustration:** the generated screenshot is content, not chrome. It keeps the 1px rule and ink-1 framing every prose image gets, takes its caption from the markdown title, and ships at whatever size the source is.
- **On-page headings:** a generated page's appended headings are not in `.TableOfContents`, so the rail and the folded mobile box are suppressed below two entries rather than showing a list of one.

### Named Rules
**The Artwork Is Data Rule.** A block illustration ships in its own colours because the hue *is* the block's category in the rules editor — it is how readers recognise one block from another. Never recolour, tint, filter, or restyle that artwork to match the palette. Frame it and leave the pixels alone.

**The Generated Title Rule.** On a block page the title belongs to the generated article. The page head supplies crumbs only, and the source row follows the article. Moving the title into the template would duplicate it; don't.

## Do's and Don'ts

### Do:
- **Do** keep accent usage under 10% of the viewport and only on actionable or current-state elements (The One Signal Rule).
- **Do** build depth from the ink ladder (base #090a0b → ink-1 #0f1113 → ink-2 #15181b → ink-3 #1c2024) and a 1px border that shifts to rule-strong (#363d44) on interaction.
- **Do** set every caption, label, table head, tab name, and keycap in JetBrains Mono at 11px with 0.14em tracking.
- **Do** keep prose at 54em max, 15.5px, 1.65 line-height, in quiet text (#a4aeb9) — the reading environment is the product.
- **Do** use uppercase Big Shoulders for headings and square, bracket-marked containers for structure; both are load-bearing for the industrial read.
- **Do** swap the whole accent to 2042 teal (#2fe0c8) via `[data-game="bf2042"]` when the page documents Battlefield 2042.
- **Do** render a block page's Community notes section even when its `extra.md` is untouched — an empty slot that names what belongs in it is how a generated reference becomes a community one.
- **Do** keep generated block artwork at its shipped size and colour, with its caption, inside the standard prose image frame (The Artwork Is Data Rule).

### Don't:
- **Don't** add shadows, glows, gradient text, or blurred glass anywhere (The Flat-By-Decree Rule).
- **Don't** round a corner. No 2px, no 4px, no pills, no circles — a rounded element is a foreign object in this system (The Dead Square Rule).
- **Don't** show signal violet and 2042 teal on the same page, or use teal for anything outside Battlefield 2042 documentation.
- **Don't** drift gamer-neon (glow, neon gradients, targeted "esports" chrome), SaaS-marketing (gradient meshes, rounded soft cards, illustration blobs, social proof bars), or editorial-warm (serif body, cream paper, oversized italic pull quotes). All three are confirmed anti-references.
- **Don't** adopt Material defaults: no ripple, no elevation ladder, no 4/12px radii, no Roboto.
- **Don't** tint a hint's background with its semantic color, or use amber/red for emphasis — they mean warning and error, nothing else.
- **Don't** add a texture, dot grid, or pattern behind the page; the surface is flat ink.
- **Don't** put a rule or a translucent layer under the header; it is the same ink as the page.
- **Don't** recolour, tint, or restyle a generated block illustration to fit the palette — the colour is the block's category, not decoration.
- **Don't** move a block page's generated `<h1>` into the page head, or put the source link above it (The Generated Title Rule).
- **Don't** offer the same action twice on one page: the notes panel has no button because the source row below already is one.
