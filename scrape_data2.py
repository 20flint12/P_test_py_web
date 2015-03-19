#!/usr/bin/env python


import matplotlib as plt


import requests
from bs4 import BeautifulSoup
import time

while True:

    time.sleep(5)

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

    print "\n"*10





    r = requests.get("https://www.heavens-above.com/moon.aspx?lat=0&lng=0&loc=Unspecified&alt=0&tz=CET")
    # print r.content

    soup = BeautifulSoup(r.content)
    # print soup.prettify()

    g_data = soup.find_all("td", {"valign": "top"})
    # # print g_data[0]
    # # print "\n"*10
    # print g_data[1]
    # print "\n"*10
    # print g_data[2]
    # print "\n"*10


    tableTags = g_data[1].find_all("table")

    for table in tableTags:

        trTags = table.find_all("tr")
        # print trTags

        for tag in trTags:
            print tag.text


    print "\n"*10


    # for pTags in g_data[1]:
    #     ptags = pTags.find_all("p")
    #     print ptags

        # for tag in ptags:
    #         print tag.text
    #
    # print "\n"
