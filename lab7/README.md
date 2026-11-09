\# Lab 7 — Django Models (Part 1)



\## Overview

This lab introduces Django Models and the Django ORM for interacting with a relational database.



\## What was implemented

\- Defined a `Book` model in `models.py` with fields: `title`, `author`, `price`, and `edition`.

\- Generated and applied database migrations (`makemigrations`, `migrate`) to create the corresponding database table.

\- Inserted sample book records through the Django shell.

\- `simple\_query` — a basic ORM query using `filter()` to find books whose title contains "and".

\- `complex\_query` — a multi-condition query combining `filter()` and `exclude()` (author not null, title contains "and", edition ≥ 2, price above 100).

\- `my\_query` — a custom query returning books whose title contains the letter "a", with a price of 100 or less and an edition of 2 or higher.

\- `cheap\_books` — a custom query returning all books priced under 110, sorted from cheapest to most expensive using `order\_by('price')`.

\- Routes: `/books/simple/query`, `/books/complex/query`, `/books/my/query`, `/books/cheap/query`


