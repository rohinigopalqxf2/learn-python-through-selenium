from .Base_Page import Base_Page
from .moisturizer_object import Moisturizer_Object
from .sunscreen_object import Sunscreen_Object
import conf.locators_conf as locators

page_title = locators.page_title 
cart_button = locators.click_cart 



class Common_Object(Moisturizer_Object,Sunscreen_Object):
    "Class for all the common objects"

    #locators
    
    pay_with_card = locators.pay_with_card  
    iframe_name = '//iframe[@name="stripe_checkout_app"]'    
    email_field = locators.email 
    card_number_field = locators.card_number
    card_expiry_date_field = locators.card_expiry
    cvv_field = locators.cvv
    zip_code_field = locators.zip_code
    pay_button = locators.pay_button
    redirect_title_cart = 'cart'

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
        result_flag &= self.switch_to_stripe_frame(self.iframe_name)
        

    def switch_to_stripe_frame(self,iframe_name):
        "Switch to payment gateway"
        print ("frame1")
        result_flag = self.switch_frame(self.iframe_name)
        self.conditional_write(result_flag,
            positive='Switched the frame: %s'%iframe_name,
            negative='Failed to switch the frame',
            level='debug')
       
        return result_flag

    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.email_field,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag    

    def set_card_number(self,card_number):
        "Set the card number on the form"
        result_flag = self.set_text(self.card_number_field,email)
        self.conditional_write(result_flag,
            positive='Set the card number to: %s'%card_number,
            negative='Failed to set the card number in the form',
            level='debug')

        return result_flag  

    def set_card_expiry_date(self,card_expiry):
        "Set the card expiry date(mm/yy) on the form"
        result_flag = self.set_text(self.card_expiry_date_field,email)
        self.conditional_write(result_flag,
            positive='Set the card expiry date to: %s'%card_expiry,
            negative='Failed to set the expiry date in the form',
            level='debug')

        return result_flag

    def set_cvv(self,cvv):
        "Set the cvv on the form"
        result_flag = self.set_text(self.cvv_field,cvv)
        self.conditional_write(result_flag,
            positive='Set the cvv to: %s'%card_expiry,
            negative='Failed to set the cvv in the form',
            level='debug')

        return result_flag 


    def set_zip_code(self,zip_code):
        "Set the zip code on the form"
        result_flag = self.set_text(self.zip_code_field,zip_code)
        self.conditional_write(result_flag,
            positive='Set the zip code to: %s'%zip_code,
            negative='Failed to set the zip_code in the form',
            level='debug')

        return result_flag    


    def click_on_pay_with_card(self):        
        result_flag = self.click_element(self.pay_with_card)        
        self.conditional_write(result_flag,
            positive='Clicked on the "Pay with card" button',
            negative='Failed to click on "Pay with card" button',
            level='debug')

        return result_flag  


    def click_pay_button(self):        
        result_flag = self.click_element(self.pay_button)        
        self.conditional_write(result_flag,
            positive='Clicked on the "Pay" button',
            negative='Failed to click on "Pay" button',
            level='debug')

        return result_flag     

    def submit_form(self,email,card_number,card_expiry,cvv,zip_code):
        "Submit the form"
        result_flag = self.set_email(email)
        result_flag &= self.set_card_number(card_number)
        result_flag &= self.set_card_expiry_date(card_expiry)
        result_flag &= self.cvv(cvv)
        result_flag &= self.set_zip_code(zip_code)
        result_flag &= self.click_pay_button()
        #result_flag &= self.check_redirect()

        return result_flag 

    def check_redirect(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False
        if self.redirect_title in self.driver.title:
            result_flag = True
            self.switch_page("redirect")
        
        return result_flag

    def get_title(self):
        "get title"
        title = self.get_text(page_title)

        return title 

        
