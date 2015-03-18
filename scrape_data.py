#!/usr/bin/env python

# https://dev.locu.com/console/
# 20flint12@gmail.com 87

import requests
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#problems-after-installation
from bs4 import BeautifulSoup

r = requests.get("http://mail.ru")

# print r.content

soup = BeautifulSoup(r.content)

# print soup.prettify()

print soup.find_all("a")