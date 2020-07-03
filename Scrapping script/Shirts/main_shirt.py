from selenium import webdriver
from shirt_save import make_directory,shirt_save
from tshirt_images import scrap_image_url
from selenium.common.exceptions import StaleElementReferenceException

DRIVER_PATH='D:\\Software\\chromedriver_win32\\chromedriver.exe'

driver=webdriver.Chrome(executable_path=DRIVER_PATH)
current_page_url=driver.get('https://www.amazon.in/s?rh=n%3A1968093031%2Cp_36%3A4595084031&pf_rd_i=1968093031&pf_rd_p=738077a3-5b62-5f3b-83e7-1365e864c127&pf_rd_r=ZCPDXMM8P9GNM8DFQ7R0&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&ref=Oct_s9_apbd_oup_hd_bw_b29Butz_S')

DIRNAME= "Shirts"
make_directory(DIRNAME)

start_page=1
total_pages=2

for page in range(start_page, total_pages+1):
    try:
        product_details=scrap_image_url(driver=driver)
        print("Scraping page {0} of {1} pages".format(page, total_pages))

        page_value=driver.find_element_by_xpath("//li[@class='a-selected']").text
        print("The current page scraped is {}".format(page_value))
        
        shirt_save(data=product_details, dirname=DIRNAME, page=page)
        print("Scraping of page {0} done".format(page))
        

        print("Moving to the next page")
        button_type=driver.find_element_by_xpath("//div[@class='a-text-center']//li[@class='a-last']").get_attribute('innerHTML')

        if button_type=='Next':

            driver.find_element_by_xpath("li[@class='a-last']").click()
        else:
            driver.find_element_by_xpath("li[@class='a-last'][2]").click()

        new_page= driver.find_element_by_xpath("//li[@class='a-selected']").text
        print("The new page is {}".format(exp_page))
        
    except StaleElementReferenceException as Exception:
        print("We are facing an exception")

        exp_page=driver.find_element_by_xpath("//li[@class='a-selected']").text
        print("The page value at the time of exception is {}".format(exp_page))

        value=driver.find_element_by_xpath("//li[@class='a-selected']")
        link=value.get_attribute('href')
        driver.get(link)

        product_details=scrap_image_url(driver=driver)
        print("Scraping page {0} if {1} pages".format(page,total_pages))

        page_value=driver.find_element_by_xpath("//li[@class='a-selected']").text
        print("The current page scrapped is {}".format(page_value))

        #downloading the images
        save_images(data=product_details, dirname=DIRNAME, page=page)
        print("Scraping of page {0} done".format(page))

        #moving to the next page
        print("moving to the next page")

        button_type=driver.find_element_by_xpath("//div[@class='a-text-center']//li[@class='a-last']").get_attribute('innerHTML')

        if button_type =='Next':
            driver.find_element_by_xpath("//li[@class='a-last']").click()
        else:
            driver.find_element_by_xpath("//li[@class='a-last'][2]").click()

        new_page=driver.find_element_by_xpath("//li[@class='a-selected']").text
        print("The new page is {}".format(new_page))
