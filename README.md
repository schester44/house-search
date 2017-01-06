# Simplified Housing Searches With Craiglist And Slack


## Description
A python bot that scrapes craigslist for house listings based on supplied gps coordinates and keywords.
Listings that match the criteria are posted to a slack channel for easy management. 
Utilizes SQLite to prevent duplicate postings
This same bot could be used to scrape any number of craigslist categories with minimum effort.


A modified version of this excellent write up:
https://www.dataquest.io/blog/apartment-finding-slackbot/

## Getting Started

You'll need a Slack channel and a Slack API Token (test tokens work fine) https://api.slack.com/docs/oauth-test-tokens

- Download/Clone Repo
- Replace SLACK_TOKEN in settings.py with your slack token
- You'll probably want to change other settings in settings.py (min/max price, neighborhoods, coordinates, etc)
- `pip install -r requirements.txt` to install dependencies
- `python main.py` to start the app
