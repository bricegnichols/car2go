import time
import urllib2
import sched
import json
import os

# List of cities we want to include
city_list = ["austin", "columbus", "denver", "miami", "minneapolis", "portland", "seattle", "vancouver", "montreal"]
download_interval = 2     # in minutes
USER_KEY = 'USER_KEY'
save_path = "D:/Car2Go/" + city

# Access vehicle location data for all cities, save contents in a city-specific directory
def write_locations():
    for city in city_list:
        baseurl = 'https://www.car2go.com/api/v2.1/vehicles?loc=' + city + '&oauth_consumer_key=' + USER_KEY + '&format=json'
        page = urllib2.urlopen(baseurl)
        information = page.read()
        fname = time.strftime("%m_%d_%Y_%H_%M_%S")
        fname = os.path.join(save_path, time.strftime("%m_%d_%Y_%H_%M_%S"))
        with open(fname + '.json', 'w') as f:
            f.write(information)

# "Don't call us, we'll call you." 
#
# This just runs the write_locations function continuously at a given interval. 
# I want to figure out how to run this entire script at an interval instead, since
# I really don't want this instance open constantly. Windows task scheduler worked
# previously, but there may be a better way?  
while True:
    time.sleep(60*download_interval)
    write_locations()