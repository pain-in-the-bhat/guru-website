#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://gurubhat.xyz"
AUTHOR = "Gurudas Bhat"
SITE_DESCRIPTION = (
    "Essays by Gurudas Bhat on technology, ambition, internet culture, work, "
    "status, and the strange ways the present enters ordinary life."
)


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    date: str
    label: str
    read_time: str
    post_type: str
    description: str

    @property
    def href(self) -> str:
        return f"posts/{self.slug}.html"

    @property
    def url(self) -> str:
        return f"{SITE_URL}/{self.href}"

    @property
    def date_label(self) -> str:
        value = datetime.strptime(self.date, "%Y-%m-%d")
        return f"{value.strftime('%B')} {value.day}, {value.year}"

    @property
    def rss_date(self) -> str:
        value = datetime.strptime(self.date, "%Y-%m-%d")
        return value.strftime("%a, %d %b %Y 10:00:00 +0530")


POSTS = [
    Post(
        "the-social-cost-of-not-knowing",
        "The Social Cost of Not Knowing",
        "2026-06-05",
        "field note",
        "5 min read",
        "field note",
        "On ChatGPT, Amma, and the private relief of asking questions without being judged.",
    ),
    Post(
        "in-a-very-chinese-time-of-my-life",
        "In a Very Chinese Time of My Life",
        "2026-06-04",
        "internet weather",
        "5 min read",
        "internet weather",
        "On DeepSeek, dramas, supply chains, and the strange intimacy of geopolitical fascination.",
    ),
    Post(
        "aesthetics-of-intelligence",
        "The Aesthetics of Intelligence",
        "2026-06-01",
        "taste note",
        "9 min read",
        "taste note",
        "On knowledge graphs, terminal screenshots, and the market for looking like you are thinking.",
    ),
    Post(
        "formula-one-cars-for-grocery-runs",
        "Formula One Cars for Grocery Runs",
        "2026-05-29",
        "minor obsession",
        "8 min read",
        "minor obsession",
        "On overbuilt AI workflows, productivity theatre, and why impressive machinery still needs somewhere meaningful to go.",
    ),
    Post(
        "smolgate",
        "smolgate, or How I Learnt to Be Okay With Smaller Context Windows",
        "2026-05-24",
        "working theory",
        "8 min read",
        "working theory",
        "On context windows, hoarding, and the fantasy that more memory equals better thought.",
    ),
    Post(
        "goldilocks-conundrum",
        "The Goldilocks Conundrum for AI Enthusiasts",
        "2026-05-17",
        "field note",
        "9 min read",
        "field note",
        "On model maximalism, capability theatre, and learning when not to call the CEO to decide lunch.",
    ),
    Post(
        "cheap-intelligence",
        "Cheap Intelligence Changes Human Psychology More Than Smarter Intelligence",
        "2026-05-10",
        "argument",
        "9 min read",
        "argument",
        "On token anxiety, abundant retries, and the weird freedom of not treating every prompt like a prayer.",
    ),
    Post(
        "the-system-that-eats-itself",
        "The System That Eats Itself",
        "2026-05-03",
        "systems note",
        "12 min read",
        "systems note",
        "On context drift, compaction, and why the human still has to hold the telos.",
    ),
    Post(
        "tsa",
        "Tsa",
        "2026-04-26",
        "useful suspicion",
        "10 min read",
        "useful suspicion",
        "On Tibetan monks, sycophantic AI, and why your LLM is too agreeable to be useful.",
    ),
    Post(
        "the-harness-is-the-moat",
        "The Harness Is the Moat",
        "2026-04-19",
        "operator note",
        "15 min read",
        "operator note",
        "On AI, knowledge work, and a Sunday night in Bangalore that got away from me.",
    ),
    Post(
        "what-we-lost-on-the-way-to-faster",
        "What We Lost on the Way to Faster",
        "2026-04-12",
        "medium theory",
        "7 min read",
        "medium theory",
        "On typing, voice input, and the friction that was doing something.",
    ),
    Post(
        "usage-anxiety",
        "Usage Anxiety",
        "2026-04-05",
        "minor condition",
        "9 min read",
        "minor condition",
        "Like range anxiety, but for your thinking.",
    ),
    Post(
        "hello-world",
        "Hello, world",
        "2026-04-01",
        "opening note",
        "3 min read",
        "opening note",
        "A short first note on what this place is for, and why a quiet corner of the internet still feels worth making.",
    ),
]

