"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Temperature main page
2. Moistureizer page
3. Sunscreens Page
4. Cart Page
5. Payment Page
"""

from page_objects.temp_main_page import Temp_Main_Page

class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url='http://weathershopper.pythonanywhere.com/',trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name == "main page":
            print (base_url)
            test_obj = Temp_Main_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        return test_obj

    get_page_object = staticmethod(get_page_object)