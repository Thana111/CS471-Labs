\# Lab 6 — HTML Forms \& Form Handling in Django



\## Overview

This lab covers building an HTML form and processing submitted form data on the server side.



\## What was implemented

\- `search.html` — a search form with a keyword field and two checkboxes (Title / Author).

\- A `search` view in `views.py` that handles both GET requests (displaying the empty form) and POST requests (processing the submission).

\- A helper function `\_\_getBooksList()` returning a static list of book records.

\- Filtering logic that searches by title and/or author depending on which checkboxes are selected.

\- `bookList.html` — displays the filtered search results.

\- Route: `/books/search`


