# learn-POM-framework-through-selenium-using-python

The code you are going to run is a Selenium test for the [Weather Shopper application](https://weathershopper.pythonanywhere.com/).The app is in-house app of [Qxf2](https://qxf2.com/).The excercises will help you understand POM framework better along with python.

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

