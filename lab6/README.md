# Lab 6 — HTML Forms & Django Form Handling

## Overview
This lab covers building an HTML form and handling its submission in Django: a search form (keyword + title/author checkboxes) that POSTs to the same view, filters an in-memory book list, and displays the matching results.

## What was implemented
- Task 1 — `/books/search` view and `search.html` template (extends `base.html`) with a POST form: keyword text input, title/author checkboxes, CSRF token
- Task 2 — `search(request)` handles the POST: reads `keyword`, `option1` (title), `option2` (author) from `request.POST`, filters `__getBooksList()` accordingly, and renders `bookList.html` with the matching books

## URLs to test
- `/books/search` — shows the form (GET)
- `/books/search` — submit the form (POST) to see filtered results