PAGES = [
    ("", "2026-06-05", "weekly"),
    ("writing.html", "2026-06-05", "weekly"),
    ("about.html", "2026-06-05", "monthly"),
    ("proof-of-work.html", "2026-06-05", "monthly"),
    ("shelf.html", "2026-06-05", "monthly"),
]

EMAIL_SCRIPT = """    <script>
      (() => {
        const reverse = (value) => [...value].reverse().join("");
        document.querySelectorAll(".email-reveal").forEach((node) => {
          const button = node.querySelector("button");
          if (!button) return;

          button.addEventListener("click", () => {
            const email = reverse(node.dataset.user) + "@" + reverse(node.dataset.domain);
            const link = document.createElement("a");
            link.href = "mailto:" + email;
            link.textContent = email;
            node.replaceChildren(link);
          }, { once: true });
        });
      })();
    </script>"""


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def nav(prefix: str = "") -> str:
    return f"""      <nav aria-label="Primary navigation">
        <a href="{prefix}writing.html">Writing</a>
        <a href="{prefix}proof-of-work.html">Proof</a>
        <a href="{prefix}shelf.html">Shelf</a>
        <a href="{prefix}about.html">About</a>
      </nav>"""


def footer(prefix: str = "") -> str:
    return f"""    <footer class="site-footer">
      <p><span class="email-reveal" data-user="tahbsadurug" data-domain="moc.kooltuo"><button type="button">reveal email</button></span> · <a href="https://www.linkedin.com/in/gurudas-bhat/">linkedin</a> · <a href="https://x.com/PainInTheBhat">x</a> · <a href="{prefix}feed.xml">rss</a></p>
    </footer>
{EMAIL_SCRIPT}"""


def build_writing() -> None:
    rows = []
    for post in POSTS:
        rows.append(f"""        <article class="archive-item">
          <a href="{post.href}">
            <span class="post-type">{esc(post.post_type)}</span>
            <time datetime="{post.date}">{post.date_label}</time>
            <h2>{esc(post.title)}</h2>
            <p>{esc(post.description)}</p>
          </a>
        </article>""")

    content = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Writing | gurubhat</title>
    <meta
      name="description"
      content="All essays by Gurudas Bhat on gurubhat."
    >
    <link rel="canonical" href="{SITE_URL}/writing.html">
    <link rel="alternate" type="application/rss+xml" title="gurubhat" href="feed.xml">
    <meta property="og:title" content="Writing | gurubhat">
    <meta property="og:description" content="All essays by Gurudas Bhat on gurubhat.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{SITE_URL}/writing.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
      href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Newsreader:opsz,wght@6..72,500;6..72,600;6..72,700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600&display=swap"
      rel="stylesheet"
    >
    <link rel="stylesheet" href="styles.css?v=4">
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="index.html">gurubhat</a>
{nav()}
    </header>

    <main class="page-shell">
      <section class="page-hero" aria-labelledby="writing-title">
        <p class="eyebrow">Writing</p>
        <div>
          <h1 id="writing-title">The public notebook, in order.</h1>
          <p>
            Essays, field notes, useful suspicions, and other attempts to get
            more precise about the present.
          </p>
        </div>
      </section>

      <section class="archive-list" aria-label="All essays">
{chr(10).join(rows)}
      </section>
    </main>

{footer()}
  </body>
</html>
"""
    write("writing.html", content)


def build_feed() -> None:
    items = []
    for post in POSTS:
        items.append(f"""    <item>
      <title>{esc(post.title)}</title>
      <link>{post.url}</link>
      <guid>{post.url}</guid>
      <pubDate>{post.rss_date}</pubDate>
      <description>{esc(post.description)}</description>
    </item>""")
    write(
        "feed.xml",
        f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>gurubhat</title>
    <link>{SITE_URL}/</link>
    <description>{esc(SITE_DESCRIPTION)}</description>
    <language>en-us</language>
{chr(10).join(items)}
  </channel>
</rss>
""",
    )


def build_sitemap() -> None:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, lastmod, changefreq in PAGES:
        loc = f"{SITE_URL}/{path}"
        lines.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
  </url>""")
    for post in POSTS:
        lines.append(f"""  <url>
    <loc>{post.url}</loc>
    <lastmod>{post.date}</lastmod>
    <changefreq>monthly</changefreq>
  </url>""")
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")


def build_llms() -> None:
    essay_lines = [
        f"- [{post.title}]({post.url}): {post.description}" for post in POSTS
    ]
    content = f"""# gurubhat

