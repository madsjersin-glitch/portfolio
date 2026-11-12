#!/usr/bin/env python3
"""Builds the three pages (Work, Case studies, About) from the content below.

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
    ("9+", "years in B2B SaaS"),
    ("2×", "first product marketing hire"),
    ("20+", "launches led at Reshape, all tiers"),
    ("~$0.5M", "pipeline from one launch’s attendees"),
]

FEATURED = dict(
    href="case-studies/#robot", image="robot-event", alt="Two hosts presenting Reshape’s live online launch event",
    eyebrow="Reshape Biotech · Product launch", title="Launching the robot",
    text="I led product marketing for Reshape’s launch into quality-control labs: the message, sales training, website, videos, a live launch event and four email campaigns.",
    result="In the weeks after the launch, companies that attended the event accounted for ~$0.5M in new pipeline.",
)

# Work cards. Each shot: (caption, image, what to notice)
BOARDS = [
    dict(id="positioning", eyebrow="Reshape Biotech · Positioning and messaging", title="Positioning & messaging",
         sub="I rewrote Reshape’s website messaging to focus on what the product changes for the people in the lab, the people managing it and the business.",
         note="The old and new homepage, and the shift behind them. The full positioning, messaging and audience documents are internal, so the core of them is written out here instead.",
         excerpt=[("Before", "“Automate your visual experiments.” Feature-led and inside-out: it told people what the hardware did, because that was what we knew best."),
                  ("After", "Value-led, for three audiences. Scientists run more experiments, more accurately, in less time. Lab managers get standardised processes and data they can trust, with every image and data point kept to revisit later. The business does more with the same team, because the hardware and AI record the results that highly trained staff used to count by hand every few hours.")],
         cover="pos-new-website",
         shots=[("Old homepage", "pos-old-website", "Led with automating visual experiments and the hardware itself."),
                ("New homepage", "pos-new-website", "Leads with what changes for the lab: more experiments, accurate data and time saved.")],
         link=("Read the launch case study", "case-studies/#robot")),
    dict(id="launches", eyebrow="Reshape Biotech · Feature launch", title="Product launches",
         sub="I led product marketing for 20+ launches at Reshape, from small updates to the biggest releases.",
         note="One example: Experiments, a feature that takes scientists from hypothesis to conclusion in one place, from plate design through imaging and analysis. These are the places a user met it, from the first tooltip to the help article.",
         cover="exp-feature-tour",
         shots=[("In-app tooltip", "exp-tooltips", "Points existing users to the new feature where they already work."),
                ("Empty state", "exp-empty-state", "Explains what Experiments does before there is anything in it."),
                ("Feature-tour screenshot", "exp-feature-tour", "A step from the clickable tour through plate design."),
                ("Launch email", "exp-launch-email", "The announcement to customers, leading with what changes for them."),
                ("Help article", "exp-kb-plate-templates", "A step-by-step guide with an embedded video.")]),
    dict(id="onboarding", eyebrow="Reshape Biotech · User onboarding", title="User onboarding",
         sub="I built a five-email onboarding programme with help articles and video guides for newly invited users.",
         note="Each email links to a help article with a video guide, so people can read or watch their way into the product.",
         cover="onb-email",
         shots=[("Onboarding email", "onb-email", "The first of five emails, with a short way in and a video thumbnail."),
                ("Video guides", "onb-videos", "The Reshape 101 series: one short video per step."),
                ("Help article", "onb-article-job", "Starting a new job, the second step in the programme.")],
         link=("Read the onboarding case study", "case-studies/#onboarding-story")),
    dict(id="creative", eyebrow="Reshape Biotech · Campaign video", title="Creative production", numbered=True,
         sub="I wrote scripts and created mood boards for five campaign videos, working with a videographer and our designers.",
         note="How one of them came together, from script to finished film.",
         cover="cre-final",
         shots=[("Script", "cre-script", "Scene by scene, with the spoken lines and the shots to film."),
                ("Mood board", "cre-moodboard", "The look and references agreed with the videographer."),
                ("Design collaboration", "cre-design", "Matching on-screen software to what happens at the lab bench."),
                ("Frame from the final film", "cre-final", "End-to-end workflows, the finished campaign video.")]),
    dict(id="sales", eyebrow="Reshape Biotech · Sales enablement", title="Sales enablement",
         sub="I built a sales resources hub with decks, one-pagers and product guides, used by everyone in the commercial teams, around 15 people.",
         note="A few of the pieces: slides from the quality-control sales deck, product guides and one-pagers.",
         cover="sal-slide-modernizing",
         shots=[("Sales deck: title slide", "sal-slide-modernizing", "Opens on the customer’s goal: modernising microbiology quality control."),
                ("Sales deck: standardisation", "sal-slide-standardize", "One analysis standard across a company, the core value for QC buyers."),
                ("Sales deck: global sites", "sal-slide-global", "For customers with labs in several countries."),
                ("Product guides", "sal-guides", "Printable guides for research and development (R&D) and QC customers."),
                ("One-pagers", "sal-onepagers", "Short leave-behinds for different use cases.")]),
]

CASES = [
    dict(id="robot", eyebrow="Reshape Biotech · Product launch", title="Launching the robot",
         sub="I led product marketing for Reshape’s launch into quality-control labs.",
         facts=[("My role", "Launch positioning, communications and sales preparation"),
                ("With", "The hardware and software teams, a co-founder, a freelance videographer and our designer"),
                ("Timeline", "About three months from first preparation to the launch campaign")],
         results=["100+ attendees from biotech companies worldwide at the launch event",
                  "In the weeks after the launch, companies that attended accounted for ~$0.5M in new pipeline"],
         why="Reshape’s imaging technology could serve quality control (QC), but QC buyers worry about different things than our existing customers. The product team built a robot for QC labs, the High-throughput Imaging Device, and I led launch positioning, communications and sales preparation.",
         how="I moved the message from data harmonisation to what QC cares about: time saved, accurate data and a clear trail of every test when an auditor asks. I trained sales together with a co-founder, rewrote the website and made the launch videos with a videographer and our designer. We ran a 45-minute online launch event and four email campaigns.",
         call="I split the follow-up by how warm each audience was. Cold leads got a longer sequence that built trust, with our ISO certifications and examples of how the hardware is used. Warmer leads got a short sequence that went straight to the launch video and the website.",
         bump="Software was built after the hardware, but the videos and sales training needed a working product. Together with our designer I built clickable mockups showing how software and robot would work together, so the launch date didn’t have to wait.",
         shots=[("Live launch event", "robot-event", "The 45-minute online event, half live and half pre-recorded."),
                ("Frame from the launch video", "robot-video", "The launch film, also cut into ads."),
                ("Landing page", "robot-landing", "The new product page, written around QC’s concerns."),
                ("Sales training slide", "robot-training", "From the session that prepared the sales team: what changed and what to say.")]),
    dict(id="onboarding-story", eyebrow="Reshape Biotech · User onboarding", title="Onboarding every new user, not just the admins",
         sub="I built a five-email programme that starts within 30 minutes of an accepted invitation and runs for 30 days.",
         facts=[("My role", "Built and ran the programme: copy, flow, videos and help articles"),
                ("With", "A marketing data engineer, a customer success manager and the product team"),
                ("Timeline", "About a week to build; 30 days for each new user")],
         results=["200–250 new users received the emails", "~80% average open rate across the five emails",
                  "~35% clicked through from the first email"],
         why="Administrators told me that the colleagues they invited landed in the product without knowing how to use it. Admins got a hands-on onboarding from customer success; everyone else got an invitation and silence.",
         how="Each email follows the work a new user actually does: a platform overview, starting a job, analysing the data, validating results and trying other experiments. Each links to a help article with a video guide. I wrote the copy, built the flow in Intercom, scripted and edited the videos and wrote the articles. A customer success manager presented the videos.",
         call="I left out the administrators. They already had a personal onboarding with customer success, and a second, automated one would only have got in the way.",
         bump="The first email arrived far too late, because product data synced only once a day. I worked with a marketing data engineer to run the sync every 30 minutes, so the first email now arrives within half an hour.",
         link=("See the onboarding screens", "#onboarding")),
    dict(id="invoices", eyebrow="Pleo · Product relaunch", title="Letting customers name the product",
         sub="I led product marketing for relaunching Pleo Bills as Pleo Invoices in the UK, through bookkeeping partners.",
         facts=[("My role", "Positioning, messaging and the go-to-market through partners"),
                ("With", "Partner marketing, the brand team, two product teams and the head of bookkeeping partnerships"),
                ("Timeline", "Partners came on board over about six months")],
         results=["200 bookkeeping partners signed up and onboarded at least one client within about six months",
                  "#2 Product of the Day on Product Hunt"],
         why="Pleo wanted to cover all company spend, not just card expenses, and invoices are a big share of it. A first UK attempt had run for about a year without traction.",
         how="In around 20 customer conversations, people kept clarifying that by “bills” they meant invoices. So we renamed the product, and the rename became the hook. I built an enablement portal for partners, directed a campaign video made by a motion designer, wrote the website copy and ran targeted emails and a Product Hunt launch.",
         call="We took it to market through bookkeeping partners rather than straight to companies. Partners wanted to gather their clients’ finances in fewer tools, the main UK competitor had become more expensive, and Pleo already had traction with its card.",
         bump="Everyone involved had competing priorities. Instead of asking for “more time”, I secured two weeks of a motion designer’s time and a dedicated launch budget."),
    dict(id="pr", eyebrow="Pleo · Press relations", title="Making funding news worth a second story",
         sub="I pitched Danish media stories about the CEO’s case for attracting international talent to Denmark.",
         facts=[("My role", "All Danish media contact around the funding rounds"),
                ("With", "The CEO and the head of brand"),
                ("Timeline", "Series A, B, C and a C extension")],
         results=["National TV and front pages of Børsen and Finans",
                  "Roughly 3–4× the job applications compared with before the coverage (my estimate)"],
         why="Funding rounds put Pleo in the spotlight and brought in applicants, but “start-up raises money” gets old fast for journalists.",
         how="I wrote the press releases, gave each outlet its own angle and prepared the CEO with figures on the Danish labour market. The talent theme was the CEO’s; I kept pitching it through the Series B and the Danish election campaign.",
         call="I gave the funding news a political angle. The size of a round interests the business press once; Denmark’s shortage of tech talent gave TV and the papers a reason to come back.",
         bump="I learned the hard way not to pitch the same story to every outlet. From then on, each got its own angle or an exclusive, which also helped on busy news days."),
    dict(id="housing", eyebrow="Pleo · Targeted campaign", title="A campaign for ~300 supported housing facilities",
         sub="A small, well-defined audience, reached through their own national organisation.",
         facts=[("My role", "Overall responsibility for the campaign"),
                ("With", "Our designer, the paid media team and sales"),
                ("Timeline", "Two months")],
         results=["~30–40 sales meetings booked with supported housing facilities during the two-month campaign"],
         why="Customer conversations kept showing the same thing: staff paid for residents’ shopping from a shared cash box, and bookkeepers struggled to track the spending.",
         how="I mapped the ~300 facilities in Denmark into one list. We reached them with display ads on sites care staff read, print ads with a QR code and paid campaigns, all pointing to one landing page with a first-year discount.",
         call="Instead of buying broad reach, I went to the sector’s own national organisation and placed the offer in its newsletter and members’ magazine.",
         bump="The print and display partners couldn’t measure much. I matched tracked links and QR codes against booked meetings to compare how each channel performed."),
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
    for i, (cap, name, desc) in enumerate(shots):
        label = f"{i + 1} → {cap}" if numbered else cap
        w, h = Image.open(os.path.join(ROOT, "assets", "img", name + ".webp")).size
        figs.append(
            f'<figure class="shot" style="--r: {w / h:.4f}"><figcaption>{e(label)}</figcaption>'
            f'<button type="button" data-caption="{e(cap)}" data-desc="{e(desc)}" aria-label="Enlarge: {e(cap)}">'
            f'{img(name, cap + ". " + desc, p)}</button><p class="shot-desc">{e(desc)}</p></figure>')
    return (f'<div class="strip-wrap"><div class="strip">{"".join(figs)}</div>'
            f'<div class="strip-foot"><span class="count" aria-live="polite">1 of {len(shots)}</span>'
            '<div class="arrows"><button type="button" data-dir="-1" aria-label="Previous image">←</button>'
            '<button type="button" data-dir="1" aria-label="Next image">→</button></div></div></div>')


def page(slug, title, desc, body):
    p = "" if slug == "work" else "../"
    nav = [("work", "Work", p or "./"), ("cases", "Case studies", p + "case-studies/"), ("about", "About", p + "about/")]
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
<div class="lang" role="group" aria-label="Language"><span class="lang-on" aria-current="true">EN</span><span class="lang-off" aria-disabled="true">DA <span class="soon">Coming</span></span></div>
<a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a>
<a href="{CV}" target="_blank" rel="noopener">CV ↗</a>
<a class="cta" href="mailto:{EMAIL}">Get in touch</a>
</div>
</header>
<main class="wrap">
{body}
<section class="contact" aria-label="Contact">
<h2>I’m looking for my next product marketing role.</h2>
<div class="contact-links">
<a href="mailto:{EMAIL}">Email me <span aria-hidden="true">→</span></a>
<a href="{CV}" target="_blank" rel="noopener">View my CV <span aria-hidden="true">↗</span></a>
<a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn <span aria-hidden="true">↗</span></a>
</div>
</section>
<footer class="site-footer">
<div class="footer-cols">
<div><span class="label">Main</span>{foot}</div>
<div><span class="label">Contact</span><a href="mailto:{EMAIL}">Email →</a><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a><a href="{CV}" target="_blank" rel="noopener">CV ↗</a></div>
<div><span class="label">Language</span><div class="lang" role="group" aria-label="Language"><span class="lang-on" aria-current="true">EN</span><span class="lang-off" aria-disabled="true">DA <span class="soon">Coming</span></span></div></div>
</div>
<div class="footer-base">
<div><p>© 2026 Mads Jersin</p><p>Made with love (and Claude) in Copenhagen &lt;3</p></div>
<span class="label">Copenhagen · Updated November 2026</span>
</div>
</footer>
</main>
<dialog class="lightbox" id="lightbox" aria-label="Enlarged image">
<figure>
<img alt="">
<figcaption>
<div class="lb-text"><strong data-caption></strong><span data-desc></span></div>
<div class="lb-controls"><span class="lb-count" data-count></span><button type="button" data-step="-1" aria-label="Previous image">←</button><button type="button" data-step="1" aria-label="Next image">→</button><button type="button" data-close>Close</button></div>
</figcaption>
</figure>
</dialog>
<script src="{p}assets/site.js"></script>
</body>
</html>
"""


