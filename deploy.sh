#!/usr/bin/env bash

python3 manage.py test

if [ $? -eq 0 ]; then 
    git push heroku main 
    exit 0
fi

echo "there are errors in the code."
exit 1
