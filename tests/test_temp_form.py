"""
This is an example automated test to help you learn Qxf2's framework
Our automated test will do the following:
    #Open http://weathershopper.pythonanywhere.com page.
    #Read the temperature
    #
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser


def test_temp_form(base_url,browser,browser_version,os_version,os_name,remote_flag,remote_project_name,remote_build_name):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object 
        test_obj = PageFactory.get_page_object("Main Page",base_url=base_url)

        #2. Setup and register a driver
        start_time = int(time.time())	#Set start_time with current time
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)
        
         #5. get the current temperature
        result_flag = test_obj.check_temperature()      
        test_obj.log_result(result_flag,
                            positive="Successfully read the temperature",
                            negative="Failed to read the temperature")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #Update TestRail
        #case_id = testrail_file.test_example_form_name
        #test_obj.report_to_testrail(case_id,test_run_id,result_flag)
        #test_obj.add_tesults_case("Set Name", "Sets the name in the form", "test_example_form", result_flag, "Failed to set name: %s \nOn url: %s\n"%(name,test_obj.get_current_url()), [test_obj.log_obj.log_file_dir + os.sep + test_obj.log_obj.log_file_name])
        
        if result_flag is True:
            result_flag = test_obj.check_heading()
        test_obj.log_result(result_flag,
                            positive="Heading on the redirect page checks out!\n",
                            negative="Fail: Heading on the redirect page is incorrect!")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        result_flag = test_obj.select_product_type()  
        test_obj.log_result(result_flag,
                            positive="Selected the products\n",
                            negative="Not able to select the products")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))        
          
        result_flag = test_obj.check_cart_heading()
        test_obj.log_result(result_flag,
                            positive="Heading on the cart page checks out\n",
                            negative="Fail: Heading on the cart page is incorrect!")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 
        


        #13. Print out the results
        test_obj.write_test_summary()

        #Teardown
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter
        test_obj.teardown()
        
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
       
    
#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_temp_form(base_url=options.url,
                        browser=options.browser,
                        browser_version=options.browser_version,
                        os_version=options.os_version,
                        os_name=options.os_name,
                        remote_flag=options.remote_flag,
                        remote_project_name=options.remote_project_name,
                        remote_build_name=options.remote_build_name) 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())
