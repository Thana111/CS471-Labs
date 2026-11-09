# Lab 7 — Django Models & ORM Queries

## Overview
This lab covers Django Models (Part 1): defining a model, running migrations, inserting data, and querying the database with the Django ORM.

## What was implemented
- Task 1 — `Book` model (`title`, `author`, `price`, `edition`) in `apps/bookmodule/models.py`, with `makemigrations` / `migrate` applied
- Task 2 — Sample data inserted via the Django shell using `Book.objects.create(...)`
- Task 3 — `simple_query` (`/books/simple/query`) — `Book.objects.filter(title__icontains='and')`
- Task 4 — `complex_query` (`/books/complex/query`) — chained `filter()`/`exclude()` with `isnull`, `icontains`, `gte`, `lte` lookups and slicing
- Extra — two additional self-made queries: `my_query` (`/books/my/query`) and `cheap_query` (`/books/cheap/query`)

## URLs to test
- `/books/simple/query`
- `/books/complex/query`
- `/books/my/query`
- `/books/cheap/query`
