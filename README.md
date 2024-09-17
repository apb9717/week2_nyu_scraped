# week2_NYU_Scraped

A Python project to scrape free weather data from weather.gov, a highly-accurate yet severely underutilized data source.

# Overview

This feature returns a forecast for the current day plus the following five days, including the following four days' night forecasts as well. It includes information on precipitation, temperature (in Fahrenheit), and wind speeds.

# Setup Instructions

First, set up a Python virtual environment by first running "python -m venv .venv" then running

- ".venv\Scripts\activate" on Windows
- "source .venv/bin/activate" on Mac

Verify that the terminal prefix is (.venv) to demonstrate that you have successfully set up the virtual environment.
Then, install the necessary packages listed in requirements.txt with "pip install -r requirements.txt".

# Usage

Simply run the program and the forecast will be generated for New York City.

# Notes

I sincerely hope nobody else used this website.
For the sake of usability, we simply set up the program to work for the NYC forecast, as lat/long are used in the URL. In a future iteration, using some library which converts a place name to coordinates, we could make the system more robust and have it apply for a wider variety of locations.
