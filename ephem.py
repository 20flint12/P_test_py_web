
# http://blogs.bu.edu/mhirsch/2012/08/installing-pyephem-in-ubuntu-computing-sunrisesunset-in-python/
# https://wiki.python.org/moin/CheeseShopTutorial
# https://virtualenv.pypa.io/en/latest/installation.html


import ephem
import datetime

now = datetime.datetime.now() #get current time

Boston=ephem.Observer()
Boston.pressure = 1010 # millibar
Boston.temp = 25 # deg. Celcius
Boston.horizon = 0
Boston.lat='42.3462'
Boston.lon='-71.0978'
Boston.elevation = 3 # meters
Boston.date = now

sun = ephem.Sun()

print("Next sunrise in Boston will be: ",ephem.localtime(Boston.next_rising(sun)))
print("Next sunset in Boston will be: ",ephem.localtime(Boston.next_setting(sun)))