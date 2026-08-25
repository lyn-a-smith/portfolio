# Projects page — archived drafts

The **"Case Files"** layout (Option A) was chosen and integrated into the live site on 2026-08-25:

```
templates/portfolio/projects.html    the Projects page (Case Files layout, loops the Project model)
static/css/projects.css              the page's styles
```

This folder holds:

- `projects_log.html` / `projects_studies.html` — the two draft layouts that weren't chosen
  (Operations Log rows and Case Studies spreads)
- `projects_files.html` — the chosen draft in its original self-contained form
  (its content now lives in projects.html + projects.css)
- `projects_wip_original.html` — your own earlier work-in-progress version of the page,
  saved before integration

Nothing here is referenced by Django — it's outside `templates/`, so the loader never
sees it. To try a different layout later: copy it into `templates/portfolio/`, point
`portfolio/views.py` at it, and pass the same `projects` context. Each draft is
self-contained (CSS inline in the file).
