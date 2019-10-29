"""
This class models the cart and payment pages
"""
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from utils.Wrapit import Wrapit
import re


class Sunscreens_Moisturizers_Object:
    "Page Object for the cart and payment"
    
    #locators
    page_title = locators.page_title
    add_button = locators.add_moisturizer_sunscreen_button
    cart_count = locators.cart_count
    cart_button = locators.cart_button
    add_most_expensive = locators.add_item
    price_tag = locators.price_tag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_button(self):
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
        "Click all add buttons"
        result_flag =False
        number_of_items= self.get_elements(self.add_button)   #wrong function used, we need all elements
        for index in enumerate(number_of_items):
            print(index)
            #print(row)
            result_flag = self.click_element(self.add_button[index])
            self.conditional_write(result_flag,
            positive='Clicked on add button',
            negative='Could not click on add button',
            level='debug')    
        return result_flag

    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_added_count(self): 
        "Check the count of added items to the card with the number of add button. They should be same"
        result_flag =False
        number_of_items= self.get_elements(self.add_button)
        number_of_add_button = len(number_of_items)  #length of the right side variable should be assigned here
        cart_cnt = self.get_text(self.cart_count)
        cart_cnt = cart_cnt.decode('utf-8')
        if(int(cart_cnt[0])==1): #typo error
            result_flag=True
            self.conditional_write(result_flag,
            positive='One items added to the cart',
            negative='No items are not added to the cart',
            level='debug')
        elif(number_of_add_button == int(cart_cnt[0])): #typo error
            result_flag=True
            self.conditional_write(result_flag,
            positive='All items added to the cart',
            negative='Some items are not added to the cart',
            level='debug')    
        
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_cart(self):
        "Click cart items button"
        result_flag = self.click_element(self.cart_button)
        self.conditional_write(result_flag,
            positive='Clicked on cart button',
            negative='Could not click cart button',
            level='debug')    

        return result_flag
 
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_cart(self):
        "Check the cart screen is loaded on redirect"
        result_flag = False
        cart_url = 'cart'  #url is singular word        
        if cart_url.lower() in self.get_current_url().lower():
            result_flag = True
            self.switch_page("cart")
        self.conditional_write(result_flag,
            positive='Landed on cart screen',
            negative='Could not land on cart screen',
            level='debug')    

        return result_flag 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def add_all_items_and_verify_cart(self):
        "Add all items to the cart and verify if added successfully"
        result_flag =self.click_add_button()
        result_flag &=self.check_added_count()   
        result_flag &=self.click_cart() 
        result_flag &=self.check_redirect_cart()

        return result_flag        #wrong return variable