def card(cid, eyebrow, title, sub, side, body, level):
    return f"""<details class="card" id="{cid}">
<summary>
<div class="card-text"><span class="label">{e(eyebrow)}</span><h{level}>{e(title)}</h{level}><p>{e(sub)}</p></div>
{side}
<span class="plus" aria-hidden="true"><span>+</span></span>
</summary>
<div class="card-body">{body}</div>
</details>"""


def work():
    p = ""
    stats = "".join(f'<li><strong>{e(n)}</strong> {e(c)}</li>' for n, c in STATS)
    f = FEATURED
    cards = []
    for b in BOARDS:
        body = f'<p class="note">{e(b["note"])}</p>'
        if b.get("excerpt"):
            rows = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in b["excerpt"])
            body += f'<div class="excerpt"><span class="label">The shift, in short</span><dl>{rows}</dl></div>'
        body += strip(b["shots"], p, b.get("numbered", False))
        if b.get("link"):
            label, href = b["link"]
            body += f'<a class="more" href="{href}">{e(label)} <span aria-hidden="true">→</span></a>'
        cards.append(card(b["id"], b["eyebrow"], b["title"], b["sub"], f'<div class="thumb">{img(b["cover"], "", p)}</div>', body, 3))
    body = f"""<section class="hero">
<span class="label">Open to senior roles · Copenhagen</span>
<h1>I’m a product marketer who turns customer insight into positioning, launches and onboarding.</h1>
<p class="intro">I’ve spent 9+ years at Pleo, Veo and Reshape Biotech, including two roles as the first product marketing hire. I’m looking for a senior product marketing role in Copenhagen.</p>
<ul class="stats" aria-label="The shorthand">{stats}</ul>
</section>
<section class="featured" aria-labelledby="featured-title">
<a class="featured-img" href="{f['href']}" tabindex="-1" aria-hidden="true">{img(f['image'], f['alt'], p, lazy=False)}</a>
<div class="featured-text">
<span class="label">Featured case study · {e(f['eyebrow'])}</span>
<h2 id="featured-title"><a href="{f['href']}">{e(f['title'])}</a></h2>
<p>{e(f['text'])}</p>
<p class="featured-result">{e(f['result'])}</p>
<a class="more" href="{f['href']}">Read the case study <span aria-hidden="true">→</span></a>
</div>
</section>
<section class="section ruled" id="work">
<div class="section-head">
<h2>What the work looks like</h2>
<p>Examples of my positioning, launch, onboarding, creative and sales-enablement work at Reshape Biotech. Open a card to see the pieces, and click any image to enlarge it. My work at Pleo is told in the <a href="case-studies/">case studies</a>.</p>
</div>
<div class="cards">{"".join(cards)}</div>
</section>"""
    return page("work", "Mads Jersin · Product marketing portfolio",
                "Product marketer in Copenhagen with 9+ years in B2B SaaS: Pleo, Veo and Reshape Biotech. Positioning, launches, onboarding and creative production.", body)


