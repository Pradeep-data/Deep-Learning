from selenium import webdriver
from saree_save import make_directory,saree_save
from saree_images import scrap_image_url
from selenium.common.exceptions import StaleElementReferenceException

DRIVER_PATH='D:\\Software\\chromedriver_win32\\chromedriver.exe'

driver=webdriver.Chrome(executable_path=DRIVER_PATH)
current_page_url=driver.get('https://www.amazon.in/b/ref=s9_acss_bw_cg_WWDTIMPC_2b1_w?node=17186600031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=8Y1RXX2MRAWB3YHJCC38&pf_rd_t=101&pf_rd_p=79601a8b-7d7e-4e08-84fe-e82957496171&pf_rd_i=1968256031')

DIRNAME= "Sarees"
make_directory(DIRNAME)

start_page=1
total_pages=2

for page in range(start_page, total_pages+1):
    try:
        product_details=scrap_image_url(driver=driver)
        print("Scraping page {0} of {1} pages".format(page, total_pages))

        page_value=driver.find_element_by_xpath("//span[@class='pagnCur']").text
        print("The current page scraped is {}".format(page_value))
        
        saree_save(data=product_details, dirname=DIRNAME, page=page)
        print("Scraping of page {0} done".format(page))
        

        print("Moving to the next page")
        button_type=driver.find_element_by_xpath("//div[@class='pagnHy']//a[@class='pagnNext']//span").get_attribute('innerHTML')

        if button_type=='Next':

            driver.find_element_by_xpath("//a[@class='pagnNext']").click()
        else:
            driver.find_element_by_xpath("//a[@class='pagnNext'][2]").click()

        new_page= driver.find_element_by_xpath("//span[@class='pagnCur']").text
        print("The new page is {}".format(new_page))
        
    except StaleElementReferenceException as Exception:
        print("We are facing an exception")

        exp_page=driver.find_element_by_xpath("//span[@class='pagnCur']").text
        print("The page value at the time of exception is {}".format(exp_page))

        value=driver.find_element_by_xpath("//span[@class='pagnCur']")
        link=value.get_attribute('href')
        driver.get(link)

        product_details=scrap_image_url(driver=driver)
        print("Scraping page {0} if {1} pages".format(page,total_pages))

        page_value=driver.find_element_by_xpath("//span[@class='pagnCur']").text
        print("The current page scrapped is {}".format(page_value))

        #downloading the images
        saree_save(data=product_details, dirname=DIRNAME, page=page)
        print("Scraping of page {0} done".format(page))

        #moving to the next page
        print("moving to the next page")

        button_type=driver.find_element_by_xpath("//div[@class='pagnHy']//a[@class='pagnNext']//span").get_attribute('innerHTML')

        if button_type =='Next':
            driver.find_element_by_xpath("//a[@class='pagnNext']").click()
        else:
            driver.find_element_by_xpath("a[@class='pagnNext'][2]").click()

        new_page=driver.find_element_by_xpath("//span[@class='pagnCur']").text
        print("The new page is {}".format(new_page))
