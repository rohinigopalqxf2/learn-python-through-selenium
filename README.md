# learn-python-through-selenium
Learn Python as you solve Selenium exercises

Fix the issues in this repo and make this program work. This repository is aimed at folks who have already learnt to write basic Python but are looking for more realistic challenges that involve reading a large enough codebase, exploring file structures and making changes to an existing codebase.

The code you are going to run is a Selenium test for the Weather Shopper application. The automated test itself completes the weather shopper exercise. Your job is to fix the problems in the automated test and make it run successfully.

Setup

This codebase uses Python 3.7.x

Fork this repository

Clone your forked repository

Create a virtualenv and activate it

pip install -r requirements.txt

Install Chrome driver

There are 4 tests and each can be run using following commands

pytest -k add_all_items_to_cart_and_checkout

pytest -k add_all_moiturizers_to_cart

pytest -k most_expensive_sunscreen

pytest -k most_expensive_moisturizer

pytest -k select_2_least_expensive_sunscreens

pytest -k select_2_least_expensive_moisturizers

