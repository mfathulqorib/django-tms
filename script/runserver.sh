#!/bin/bash

# Pindah ke direktori proyek
cd ~/Projects/Python/django-tms || exit

# Aktifkan virtual environment
source .venv/bin/activate

# Buka terminal baru untuk npm run tw
osascript -e 'tell application "Terminal" to do script "cd ~/Projects/Python/django-tms && npm run tw"'

# Jalankan Django server
python3 manage.py runserver



