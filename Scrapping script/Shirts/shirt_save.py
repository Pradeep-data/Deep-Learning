import shutil
import os
import requests

def make_directory(dirname):
    current_path=os.getcwd()
    path=os.path.join(current_path, dirname)
    if not os.path.exists(path):
        os.makedirs(path)

def shirt_save(data, dirname, page):
    for index, link in enumerate(data['image_urls']):
        print("Downloading {0} of {1} images".format(index + 1, len(data['image_urls'])))
        response=requests.get(link)
        with open('{0}/img_{1}{2}.jpeg'.format(dirname, page, index), "wb") as file:
            file.write(response.content)
