# gurubhat.xyz — Design Identity Brief

This document describes the design identity for gurubhat.xyz. Use it to make
every design and implementation decision. When in doubt, refer back here.

---

## What This Site Is

A personal blog by Gurudas Bhat — MBA student, former software engineer, 
aspiring VC, occasional poet. The writing covers AI, knowledge work, consulting,
internet culture, and the strange psychology of ambition. The tone is: a very
smart friend talking about something they went down a rabbit hole on at 2 AM.

The site's job: a recruiter or collaborator lands here and immediately understands
how this person thinks. Not what they've done — how they think. The design must
get out of the way of that and do it with confidence.

The blog is called **gurubhat** with the subtitle *Notes from an AI-Accelerated Midwit*.

---

## The One Design Principle

**The design should be invisible in service of the thinking.**

The moment a visitor notices the design more than the ideas, we've failed. What
we're after is the feeling of landing somewhere and immediately trusting the person
behind it has taste — without being able to articulate why.

This is not a portfolio. It is not a startup landing page. It is not a developer
blog with syntax highlighting and GitHub activity graphs. It is an essay site
that happens to be built by someone who can code.

---

## Aesthetic Direction

**Dark. Editorial. Typographic. Restrained with one or two moments of personality.**

References that are directionally correct:
- Craig Mod's newsletter/site (generous whitespace, serif-led, writing-first)
- The Browser (sparse, trusted, every element earns its place)
- Robin Sloan (personal but precise)
- Early Substack before it became homogeneous

References that are wrong:
- Any site that looks like a Notion export
- Developer blogs with card grids and tag filters
- Purple gradient on white (the generic AI aesthetic)
- Maximalist anything — the unit-zero piece (Evangelion-coded, scanlines, orange)
  is a one-off statement piece, NOT the blog's identity

---

## Colour

Dark background. Not pure black — something with a tiny amount of warmth.
Think: `#0D0D0B` or `#0F0E0C`. Feels like a well-lit room at night, not a terminal.

Text: warm off-white. `#E8E4DC` or similar. Never pure white — it's too harsh
against dark.

One accent colour. Used sparingly — link hovers, the occasional marker, the
blog name. Something with character. Options:
- A warm amber: `#C8953A`
- A muted terracotta: `#C4614A`  
- A desaturated gold: `#B8A060`

NOT orange neon. NOT electric blue. NOT anything that reads as "hacker" or "tech bro."
The accent should feel like it belongs in an old library, not a data centre.

Muted mid-tone for secondary text, dates, section labels: around `#6B6660`.

---

## Typography

This is the most important design decision on the site. Get this right and
everything else follows.

**Display / Headings:** A serif with personality at large sizes. Options:
- Playfair Display (classic, slightly dramatic)
- Cormorant Garamond (elegant, slightly unconventional)
- DM Serif Display (contemporary but still warm)

Whichever is chosen: used at large sizes for post titles on the homepage,
medium for post section headings. Let it breathe. Don't crowd it.

**Body:** A highly readable serif optimised for long-form reading.
- Lora (warm, designed for screens)
- Crimson Pro (what unit-zero uses for body — it works)
- Source Serif 4 (Google Fonts, excellent legibility)

NOT Inter. NOT system-ui. NOT anything sans-serif for the body. This is an
essay site. The body must be serif.

**Mono:** For any code, file paths, technical references within prose.
- JetBrains Mono (friendly, not aggressive)
- IBM Plex Mono (editorial, slightly refined)

**Scale:**
- Body: 18-19px, line-height 1.75-1.8
- Post width: 660-680px max. No wider. Long-form prose needs a narrow column.
- Generous paragraph spacing. Each paragraph should feel like it has room to breathe.

---

## Layout

**Homepage:**
- The blog name (gurubhat) at top left or centred, display typeface, large.
- Subtitle (*Notes from an AI-Accelerated Midwit*) beneath it, smaller, italic, muted.
- Navigation minimal: maybe just "writing" and "about". Nothing else.
- Post list: title, date, one-line description or opening sentence. No cards,
  no thumbnails, no category tags. Just titles and dates, well-spaced.
- No hero image. No banner. The title is the hero.

**Post page:**
- Post title: large, display typeface, generous top margin.
- Subtitle/tagline if present: italic, smaller, directly beneath.
- Reading time and date: small, muted, monospaced. Not prominent.
- Body: single column, 660px max, centred. Lots of whitespace either side.
- Section headings: smaller than you'd expect — they label, they don't shout.
- No sidebar. No related posts widget. No social share buttons cluttering the
  reading experience. A reader who finishes should feel like they just read
  something, not like they're being asked to do something immediately after.
- Footer: minimal. A quiet line at the bottom. Maybe just an email address
  or a link back to the index.

---

## What Gets Designed Once and Stays Consistent

- The type system (the two fonts, the scale, the leading)
- The colour variables (background, text, accent, muted)
- The maximum column width
- The header (blog name + minimal nav)
- The post list item format (title + date + one line)
- The post page shell (title block, body, footer)

Everything else is the writing's job.

---

## Personality Markers — Where the Restraint Gets One Break

The site is restrained. But restraint without personality is just blankness.
One or two places where character shows through:

**The blog name treatment:** `gurubhat` in the display typeface, slightly
larger than feels strictly necessary. This is the one moment of visual confidence.
The subtitle beneath it in a smaller italic is the wit to the name's seriousness.

**Link hover states:** Something slightly unexpected. Not just underline on hover —
maybe the accent colour bleeds in, or the text shifts weight subtly. Small,
noticed-but-not-announced.

**Horizontal rules / section dividers in posts:** Not a default `<hr>`.
A short centred mark — maybe three dots, maybe a short line 40px wide — that
feels like a breath between thoughts rather than a structural element.

**Dates and metadata:** Monospaced, small, slightly warm-muted. The kind of
typographic detail that someone who notices typography will appreciate.

---

## What This Site Is NOT

- Not a portfolio with case studies and project cards
- Not a newsletter with subscription CTAs above the fold
- Not a developer blog with syntax-highlighted code blocks everywhere
- Not a personal brand site with a headshot and a hero statement
- Not unit-zero (that aesthetic belongs to one specific experimental piece,
  not the whole blog)
- Not anything that looks like it was generated by an AI design tool

---

## The Test

When the site is done, ask: if you removed the author's name, would a reader
still feel like they were in a specific person's space — not a template,
not a theme, but somewhere that belongs to someone with a distinct way of
seeing things?

If yes: ship it.
If no: something is wrong with the typography or the colour or there's one
element too many. Remove until the answer is yes.