def cases():
    p = "../"
    out = []
    for c in CASES:
        results = "".join(f"<li><span>{e(r)}</span></li>" for r in c["results"])
        facts = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in c["facts"])
        body = (f'<dl class="facts-line">{facts}</dl>'
                f'<dl class="story"><div><dt>Why</dt><dd>{e(c["why"])}</dd></div>'
                f'<div><dt>How</dt><dd>{e(c["how"])}</dd></div>'
                f'<div><dt>The call</dt><dd>{e(c["call"])}</dd></div>'
                f'<div><dt>The bump</dt><dd>{e(c["bump"])}</dd></div></dl>')
        if c.get("shots"):
            body += strip(c["shots"], p)
        if c.get("link"):
            label, href = c["link"]
            body += f'<a class="more" href="{p}{href}">{e(label)} <span aria-hidden="true">→</span></a>'
        side = f'<div class="result"><span class="label">Result</span><ul>{results}</ul></div>'
        out.append(card(c["id"], c["eyebrow"], c["title"], c["sub"], side, body, 2))
    body = f"""<section class="section first">
<div class="section-head">
<h1>How I approach a problem</h1>
<p>Five case studies from Reshape Biotech and Pleo. The result comes first; open a case for why it mattered, what I did, the decision that shaped it and what went wrong along the way.</p>
</div>
<div class="cards">{"".join(out)}</div>
</section>"""
    return page("cases", "Case studies · Mads Jersin",
                "Five product marketing case studies from Reshape Biotech and Pleo: why they mattered, what I did, the key decision, what went wrong and the result.", body)


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
<div class="fact"><span class="label">Skills</span><span>Positioning · Launches · Sales enablement · Onboarding · Video scripts · Landing pages · Press relations</span></div>
<div class="fact"><span class="label">Tools</span><span>HubSpot · Intercom · Webflow · Notion · Figma · Lovable · Claude</span></div>
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
    write("case-studies/index.html", cases())
    write("about/index.html", about())
    # The page used to live at /approach/; send old links on.
    write("approach/index.html", '<!doctype html><meta charset="utf-8"><title>Case studies · Mads Jersin</title>'
          '<meta http-equiv="refresh" content="0; url=../case-studies/"><link rel="canonical" href="../case-studies/">'
          '<a href="../case-studies/">Case studies</a>')
