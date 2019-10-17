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

#Main page
page_title = "xpath,//h2"
temperature_field = "xpath,//span[@id ='temperature']"
click_moisturizers = "xpath,//button[text()='Buy moisturizers']"
click_sunscreens= "xpath,//button[text()='Buy sunscreens']"
heading_text = "xpath,//h2[contains(text(),'%s')]"
heading_sunscreen = "xpath,//h2[contains(text(),'Sunscreens')]"
heading_moisturizer = "xpath,//h2[contains(text(),'Moisturizers')]"

add_moisturizer_sunscreen_button ="xpath,//button[@class='btn btn-primary']"
cart_count ="xpath,//span[contains(text(),'item(s)')]"
