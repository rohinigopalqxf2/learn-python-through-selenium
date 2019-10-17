"""
This class models the table on the Selenium tutorial page
"""
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from utils.Wrapit import Wrapit


class Sunscreens_Moisturizers_Object:
    "Page Object for the Sunscreen's and Moisturizer's page"
    
    #locators
    page_title = locators.page_title
    add_button = locators.add_moisturizer_sunscreen_button
    cart_count = locators.cart_count

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_button(self,page_title):
        "Click add button"
        result_flag = self.click_element(self.add_button)
        self.conditional_write(result_flag,
            positive='Clicked on add button',
            negative='Could not click add button',
            level='debug')    

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_all_add_button(self):
        "Click all add  button"
        result_flag =False
        number_of_items= self.get_elements(self.add_button)
        for element in number_of_items:
            result_flag = self.click_element(self.add_button)
            self.conditional_write(result_flag,
            positive='Clicked on add button',
            negative='Could not click on add Sunscreen button',
            level='debug')    
        return result_flag

    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_added_count(self):
        "Check the count of added items to the card with the number of add button. They should be same"
        result_flag =False
        number_of_items= self.get_elements(self.add_button)
        number_of_add_button = len(number_of_items)
        cart_cnt = self.get_text(self.cart_count)
        cart_cnt = cart_cnt.decode('utf-8')
        
        if(number_of_add_button == int(cart_cnt[0])):
            result_flag=True
            self.conditional_write(result_flag,
            positive='All items added to the cart',
            negative='Some items are not added to the cart',
            level='debug')    
        
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def add_all_items_and_verify_cart(self):
        "Add all items to the cart and verify if added successfully"
        result_flag =self.click_all_add_button()
        result_flag &=self.check_added_count()    

        return result_flag
        