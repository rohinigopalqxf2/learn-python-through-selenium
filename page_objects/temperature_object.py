"""
This class models the form on the weather shopper application main page
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import sys


class Temperature_Object:
    "Page object for the Form"
    
    #locators
    temp_field = locators.temp_field
    click_buy_moisturizers = locators.click_moisturizers
    click_buy_sunscreens = locators.click_sunscreens
  

    def get_temperature(self):
        "get the temperature value from the page"
        temp_element = self.get_element(self.temp_field).text
        temp_element = temp_element[:-2]
        #temp_element.encode(sys.stdout.encoding, 'ignore').decode(sys.stdout.encoding)
        print(temp_element)
        #temp_element = temp_element[:2]

        return temp_element


    def click_moisturizers(self):
        "click the Buy moisturizers button"
        print ("enter")
        result_flag = self.click_element(self.click_buy_moisturizers)
        self.conditional_write(result_flag,
            positive='Clicked on the "Buy moisturizers" button',
            negative='Failed to click on "Buy moisturizers" button',
            level='debug')

        return result_flag


    def click_sunscreens(self):
        "click the Buy sunscreens button"
        result_flag = self.click_element(self.click_buy_sunscreens)
        self.conditional_write(result_flag,
            positive='Clicked on the "Buy sunscreens" button',
            negative='Failed to click on "Buy sunscreens" button',
            level='debug')

        return result_flag

    