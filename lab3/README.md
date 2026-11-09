# Lab 3 — Django URLs, Views & Templates

## Overview
This lab covers mapping URLs to view functions, passing parameters via GET requests and URL path parameters, creating a basic HTML template, rendering context variables, splitting URL configuration into a per-app `urls.py`, and building a dynamic book-detail view.

## What was implemented
- Task 1 & 2 — `index(request)` view returning `HttpResponse`, then updated to read a `name` GET parameter (`?name=...`) and render it
- Task 3 — `index2(request, val1=0)` view mapped to `index2/<int:val1>/`, returning `"value1 = <val1>"`
- Task 4 & 5 — Converted `index` to use `render()` with an HTML template (`bookmodule/index.html`) and a context dictionary (`{{ name }}`)
- Task 6 — Moved URL patterns into `apps/bookmodule/urls.py`, included under the `/books/` prefix from the project-level `libraryproject/urls.py`
- Task 7 — `viewbook(request, bookId)` view and `bookmodule/show.html` template to display a single book's ID, title, and author

## URLs to test
- `/books/` → "Hello, world!"
- `/books/?name=Thana` → "Hello, Thana"
- `/books/index2/3/` → "value1 = 3"
- `/books/123` and `/books/456` → book detail pages
