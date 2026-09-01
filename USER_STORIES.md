# Portfolio Website — User Stories

Project: Django portfolio site (About Me, Experience, Projects, Contact)
Author: Lyn Smith · SDGKU Full-Stack Development Immersive, Cohort 67

---

## Story 1 — Evaluating the candidate

🧾 **User Story:**
As a hiring manager reviewing applicants, I want to see a summary of Lyn's background, skills, and certifications the moment I land on the site, so that I can quickly decide whether he's a fit before reading a resume or scheduling a call.

✅ **Acceptance Criteria (Gherkin):**
Given I am a visitor who has never seen the site before
When I navigate to the root URL "/"
Then I see the About Me page with a professional summary, skills, certifications, career stats, a photo, and working contact links (email, LinkedIn, contact page) — readable on desktop and phone

- [x] Acceptance criteria validated

🏷️ **Labels:**
Feature: About page · Estimation: 3 pts · Priority: High · Sprint-ready

✍️ **Note:**
Acceptance criteria based on Gherkin syntax by Dan North (BDD).

**Tasks checklist:**

- [x] Design the bento-grid About layout (Dossier theme)
- [x] Build `templates/pages/about_me.html` extending `base.html`
- [x] Move page styles into `static/css/about.css` via the `extra_head` block
- [x] Add profile photo to `static/img/` and wire it into the page
- [x] Write summary, skills, certifications, and stats content from resume/LinkedIn
- [x] Add contact actions (mailto, LinkedIn, contact page link)
- [x] Verify responsive breakpoints (desktop / tablet / phone)

---

## Story 2 — Verifying the work

🧾 **User Story:**
As a visitor considering Lyn for a role or collaboration, I want to browse his projects with real screenshots, tech tags, and source-code links, so that I can see actual work and verify his skills for myself.

✅ **Acceptance Criteria (Gherkin):**
Given the database contains projects with a title, year, description, screenshot, repository URL, and skills
When I navigate to "/projects/"
Then I see one card per project (newest year first, newest featured), each showing its screenshot in a browser-style frame that pans on hover, its title, year, description, and skill tags, and a "View Repository" link that opens GitHub in a new tab — with a clean placeholder when a project has no image

- [x] Acceptance criteria validated

🏷️ **Labels:**
Feature: Projects showcase · Estimation: 5 pts · Priority: High · Sprint-ready

✍️ **Note:**
Acceptance criteria based on Gherkin syntax by Dan North (BDD).

**Tasks checklist:**

- [x] Create `Project` and `Skill` models with a many-to-many relationship
- [x] Run migrations and configure `MEDIA_URL` / `MEDIA_ROOT` for uploads
- [x] Build `projects_view` returning projects ordered by year (newest first)
- [x] Build the Case Files template with featured card + grid
- [x] Add the browser-frame screenshot window with hover-pan CSS (reduced-motion safe)
- [x] Capture and compress real screenshots of all five project sites
- [x] Handle missing-image placeholder and empty-state message
- [x] Link each card to its GitHub repository

---

## Story 3 — Maintaining the site

🧾 **User Story:**
As the site owner, I want to add or update projects through the Django admin, so that the Projects page always reflects my latest work without editing HTML or redeploying code.

✅ **Acceptance Criteria (Gherkin):**
Given I am logged in to the Django admin as the site owner
When I create or edit a Project — title, year, description, repository URL, uploaded screenshot, and skills — and save it
Then the change appears on the public "/projects/" page automatically, with the screenshot stored under `media/projects/` and existing skills reusable across projects without duplicates

- [x] Acceptance criteria validated

🏷️ **Labels:**
Feature: Project management (admin) · Estimation: 2 pts · Priority: Medium · Sprint-ready

✍️ **Note:**
Acceptance criteria based on Gherkin syntax by Dan North (BDD).

**Tasks checklist:**

- [x] Register `Project` and `Skill` in `portfolio/admin.py`
- [x] Verify image uploads land in `media/projects/` and render on the page
- [x] Verify skills are reusable across projects (many-to-many)
- [x] Confirm new projects appear on the public page with no code changes
- [ ] Stretch: auto-resize/compress screenshots in `Project.save()` so large uploads can't slow the page
