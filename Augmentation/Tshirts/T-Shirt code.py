from selenium import webdriver
import os
import shutil
import requests

driver=webdriver.Chrome(executable_path='D:\\Software\\chromedriver_win32\\chromedriver.exe')
my_page=driver.get('https://www.amazon.in/s?rh=n%3A1968123031%2Cp_36%3A4595084031&pf_rd_i=1968123031&pf_rd_p=aae87896-3cf4-5471-9447-cc20e584d0a8&pf_rd_r=QTXVVGF8HQX8E521TVBV&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&ref=Oct_s9_apbd_oup_hd_bw_b29C2hr_S')

def make_directory(dirname):
    current_path=os.getcwd()
    path=os.path.join(current_path, dirname)
    if not os.path.exists(path):
        os.makedirs(path)

make_directory("T-Shirts")

images=driver.find_elements_by_xpath("//img[@class='s-image']")

urls=[]
for image in images:
    source=image.get_attribute('src')
    urls.append(source)

for index, link in enumerate(urls):
    print("Downloading {0} of {1} images".format(index + 1, len(urls)))
    response=requests.get(link)
    with open('T-Shirts/img_{0}.jpeg'.format(index), "wb") as file:
        file.write(response.content)

