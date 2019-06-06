#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################


temp_field = "xpath,//span[@id ='temperature']"
click_moisturizers = "xpath,//button[text()='Buy moisturizers']"
click_sunscreens= "xpath,//button[text()='Buy sunscreens']"

heading_moisturizer = "xpath,//h2[contains(text(),'Moisturizers')]"
heading_sunscreen = "xpath,//h2[contains(text(),'Sunscreens')]"

page_title = "xpath,//h2"

moisturizers = "xpath,//div[contains(@class,'text-center col-4')]"
sunscreens = "xpath,//div[contains(@class,'text-center col-4')]"

moisturizers_names = "xpath,//p[contains(@class,'font-weight-bold top-space-10')]"
sunscreens_names ="xpath,//p[contains(@class,'font-weight-bold top-space-10')]"

moisturizers_price = "xpath,//p[contains(text(),'Price')]"
sunscreens_price = "xpath,//p[contains(text(),'Price')]"

click_cart = "xpath,//button[contains(@class,'nav-link')]"
checkout_heading = "xpath,//h2"

product_price_element = "xpath,//p[contains(text(), '%s')]/following-sibling::p"
product_add_element ="xpath,//p[contains(text(), '%s')]/following-sibling::p[contains(text(),'%s')]/following-sibling::button"
      
pay_with_card = "xpath,//button['Pay with Card']"

iframe_name = "xpath,//iframe[@name='stripe_checkout_app']"
email = "xpath,//input[@type='email']"       

card_number  =  "xpath,//input[@type='tel']"

card_expiry = "xpath,//input[@placeholder='MM / YY']"

cvv = "xpath,//input[@placeholder='CVC']"

zip_code = "xpath, //input[@placeholder='ZIP Code']"

pay_button = "xpath, //button[@type ='submit']"







