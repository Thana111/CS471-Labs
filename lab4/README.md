# Lab 4 — HTML, CSS & Django Template Tags

## Overview
This lab covers building a basic website with several HTML pages, styling with inline, internal and external CSS, and integrating everything into Django using the `{% static %}`, `{% url %}`, `{% extends %}`, `{% block %}` and `{% include %}` template tags. A shared layout (`base.html`) with a common header and footer was created so every page inherits the same navigation bar and styling.

## What was implemented
- Task 4 — Created `apps/static/` and configured `STATIC_URL` / `STATICFILES_DIRS` in `settings.py`; moved `styles.css` and the book/icon images into it; added `list_books` and `aboutus` views and routes, and moved all HTML files into `apps/templates/bookmodule/`, updating links/images/static references with `{% static %}` and `{% url %}` tags
- Task 5 — Built a shared layout: `layouts/base.html` plus `includes/header.html` and `includes/footer.html`, and converted every page (`index.html`, `aboutus.html`, `list_books.html`, `show.html`) to `{% extends "layouts/base.html" %}` with `{% block content %}`

## URLs to test
- `/books/` — styled home page with shared nav bar
- `/books/list_books/` — book covers loaded from `apps/static/`
- `/books/aboutus/` — about page
- `/books/123` and `/books/456` — one-book detail page, now using the shared layout
