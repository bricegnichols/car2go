import time
import urllib2
import sched
import json
import os

city_list = ["austin", "columbus", "denver", "miami", "minneapolis", "portland", "seattle", "vancouver", "montreal"]
download_interval = 2     # in minutes

def write_locations():
    for city in city_list:
        baseurl = 'https://www.car2go.com/api/v2.1/vehicles?loc=' + city + '&oauth_consumer_key=TransitShare&format=json'
        page = urllib2.urlopen(baseurl)
        information = page.read()
        fname = time.strftime("%m_%d_%Y_%H_%M_%S")
        save_path = "D:/Car2Go/" + city
        fname = os.path.join(save_path, time.strftime("%m_%d_%Y_%H_%M_%S"))
        with open(fname + '.json', 'w') as f:
            f.write(information)

while True:
    time.sleep(60*download_interval)
    write_locations()