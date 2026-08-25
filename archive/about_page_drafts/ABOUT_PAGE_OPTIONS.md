# About Me — Bento Page Options

Six ready-to-use About Me pages for your Django portfolio, all bento-grid layouts
populated with real content from your resumes and LinkedIn.

## Round 1 — three distinct directions

```
templates/pages/about_me_signal.html     Option 1 — "Signal"   (dark tactical / terminal)
templates/pages/about_me_gradient.html   Option 2 — "Gradient" (bold gradients / glass cards)
templates/pages/about_me_clean.html      Option 3 — "Clean Pro" (refined, matches your current site)
```

## Round 2 — remixes of the favorite components

Built from the cards you flagged: terminal, mission brief, field-proven, quote (opt 1);
superpowers, receipts, let's-build-something (opt 2); current post, what-I-work-with,
stats (opt 3). All three use a clean dark palette in the spirit of Clean Pro, with variations:

```
templates/pages/about_me_console.html    Option 4 — "Console"  (blue slate — same palette family
                                         as your site; name + terminal share the hero row)
templates/pages/about_me_circuit.html    Option 5 — "Circuit"  (teal on graphite, Space Grotesk
                                         headings, chip labels, stats as individual mini-cards)
templates/pages/about_me_dossier.html    Option 6 — "Dossier"  (warm charcoal + amber, editorial
                                         serif headline with drop cap, FILE-numbered sections)
```

Shared assets:

```
static/img/headshot.png                  Your profile photo (circular crop, transparent background)
templates/base.html                      UPDATED in round 1 — see below
```

Your original `templates/pages/about_me.html` was left untouched.

## Changes made to base.html (round 1)

1. Added `{% block extra_head %}{% endblock extra_head %}` just before `</head>`.
   Each option injects its own fonts + CSS through this block, so pages can style
   themselves without touching `static/css/style.css`.
2. The footer LinkedIn icon now points to your actual profile
   (`linkedin.com/in/lyn-smith-b5911417a`) instead of linkedin.com.
3. The footer GitHub icon still points to `https://github.com/` — swap in your username
   when you're ready.

## How to try each option

In `pages/views.py`, point the about view at the option you want to see:

```python
def about_me_view(request):
    return render(request, 'pages/about_me_console.html')   # or _signal / _gradient /
                                                            # _clean / _circuit / _dossier
```

Run the server (`python manage.py runserver`) and refresh the home page. When you've
picked a winner, either keep that view pointing at it, or copy that file's contents into
`templates/pages/about_me.html` and delete the rest.

## Notes

- Each template is self-contained: markup + CSS live in one file, and fonts load from
  Google Fonts with system fallbacks (Option 4: Inter + JetBrains Mono · Option 5:
  Space Grotesk + Inter + JetBrains Mono · Option 6: Newsreader + Inter + JetBrains Mono).
- All options are responsive (12-col bento on desktop, 2-col on tablet, single column on
  phones) and respect `prefers-reduced-motion`.
- The headshot was captured from your LinkedIn profile at screen resolution. If you have
  the original photo, drop it in as `static/img/headshot.png` (square crop) and every
  option picks it up automatically.
- Content sources: your master resumes (Documents/Resumes) + your LinkedIn headline,
  About section, and posts. Stats used: 16+ years, 215+ reports, 500+ instruction hours,
  135+ Marines trained, 5 personal awards, TS//SCI. If any of those need adjusting,
  they're plain text in each template — search for the number.
