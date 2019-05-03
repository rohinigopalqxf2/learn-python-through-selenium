from .Base_Page import Base_Page
from .moisturizer_object import Moisturizer_Object
from .sunscreen_object import Sunscreen_Object
import conf.locators_conf as locators


page_title = locators.page_title 
cart_button = locators.click_cart 
pay_with_card = locators.pay_with_card   
redirect_title_cart = 'cart'

class Common_Object(Moisturizer_Object,Sunscreen_Object):
    "Class for all the common objects"
    def select_product_type(self):
        "select two products"
        title = self.get_title() 
        title = title.decode('utf-8')       
        result_flag = None
        if title in "Moisturizers":
            result_flag = self.process_moisturizers()            
        elif title in 'Sunscreens':
            result_flag = self.process_sunscreens()               

        return result_flag

    
    def make_payment_with_card(self):
        "Make the payment for the items"
        result_flag = self.click_on_pay_with_card()
        result_flag &= self.set_email()


    def set_email():
        "Set the email on the form"
        result_flag = self.set_text(self.email_field,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag    


    def click_on_pay_with_card(self):
        result_flag = self.click_element(self.pay_with_card)
        
        self.conditional_write(result_flag,
            positive='Clicked on the "Pay with card" button',
            negative='Failed to click on "Pay with card" button',
            level='debug')

        return result_flag  

        
    def get_title(self):
        "get title"
        title = self.get_text(page_title)

        return title 

        
