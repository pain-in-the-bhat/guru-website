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

The site follows the identity brief in `design-identity-brief.md`: dark,
editorial, typographic, restrained, and writing-first. The title is the hero.
There are no thumbnails, cards, sidebars, or subscription prompts.

## Add a post

1. Copy `posts/hello-world.html` to a new file in `posts/`.
2. Update the title, date, canonical URL, and body.
3. Add the new post to `index.html`.
4. Add the new post to `feed.xml`.
