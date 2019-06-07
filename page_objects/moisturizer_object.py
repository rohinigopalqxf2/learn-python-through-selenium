"""
This class models the form on the weather shopper application main page
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import re


class Moisturizer_Object:
    "Page object for the Moisturizer"
     
    #locators         
    
    product_price_element = locators.product_price_element
    product_add_element = locators.product_add_element
    cart_button = locators.click_cart  
    checkout_heading = locators.checkout_heading  
    redirect_title_cart = 'cart'

    def add_moisturizers(self):
        "add moisturizers" 
      
        result_flag = False        
        product_category =['Aloe','Almond']

        for product in product_category:
            price_product = 100000          
            product_elements = self.get_elements(self.product_price_element%product)

            for element in product_elements:                
                product_price = element.text                   
                product_price = re.findall(r'\b\d+\b', product_price)              
                if int(product_price[0]) < price_product:                   
                    price_product = int(product_price[0])                
            result_flag = self.click_element(self.product_add_element%(product,price_product))
            self.conditional_write(result_flag,
                                positive='Successfully added moisturizers',
                                negative='Failed to add moisturizers',
                                level='debug')        

        return result_flag


    def click_cart(self):
        "Click on the Cart button"
        result_flag = self.click_element(self.cart_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "cart" button',
            negative='Failed to click on "cart" button',
            level='debug')

        return result_flag     


    def check_redirect_cart(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False        
        #self.driver.title = "The best sunscreens in the world!"
        #remove after Arun changes the title for sunscreens      
            
        result_flag = True if self.check_element_present(self.checkout_heading) else False        
        self.conditional_write(result_flag,
                               positive="User is redirected to cart Page ",
                               negative="User is not redirected to cart Page",
                               level='debug')
        if result_flag == True:
            self.switch_page("cart")

        return result_flag 

    def process_moisturizers(self):
        "Process Moisturizers"
        result_flag = self.add_moisturizers()
        result_flag &= self.click_cart()
        result_flag &= self.check_redirect_cart()
        
        return result_flag