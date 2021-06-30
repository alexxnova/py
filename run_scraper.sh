#!/bin/bash

# SCRAPE
echo Sraping ...
python main.py 

# TESTS
read -p "Run tests? y/n "

if [[ $REPLY =~ ^[Yy]$ ]]
then
    python -m pytest --cov-config=.coveragerc --cov-report term-missing --cov-report html:coverage --cov-fail-under=90 --cov=. test/unit_tests
else 
    exit 3
fi
