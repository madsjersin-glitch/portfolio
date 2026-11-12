#!/usr/bin/env python3
"""Builds the three pages (Work, Approach, About) from the content below.

Edit the content, then run:  python3 build.py
Needs Pillow only to read image sizes (pip install pillow).
"""
import os
from html import escape as e
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "madsjersin@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/madsjersin/"
CV = "https://drive.google.com/file/d/1JuSTkis4ubju15cBtVHwm5WneKTmhr91/view?usp=sharing"

STATS = [
    ("9+", "Years in B2B SaaS"),
    ("2×", "First product marketing hire"),
    ("20+", "Launches owned"),
    ("~$0.5M", "Pipeline influenced by one launch"),
]

# Work: (id, eyebrow, title, one-liner, note, cover image, numbered steps?, [(caption, image)])
BOARDS = [
    ("positioning", "Website · Frameworks", "Positioning & messaging",
     "Moved Reshape’s story from what the hardware does to what it changes for the lab.",
     "The old and new website side by side, and the documents behind the change: a written positioning, a messaging framework and audience profiles for quality control (QC) and R&D labs.",
     "pos-new-website", False,
     [("Old website", "pos-old-website"), ("New website", "pos-new-website"), ("Positioning document", "pos-positioning"),
      ("Messaging framework", "pos-messaging"), ("Audience framework", "pos-audience")]),
    ("launches", "Experiments launch", "Product launches",
     "Ran launches from positioning and planning through sales training, rollout and adoption.",
     "The Experiments launch: every place a user meets the new feature, from the first tooltip to the help article. One of the launches run through Reshape’s tiered launch model.",
     "exp-feature-tour", False,
     [("In-app tooltips", "exp-tooltips"), ("Empty state", "exp-empty-state"), ("Clickable feature tour", "exp-feature-tour"),
      ("Launch email", "exp-launch-email"), ("Help article: Plate templates", "exp-kb-plate-templates"),
      ("Help article: Experiments", "exp-kb-experiments")]),
    ("onboarding", "Intercom · Help centre", "User onboarding",
     "Five emails, help articles and video guides that get every new user started, not only the admins.",
     "Each email points to a help article with a video guide, so new users can read or watch their way into the product. The story behind it is under Approach.",
     "onb-email", False,
     [("Onboarding email", "onb-email"), ("Video guides: Reshape 101", "onb-videos"),
      ("Help article: Starting a new job", "onb-article-job"), ("Help article: Discovery overview", "onb-article-overview")]),
    ("creative", "From script to film", "Creative production",
     "Wrote the scripts and mood boards for five campaign videos, and shaped the direction with a videographer and our designers.",
     "How one of them came together, from script to finished film.",
     "cre-final", True,
     [("Scripting", "cre-script"), ("Mood boarding", "cre-moodboard"), ("Design collaboration", "cre-design"), ("Final film", "cre-final")]),
    ("sales", "Enablement hub", "Sales support",
     "Built one hub where sales, customer success and marketing find decks, one-pagers, product guides and competitor notes.",
     "Used by everyone in the commercial teams, around 15 people.",
     "sal-decks", False,
     [("Enablement & sales collateral hub", "sal-hub"), ("Sales decks", "sal-decks"), ("Product guides", "sal-guides"),
      ("One-pagers", "sal-onepagers"), ("Competitive intel", "sal-compintel"), ("Internal feature overviews", "sal-feature-overviews")]),
    ("alignment", "Product × Commercial", "Cross-functional alignment",
     "Kept Product and Commercial in step with an internal changelog, feature training and one shared launch board.",
     "The quieter work that makes launches land.",
     "ali-launch-board", False,
     [("Internal product changelog", "ali-changelog"), ("Internal feature training", "ali-training"),
      ("Product launch coordination", "ali-launch-board")]),
]

