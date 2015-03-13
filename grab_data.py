#!/usr/bin/env python
#Learn how this works here: http://youtu.be/pxofwuWTs7c


# https://dev.locu.com/console/
# 20flint12@gmail.com 87



import urllib2
import json

locu_api = '4bae877ebeace9a13ccfd6cdc3a906ec59360590'

def locu_search(query):
    api_key = locu_api
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)

    for item in data['objects']:
        print item['name'], item['phone']


locu_search("new york")
