# About page — archived drafts

The **"Dossier"** design (Option 6) was chosen and integrated into the live site on 2026-08-24:

```
templates/pages/about_me.html    the About Me page (Dossier bento markup)
static/css/about.css             the page's styles
static/css/style.css             site-wide theme (warm charcoal + amber, Newsreader/Inter/JetBrains Mono)
templates/base.html              loads the site fonts + has an {% block extra_head %} hook
static/img/headshot.png          profile photo used by the page
```

This folder holds the five draft options that were not chosen, plus the superseded
`about_me_dossier.html` (its content now lives in `about_me.html`) and the old options
README. Nothing in here is referenced by the Django project — it's outside the
`templates/` directory, so the template loader never sees it. Safe to keep for
reference or delete whenever.

To resurrect a draft: copy it back into `templates/pages/` and point
`pages/views.py` at it. Each draft is self-contained (its CSS is inline in the file).