# Approach: dicts with eyebrow, title, sub, results, why, how, bump, tags, shots, link
CASES = [
    dict(id="robot", eyebrow="Reshape Biotech · Product launch", title="Launching the robot",
         sub="Took Reshape’s first quality-control product into a new segment.",
         results=["100+ attendees from biotech companies worldwide", "The launch influenced ~$0.5M in pipeline"],
         why="Reshape’s imaging technology could serve quality control (QC), but QC buyers worry about different things than our existing customers. The product team built a robot for QC labs, the High-throughput Imaging Device, and I owned the launch end to end.",
         how="Repositioned the message around what QC cares about: time savings, data accuracy and a clear trail of every test when an auditor asks. Trained sales together with a co-founder, rewrote the website, made the launch videos with a videographer and our designer, ran a 45-minute online launch event and sent four email campaigns to four different audiences.",
         bump="Software was built after the hardware, but the videos and sales training needed a working product. Together with our designer I built clickable mockups showing how software and robot would work together, so the launch date didn’t have to wait.",
         tags="Positioning | Sales training | Video | Launch event | Email",
         shots=[("45-minute live launch event", "robot-event"), ("Launch video", "robot-video"), ("Landing page", "robot-landing"),
                ("Team training", "robot-training"), ("Product positioning", "robot-positioning"), ("Sales deck", "robot-deck")]),
    dict(id="onboarding-story", eyebrow="Reshape Biotech · User onboarding", title="Onboarding every new user, not just the admins",
         sub="A five-email, 30-day programme that reaches people while they are still in the product.",
         results=["~80% open rate across all five emails", "~35% click-through on the first email", "200–250 new users onboarded"],
         why="Administrators told me that the colleagues they invited landed in the product without knowing how to use it. Admins got a hands-on onboarding; everyone else got an invitation and silence.",
         how="Five emails over 30 days, following the work a new user actually does, each linking to a help article with a video guide. I wrote the copy, built the flow in Intercom, scripted and edited the videos and wrote the articles, with a data engineer from the marketing team on the data side and a customer success manager in front of the camera.",
         bump="The first email arrived far too late because product data synced once a day. We restructured the sync to run every 30 minutes, so the first email lands within half an hour of accepting the invitation.",
         tags="Lifecycle | Intercom | Video guides | Help centre",
         link=("See the onboarding screens", "#onboarding")),
    dict(id="invoices", eyebrow="Pleo · UK relaunch", title="Letting customers name the product",
         sub="Relaunched Pleo Bills as Pleo Invoices in the UK, and took it to market through bookkeeping partners.",
         results=["200 bookkeeping partners on board in about six months", "#2 Product of the Day on Product Hunt"],
         why="Pleo wanted to cover all company spend, not just card expenses, and invoices are a big share of it. A first UK attempt had run for about a year without traction.",
         how="In about 20 customer conversations, nine times out of ten the people who said “bills” added “we mean invoices”. So we renamed it, and the rename became the hook. I owned positioning, messaging and the go-to-market through partners: an enablement portal, a campaign video, website copy, targeted emails and a Product Hunt launch, with partner marketing, the brand team and two product teams.",
         bump="Everyone involved had competing priorities. Instead of asking for “more time”, I negotiated something concrete: two weeks of a motion designer and a dedicated budget for the launch.",
         tags="Naming | Positioning | Partner enablement | Video"),
    dict(id="pr", eyebrow="Pleo · PR around funding rounds", title="Making funding news worth a second story",
         sub="Took the CEO’s theme of attracting international talent to Denmark into the national debate.",
         results=["National TV and front pages of Børsen and Finans", "Roughly 3–4× the job applications after each round (est.)"],
         why="Funding rounds put Pleo in the spotlight and brought in applicants, but “startup raises money” gets old fast for journalists.",
         how="Owned all Danish media contact across Series A, B, C and a C extension. Wrote the press releases, gave each outlet its own angle, prepared the CEO with labour-market figures and kept pitching his talent theme through the Series B and the Danish election campaign.",
         bump="I learned the hard way not to pitch the same story to every outlet. From then on each got its own angle or an exclusive, which also helped on busy news days.",
         tags="PR | Press releases | Media relations | Employer brand"),
    dict(id="housing", eyebrow="Pleo · Targeted campaign", title="A campaign for ~300 supported housing facilities",
         sub="A small, well-defined audience, reached through their own national organisation.",
         results=["~30–40 booked meetings in two months"],
         why="Customer conversations kept showing the same thing: staff paid for residents’ shopping out of a shared cash box, and bookkeepers couldn’t see where the money went.",
         how="Mapped the ~300 facilities in Denmark into one list. Reached them through their national organisation’s newsletter and members’ magazine, display ads on sites care staff read, print ads with a QR code and paid campaigns run by our paid team, all pointing to one landing page with a first-year discount.",
         bump="The print and display partners couldn’t measure much. Tracked links and QR codes, matched against booked meetings, showed which channel actually worked.",
         tags="Campaign | Segmentation | Print + display | HubSpot"),
]

ROLES = [
    ("Reshape Biotech", "Mar 2024 → Oct 2026", "Senior Product Marketing Manager",
     "First product marketing hire. Ran the launch framework, and built the enablement hub, the onboarding programme and a pricing tool for sales that replaced a paid one."),
    ("Veo Technologies", "2022 → 2023", "Senior Product Marketing Manager",
     "First product marketing hire. Surveyed 300 coaches on how they used Veo and fed the findings into positioning."),
    ("Pleo", "2017 → 2022", "Business development → Partnerships → Field marketing → Product marketing",
     "Four roles as the company grew from ~20 to ~1,000 people. Danish marketing and PR, the first sales development team, and the UK relaunch of Pleo Invoices."),
    ("Cykelven Privat", "2015 → 2017", "Managing director",
     "Mobile bike workshops that employed and trained young people from vulnerable backgrounds. Ran daily operations and sales to companies."),
]


