# Mads Jersin · Portfolio

A static site with three pages: Work (`/`), Case studies (`/case-studies/`) and About (`/about/`).
No build step is needed to host it; Vercel serves the files as they are.

## Editing

All text lives in `build.py`. Change it there, then run:

    python3 build.py

That rewrites `index.html`, `case-studies/index.html` and `about/index.html`, plus a redirect from the old `approach/` address.
Styles are in `assets/styles.css`, behaviour in `assets/site.js`, images in `assets/img/`.

Only public or approved material goes in `assets/img/`: no internal documents, colleagues' names or faces. Describe internal work in text instead.
