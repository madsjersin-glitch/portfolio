# Mads Jersin · Portfolio

A static site with three pages: Work (`/`), Approach (`/approach/`) and About (`/about/`).
No build step is needed to host it; Vercel serves the files as they are.

## Editing

All text lives in `build.py`. Change it there, then run:

    python3 build.py

That rewrites `index.html`, `approach/index.html` and `about/index.html`.
Styles are in `assets/styles.css`, behaviour in `assets/site.js`, images in `assets/img/`.

Screenshots of internal documents are blurred on purpose. Blur any new ones before adding them.
