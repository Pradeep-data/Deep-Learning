from selenium import webdriver
import os
import shutil
import requests

driver=webdriver.Chrome(executable_path='D:\\Software\\chromedriver_win32\\chromedriver.exe')
my_page=driver.get('https://www.amazon.in/s?rh=n%3A17186600031&page=2&qid=1594144394&ref=lp_17186600031_pg_2')
def make_directory(dirname):
    current_path=os.getcwd()
    path=os.path.join(current_path, dirname)
    if not os.path.exists(path):
        os.makedirs(path)

make_directory("saree")

images=driver.find_elements_by_xpath("//img[@class='s-image']")

urls=[]
for image in images:
    source=image.get_attribute('src')
    urls.append(source)

for index, link in enumerate(urls):
    print("Downloading {0} of {1} images".format(index + 1, len(urls)))
    response=requests.get(link)
    with open('saree/img_{0}.jpeg'.format(index), "wb") as file:
        file.write(response.content)
