# learn-python-through-selenium

Learn Python as you run the Selenium tests

The code you are going to run is a Selenium test for the [Weather Shopper application](https://weathershopper.pythonanywhere.com/).The automated test itself completes the weather shopper exercise. Your job is to fix the problems in the automated test and make it run successfully.

Setup
1. This codebase uses Python 3.7.x.
2. Fork this repository
3. Clone your forked repository
4. Create a virtualenv and activate it
5. pip install -r requirements.txt
6. Install Chrome driver

There are 6 tests and each can be run using following commands

```pytest -k add_all_items_to_cart_and_checkout
    pytest -k add_all_moiturizers_to_cart
    pytest -k most_expensive_sunscreen
    pytest -k most_expensive_moisturizer
    pytest -k select_two_least_expensive_sunscreens
    pytest -k select_two_least_expensive_moisturizers
    pytest -k read_weather_and_redirect
```
The setup instructions are intentionally high-level since this repository is aimed at people with people who have already written Python before. If you are beginner, you will find our other repository a better place to start.

