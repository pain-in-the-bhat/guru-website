# ROADMAP

Planned improvements for gurubhat.

## Near Term

- Keep the homepage lean: hero, start-here path, latest writing, footer.
- Continue using `writing.html` as the full archive.
- Add new posts through `scripts/build-site.py` so RSS, sitemap, `llms.txt`,
  article metadata, and post navigation stay in sync.
- Watch Google Search Console after sitemap submission and request reindexing
  for the homepage after major title/description changes.
- Add the site to public profiles: LinkedIn, X, GitHub profile README, and any
  other durable identity surfaces.

## Content

- Add a few posts outside the narrow AI lane when they naturally fit the site:
  internet culture, Indian tech, China, books, work, status, and strange markets.
- Maintain the "start here" path as the best four-entry route for new readers.
- Consider a short annual or quarterly index note if the archive grows enough
  that readers need orientation.

## Design

- Keep Newsreader for now. Revisit display type only after the homepage rhythm
  feels settled.
- Avoid adding thumbnails, cards, sidebars, share widgets, or newsletter CTAs.
- Make dense link sections feel editorial: quiet by default, expressive on
  hover.
- Keep mobile checks mandatory for hero, archive, and post navigation changes.

## Technical

- Make `scripts/build-site.py` the single source of truth for post metadata.
- Consider generating the homepage latest list from the same script once the
  layout stabilizes.
- Consider extracting the repeated email reveal script only if the site grows
  enough for repetition to become painful.
- Add a simple pre-push check that runs the build script, validates XML/JSON-LD,
  and checks local links.

## Later

- Add "more in this thread" navigation if the current previous/next flow is not
  enough.
- Add a lightweight colophon page if the design system becomes part of the
  site's identity.
- Add a small `grulab` bridge only if the experiments become central to the
  public site.
