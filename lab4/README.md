\# Lab 4 — HTML, CSS \& Django Template Tags



\## Overview

This lab focuses on building a consistent site layout using HTML, CSS, and Django's template inheritance system.



\## What was implemented

\- Created a shared base template (`base.html`) with a common header and footer, reused across all pages via `{% include %}`.

\- Built pages that extend the base template using `{% extends %}` and `{% block %}`.

\- Added a `static/` directory containing `styles.css` and book cover images.

\- Linked static assets through the `{% static %}` template tag.

\- Implemented the `list\_books` page, displaying books with their cover images and links to their detail pages.

