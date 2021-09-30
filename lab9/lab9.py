from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from PIL import Image

url = requests.get('https://ilearn.csumb.edu/') # set webpage url

soup = BeautifulSoup(url.content, 'lxml')   # create BeautifulSoup object, set url and parser

print(soup.title)   # print title of webpage

for pic in soup.find_all("img"):    # search through all img tags
    if(pic.get('alt') == ('Cat at computer')):  # find image with this alt title
        img_url = pic.get('src')    # save image url
        print(pic.get('alt'))   # print alt title
        print(img_url)  # print image url
        im = Image.open(requests.get(pic.get('src'), stream=True).raw)  # open image
        im.show()   # display retireved image
