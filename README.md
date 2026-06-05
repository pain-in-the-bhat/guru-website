# gurubhat

Static personal essay site for [gurubhat.xyz](https://gurubhat.xyz/).

## Preview locally

Open `index.html` in a browser, or serve the folder with any static file server.

## Publish on GitHub Pages

1. Create a GitHub repository for this folder.
2. Push these files to the default branch.
3. In GitHub, enable Pages for the branch that contains `index.html`.
4. Point `gurubhat.xyz` DNS at GitHub Pages.

The `CNAME` file is already set to `gurubhat.xyz`.

## Design identity

The site is editorial, typographic, restrained, and writing-first. The current
surface uses a warm paper palette, serif-led hierarchy, sparse navigation, and
no thumbnails, sidebars, or subscription prompts.

## Add a post

1. Copy `posts/hello-world.html` to a new file in `posts/`.
2. Update the title, date, canonical URL, and body.
3. Add the post metadata to `POSTS` in `scripts/build-site.py`.
4. Run `python3 scripts/build-site.py`.
5. Add the post to the homepage manually if it belongs in the latest list or
   start-here trail.

The script regenerates `writing.html`, `feed.xml`, `sitemap.xml`, `llms.txt`,
post-to-post navigation, and article JSON-LD.
