#!/usr/bin/env python
# coding: utf8


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

        # timeTags = item.find("div", {"class": "article__time"})
        # titlTags = item.find("div", {"class": "article__title"})
        # str2 = timeTags.text + titlTags.text
        # print str2


    if str_last_time == str_news:
        return None
    else:
        str_last_time = str_news
        return str_last_time


    # print g_data[0]
    # print "\n"
    # print "1#"*40
    # print g_data[1]
    # print "\n"
    # print "2#"*40
    # print g_data[2]
    # print "\n"
    # print "3#"*40

    # tabTags = g_data[2].find_all("table")
    #
    # trTags = tabTags[1].find_all("tr")
    # # for tr in trTags:
    # #     print tr.text
    # #
    # #     # line = u(tr.text)
    # #     str_re = u"Давление (на станции) (.*) мм.рт.ст."
    # #     # res = re.search(str_re, str)
    # #     # if res:
    # #     #     print res.group(1)  # pressure
    #
    #
    # out_str = trTags[1].text
    # # print trTags[1].text
    #
    # return out_str


print (get_news())

# print (get_temperature())