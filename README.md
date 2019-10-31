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

pytest -k select_2_least_expensive_sunscreens

The setup instructions are intentionally high-level since this repository is aimed at people with people who have already written Python before. If you are beginner, you will find our other repository a better place to start.

Your assignment

The weather shopper exercise has been partially completed using the code provided to you. Your assignment is to:
fix the errors in the existing code

How to proceed?

Run the test using the command 

pytest -k add_all_items_to_cart_and_checkout

pytest -k add_all_moiturizers_to_cart

pytest -k most_expensive_sunscreen

pytest -k select_2_least_expensive_sunscreens

Observe, debug and fix the error

Test your fix

Commit your change and push

Repeat same steps to the next error till the tests run successfully
