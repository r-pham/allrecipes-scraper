# About
 Web scraper to fetch recipes and details from allrecipes

# Usage
- Create a virtualenv
- Run `pip install -r requirements.txt`
- Run `python main.py` to start scraper

You may also import the allrecipes_scraper.py in python to test individual functions

# TODO
- Unit tests

# Optimizations
- Clean up requirements.txt for unnecessary libraries? The main things I need are bs4, request, dataclasses, and dataclasses-json

# Concerns
Urls changing -- can be addressed with a monitor system to check validity of urls?