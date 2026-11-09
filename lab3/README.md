\# Lab 3 — Django URLs, Views \& Templates



\## Overview

This lab introduces URL routing, view functions, and template rendering in Django.



\## What was implemented

\- Created the first view functions (`index`, `index2`) in `views.py`.

\- Handled data passed via GET parameters (`?name=...`) and via URL path converters (`<int:val1>`).

\- Built the first HTML template (`index.html`), rendered through `render()` using the `{{ name }}` context variable.

\- Separated each app's routes into its own `urls.py` file (`bookmodule/urls.py`) and linked it to the main project via `include()`.

\- Implemented `viewbook`, a dynamic view that displays book details based on the book ID passed in the URL.


