\# Lab 2 — Django Project Setup \& Git Initialization



\## Overview

This lab covers installing and configuring Django for the first time: creating a virtual environment, installing Django, creating the `libraryproject` Django project, and structuring it into two reusable apps (`bookmodule` and `usermodule`). It also covers initializing a local Git repository and connecting it to a remote GitHub repository.



\## What was implemented

\- Created and activated a Python virtual environment (`djangoenv`)

\- Installed Django via pip

\- Created the Django project `libraryproject` using `django-admin startproject`

\- Verified the default Django welcome page at `http://127.0.0.1:8000/`

\- Created an `apps/` folder with `template/` and `static/` subfolders

\- Generated two Django apps inside `apps/`: `bookmodule` and `usermodule` using `startapp`

\- Updated each app's `apps.py` to use the dotted app name (`apps.bookmodule`, `apps.usermodule`)

\- Registered both apps in `INSTALLED\_APPS` in `libraryproject/settings.py`

\- Initialized a local Git repository and connected it to the GitHub remote

