"""One-shot fix: point every project at its compressed screenshot.

Why this file exists: the database (db.sqlite3) can't be safely edited from
outside while OneDrive is syncing it and the dev server is using it — so this
script makes the change through Django itself, on your machine.

How to run it — from the project folder (same place you run manage.py),
with your virtual environment active:

    python fix_project_images.py

It prints what it changes, and it's safe to run more than once.
Feel free to delete this file (or move it to archive/) afterwards.
"""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from portfolio.models import Project  # noqa: E402

NEW_IMAGES = {
    # title: compressed screenshot already in media/projects/
    "Temperature": "projects/temperature_site.webp",        # full-page shot of the live site (24 KB)
    "Pet Salon": "projects/pet_salon_home.webp",            # your light-mode home capture, compressed (120 KB)
    "Online Store": "projects/online_store_about.webp",     # your about-page capture, compressed (47 KB)
    "Vector Baseball": "projects/vector_baseball_site.webp",  # your capture, compressed (145 KB)
    "Manga n Matcha": "projects/manga_n_matcha_site.webp",    # your capture, compressed (38 KB)
}

for project in Project.objects.all():
    new = NEW_IMAGES.get(project.title)
    if not new:
        print(f"- {project.title}: no mapping, left as {project.image}")
        continue
    old = str(project.image)
    if old == new:
        print(f"= {project.title}: already {new}")
        continue
    project.image = new
    project.save(update_fields=["image"])
    print(f"+ {project.title}: {old} -> {new}")

print("Done. Hard-refresh the Projects page (Ctrl+F5).")