def img(name, alt, p, lazy=True):
    w, h = Image.open(os.path.join(ROOT, "assets", "img", name + ".webp")).size
    return (f'<img src="{p}assets/img/{name}.webp" alt="{e(alt)}" width="{w}" height="{h}"'
            + (' loading="lazy"' if lazy else "") + ">")


def strip(shots, p, numbered=False):
    figs = []
    for i, (cap, name) in enumerate(shots):
        label = f"{i + 1} → {cap}" if numbered else cap
        figs.append(
            f'<figure class="shot"><figcaption>{e(label)}</figcaption>'
            f'<button type="button" data-caption="{e(cap)}" aria-label="Enlarge: {e(cap)}">'
            f'{img(name, cap + " (screenshot)", p)}</button></figure>')
    return (f'<div class="strip-wrap"><div class="strip">{"".join(figs)}</div>'
            f'<div class="strip-foot"><span class="label">{len(shots)} pieces · click one to enlarge</span>'
            '<div class="arrows"><button type="button" data-dir="-1" aria-label="Previous screenshots">←</button>'
            '<button type="button" data-dir="1" aria-label="Next screenshots">→</button></div></div></div>')


def page(slug, title, desc, body):
    p = "" if slug == "work" else "../"
    nav = [("work", "Work", p or "./"), ("approach", "Approach", p + "approach/"), ("about", "About", p + "about/")]
    links = "".join(f'<a href="{h}"' + (' aria-current="page"' if s == slug else "") + f">{l}</a>" for s, l, h in nav)
    foot = "".join(f'<a href="{h}">{l}</a>' for _, l, h in nav)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mona+Sans:ital,wght@0,200..900;1,200..900&amp;family=Schibsted+Grotesk:wght@400..700&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">
<link rel="stylesheet" href="{p}assets/styles.css">
</head>
<body>
<header class="site-header">
<a class="brand" href="{p or './'}"><span class="brand-name">Mads Jersin</span><span class="label">Product marketing</span></a>
<nav class="nav" aria-label="Main">{links}</nav>
<div class="header-links">
<a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a>
<a href="{CV}" target="_blank" rel="noopener">CV ↗</a>
<a class="cta" href="mailto:{EMAIL}">Get in touch</a>
</div>
</header>
<main class="wrap">
{body}
<section class="contact" aria-label="Contact">
<h2>Let’s talk about your next launch.</h2>
<div class="contact-links">
<a href="mailto:{EMAIL}">{EMAIL} <span aria-hidden="true">→</span></a>
<a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn <span aria-hidden="true">↗</span></a>
<a href="{CV}" target="_blank" rel="noopener">CV <span aria-hidden="true">↗</span></a>
</div>
</section>
<footer class="site-footer">
<div class="footer-cols">
<div><span class="label">Main</span>{foot}</div>
<div><span class="label">Contact</span><a href="mailto:{EMAIL}">Email →</a><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a><a href="{CV}" target="_blank" rel="noopener">CV ↗</a></div>
</div>
<div class="footer-base">
<div><p>© 2026 Mads Jersin</p><p>Made with love (and Claude) in Copenhagen &lt;3</p></div>
<span class="label">Copenhagen · Updated Nov 2026</span>
</div>
</footer>
</main>
<dialog class="lightbox" id="lightbox" aria-label="Enlarged screenshot">
<figure><img alt=""><figcaption><span data-caption></span><button type="button">Close</button></figcaption></figure>
</dialog>
<script src="{p}assets/site.js"></script>
</body>
</html>
"""


def work():
    p = ""
    stats = "".join(f'<div class="stat"><span class="stat-num">{e(n)}</span><span class="label">{e(c)}</span></div>' for n, c in STATS)
    cards = []
    for i, (bid, eyebrow, title, sub, note, cover, numbered, shots) in enumerate(BOARDS):
        cards.append(f"""<details class="card" id="{bid}">
<summary>
<div class="card-text"><span class="label">{i + 1:02d} · {e(eyebrow)}</span><h3>{e(title)}</h3><p>{e(sub)}</p></div>
<div class="thumb">{img(cover, "", p)}</div>
<span class="plus" aria-hidden="true"><span>+</span></span>
</summary>
<div class="card-body"><p class="note">{e(note)}</p>{strip(shots, p, numbered)}</div>
</details>""")
    body = f"""<section class="hero">
