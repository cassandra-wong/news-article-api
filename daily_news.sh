#!/bin/bash

python3 fetch_news.py
echo "fetch_news.py done"

python3 clean_db.py 
echo "Deleted old articles over 5 days old"