> A public notebook by Gurudas Bhat, trying to notice the present before it becomes obvious.

This site contains essays on technology, ambition, internet culture, work, status, AI, product, and the strange ways the present enters ordinary life.

## Main Pages

- [Home]({SITE_URL}/): Latest essays and working threads.
- [Writing]({SITE_URL}/writing.html): Full archive of published essays.
- [About]({SITE_URL}/about.html): About Gurudas Bhat and the site.
- [Proof of Work]({SITE_URL}/proof-of-work.html): Work, education, and signals behind the writing.
- [Shelf]({SITE_URL}/shelf.html): Books and inputs behind the site.
- [RSS]({SITE_URL}/feed.xml): Feed of published essays.

## Essays

{chr(10).join(essay_lines)}
"""
    write("llms.txt", content)


def article_json_ld(post: Post) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post.title,
        "description": post.description,
        "datePublished": post.date,
        "dateModified": post.date,
        "url": post.url,
        "author": {"@type": "Person", "name": AUTHOR, "url": f"{SITE_URL}/about.html"},
        "publisher": {"@type": "Person", "name": AUTHOR, "url": f"{SITE_URL}/about.html"},
        "mainEntityOfPage": post.url,
    }
    payload = json.dumps(data, ensure_ascii=False, indent=8)
    return f'    <script type="application/ld+json">\n{payload}\n    </script>'


def nav_block(prev_post: Post | None, next_post: Post | None) -> str:
    pieces = ['        <nav class="post-nav" aria-label="Essay navigation">']
    if prev_post:
        pieces.append(f"""          <a class="post-nav-link" href="{prev_post.slug}.html">
            <span>Previous</span>
            <strong>{esc(prev_post.title)}</strong>
          </a>""")
    else:
        pieces.append('          <span class="post-nav-link is-empty" aria-hidden="true"></span>')
    if next_post:
        pieces.append(f"""          <a class="post-nav-link" href="{next_post.slug}.html">
            <span>Next</span>
            <strong>{esc(next_post.title)}</strong>
          </a>""")
    else:
        pieces.append('          <span class="post-nav-link is-empty" aria-hidden="true"></span>')
    pieces.append("        </nav>")
    return "\n".join(pieces)


def update_posts() -> None:
    for index, post in enumerate(POSTS):
        path = ROOT / post.href
        text = path.read_text(encoding="utf-8")

        text = re.sub(
            r'\s*<script type="application/ld\+json">\s*\{.*?"@type": "Article".*?\}\s*</script>',
            "",
            text,
            flags=re.S,
        )
        text = text.replace(
            '    <link rel="preconnect" href="https://fonts.googleapis.com">',
            article_json_ld(post) + '\n    <link rel="preconnect" href="https://fonts.googleapis.com">',
            1,
        )

        text = re.sub(
            r'        <nav class="post-nav" aria-label="Essay navigation">.*?        </nav>\n',
            "",
            text,
            flags=re.S,
        )
        prev_post = POSTS[index + 1] if index + 1 < len(POSTS) else None
        next_post = POSTS[index - 1] if index > 0 else None
        text = text.replace("      </article>", nav_block(prev_post, next_post) + "\n      </article>", 1)

        text = text.replace('<a href="../index.html#essays">Essays</a>', '<a href="../writing.html">Writing</a>')
        text = text.replace('<a class="back-link" href="../index.html">Index</a>', '<a class="back-link" href="../writing.html">Writing</a>')
        text = re.sub(
            r'<p><a href="../index.html">gurubhat</a> ·.*?</p>',
            '<p><a href="../index.html">gurubhat</a> · <a href="../writing.html">writing</a> · <span class="email-reveal" data-user="tahbsadurug" data-domain="moc.kooltuo"><button type="button">reveal email</button></span> · <a href="https://www.linkedin.com/in/gurudas-bhat/">linkedin</a> · <a href="https://x.com/PainInTheBhat">x</a></p>',
            text,
            count=1,
        )
        path.write_text(text, encoding="utf-8")


def validate() -> None:
    ET.parse(ROOT / "feed.xml")
    ET.parse(ROOT / "sitemap.xml")
    for post in POSTS:
        path = ROOT / post.href
        if not path.exists():
            raise SystemExit(f"Missing post: {post.href}")


def main() -> None:
    build_writing()
    build_feed()
    build_sitemap()
    build_llms()
    update_posts()
    validate()
    print("Built writing.html, feed.xml, sitemap.xml, llms.txt, and post metadata.")


if __name__ == "__main__":
    main()