<span class="label">Open to senior roles · Copenhagen</span>
<h1>Mads Jersin</h1>
<p class="lede">I turn products into stories people understand, care about and act on.</p>
<p class="intro">Product marketer with 9+ years in B2B SaaS and scale-ups: Pleo, Veo and Reshape Biotech. I work from customer insight to launch and follow-up, and I measure the effect.</p>
</section>
<section class="shorthand" aria-label="The shorthand">
<span class="label">The shorthand</span>
<div class="stats">{stats}</div>
</section>
<section class="section ruled" id="work">
<div class="section-head">
<h2>What the work looks like</h2>
<p>Real screenshots from shipped work at Reshape Biotech, grouped by what it took. Open a card and flick through the pieces. Internal documents and names are blurred. The stories behind the work, including my years at Pleo, are under <a href="approach/">Approach</a>.</p>
</div>
<div class="cards">{"".join(cards)}</div>
</section>"""
    return page("work", "Mads Jersin · Product marketing portfolio",
                "Product marketer in Copenhagen with 9+ years in B2B SaaS: Pleo, Veo and Reshape Biotech. Positioning, launches, onboarding and creative production.", body)


def approach():
    p = "../"
    cards = []
    for i, c in enumerate(CASES):
        results = "".join(f"<li><span>{e(r)}</span></li>" for r in c["results"])
        extra = ""
        if c.get("shots"):
            extra = strip(c["shots"], p)
        if c.get("link"):
            label, href = c["link"]
            extra = f'<a class="more" href="{p}{href}">{e(label)} <span aria-hidden="true">→</span></a>'
        cards.append(f"""<details class="card" id="{c['id']}">
<summary>
<div class="card-text"><span class="label">{i + 1:02d} · {e(c['eyebrow'])}</span><h3>{e(c['title'])}</h3><p>{e(c['sub'])}</p></div>
<div class="result"><span class="label">Result</span><ul>{results}</ul></div>
<span class="plus" aria-hidden="true"><span>+</span></span>
</summary>
<div class="card-body">
<dl class="story">
<div><dt>Why</dt><dd>{e(c['why'])}</dd></div>
<div><dt>How</dt><dd>{e(c['how'])}</dd></div>
<div><dt>The bump</dt><dd>{e(c['bump'])}</dd></div>
</dl>
<p class="tags">{e(c['tags'])}</p>
{extra}
</div>
</details>""")
    body = f"""<section class="section first">
<div class="section-head">
<h1>How I approach a problem</h1>
<p>Five projects. The result first; open a card for why it mattered, what we did and the bump along the way.</p>
</div>
<div class="cards">{"".join(cards)}</div>
</section>"""
    return page("approach", "How I approach a problem · Mads Jersin",
                "Five product marketing projects from Reshape Biotech and Pleo: why they mattered, what we did, what went wrong and the result.", body)


def about():
    p = "../"
    roles = "".join(
        f'<div class="role"><div class="role-co"><strong>{e(co)}</strong><span class="label">{e(when)}</span></div>'
        f'<div class="role-what"><strong>{e(title)}</strong><span>{e(note)}</span></div></div>'
        for co, when, title, note in ROLES)
    body = f"""<section class="section first">
<div class="about-top">
<div class="about-text">
<h1>About me</h1>
<p>I’ve worked in B2B SaaS start-ups and scale-ups since 2017, and twice I was the first product marketing hire. My favourite place is between thinking and making: finding the story in a product, then writing the website, scripting the video and training the team that sells it, together with the people who build it.</p>
<p>Next, I’m looking for a senior role in Copenhagen where positioning, campaigns and close collaboration with the people the work is for sit at the centre.</p>
</div>
<div class="portrait">{img("mads-portrait", "Portrait of Mads Jersin", p, lazy=False)}</div>
</div>
<div class="roles">{roles}</div>
<div class="facts">
<div class="fact"><span class="label">Education</span><span>MSc Finance and Strategic Management, CBS · 2011 → 2014</span><span>BSc Business Administration, CBS · 2008 → 2011</span><span>Product Marketing Minidegree, CXL · 2023</span></div>
<div class="fact"><span class="label">Toolbox</span><span>Positioning | Launches | Sales enablement | Onboarding | Video scripts | Landing pages | PR | HubSpot | Intercom | Figma | Lovable | Claude</span></div>
</div>
</section>"""
    return page("about", "About · Mads Jersin",
                "About Mads Jersin: product marketer in Copenhagen, twice the first product marketing hire, with roles at Reshape Biotech, Veo and Pleo.", body)


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", path)


if __name__ == "__main__":
    write("index.html", work())
    write("approach/index.html", approach())
    write("about/index.html", about())
