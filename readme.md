# news image scraper
News image scraper is a simple Python script built in 2025 that automatically downloads the first image from a list of Varzezh-3 news article URLs. This tool is easy to use and helps you download images from the main list of news articles on the [varzesh3](https://www.varzesh3.com/) website.
## Requirements
- Python 3.x
- requests library
- beautifulsoup4 library
- a text file containing news URLs
## Installation
- Create an empty folder in VSCode
- Open terminal
- enter cmd
- create virtual venv use `python -m venv .venv`
- activate venv by `.venv\srcripts\activate`
- install requests `pip install requests`
- copy the `varzesh3py` file into your project folder
- Create an `images1` folder in the same directory to store downloaded images
## How to use
Once everything is set up, using the script is simple:
- Run the script `python varzesh3.py`

The script will:

1. Visit each URL in the list
2. Parse the page and find the main news image inside the div with class "news_body_lead"
3. Download all images found and save them to the images1/ folder

You can find all downloaded images in the images1/ directory, each named based on its original filename from the website.
