"""
This class models the redirect page of the temperature page
URL: moisturizer
The page consists of product info, price and adding to cart
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from .common_object import Common_Object
from .moisturizer_object import Moisturizer_Object
from utils.Wrapit import Wrapit


class Temp_Moisturizer_Redirect_Page(Base_Page,Common_Object,Moisturizer_Object):
    "Page Object for the redirect page"

    #locators
    heading = locators.heading_moisturizer

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'moisturizer'
        self.open(url)

    @Wrapit._exceptionHandler    
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading)
        self.conditional_write(result_flag,
            positive='Correct heading present on redirect page',
            negative='Heading on redirect page is INCORRECT!!',
            level='debug')

        return result_flag
