#!/usr/bin/env python


import requests
from bs4 import BeautifulSoup
import time

while True:

    time.sleep(2)

    r = requests.get("http://www.timeanddate.com/moon/usa/atlanta")
    # print r.content

    soup = BeautifulSoup(r.content)
    # print soup.prettify()

    g_data = soup.find_all("div", {"id": "qfacts"})

    for pTags in g_data:
        ptags = pTags.find_all("p")
        # print ptags

        for tag in ptags:
            print tag.text

    print "\n"





    r = requests.get("https://www.heavens-above.com/moon.aspx?lat=0&lng=0&loc=Unspecified&alt=0&tz=CET")
    # print r.content

    soup = BeautifulSoup(r.content)
    # print soup.prettify()

    g_data = soup.find_all("td", {"valign": "top"})
    print g_data

    # for pTags in g_data:
    #     ptags = pTags.find_all("p")
    #     # print ptags
    #
    #     for tag in ptags:
    #         print tag.text
    #
    # print "\n"
