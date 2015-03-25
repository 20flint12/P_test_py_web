#!/usr/bin/env python
# coding: utf8

import os
import urllib
import urllib2


import requests
from bs4 import BeautifulSoup
import time
import re


str_last_time = ""

def get_news():

    global str_last_time

    r = requests.get("http://korrespondent.net/")
    # print r.content

    soup = BeautifulSoup(r.content)
    # print soup.prettify()
    g_data = soup.find_all("div", {"class": "time-articles"})
    # print g_data

    str_news = ""
    for item in g_data:
        # print item
        # print item.text

        time_artTags = item.find("div", {"class": "article "})
        # print time_artTags.text

        str_news = time_artTags.text
        # print (str_news)


    if str_last_time == str_news:
        return None
    else:
        str_last_time = str_news
        return str_last_time



print (get_news())





#
#
# url = "http://icecat.biz/p/toshiba/pscbxe-01t00een/satellite-pro-notebooks-4051528049077-Satellite+Pro+C8501GR-17732197.html"
# html = urllib2.urlopen(url)
# soup = BeautifulSoup(html)
#
# imgs = soup.findAll("div", {"class":"thumb-pic"})
# print imgs
# for img in imgs:
#     imgUrl = img.a['href'].split("imgurl=")[0]
#     urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))


def download_photo(self, img_url, filename):
    try:
        image_on_web = urllib.urlopen(img_url)
        if image_on_web.headers.maintype == 'image':
            buf = image_on_web.read()
            path = os.getcwd() + DOWNLOADED_IMAGE_PATH
            file_path = "%s%s" % (path, filename)
            downloaded_image = file(file_path, "wb")
            downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
        else:
            return False
    except:
        return False
    return True
