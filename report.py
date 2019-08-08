# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:21:04 2018

@author: Frank_Huang
"""

import re
import json
import requests
import time

MAILCHIMP_API_KEY           = "663fdc63a6218103ee1b89f089c8d84e-us14"
MAILCHIMP_DATA_CENTER       = 'us14'
MAILCHIMP_EMAIL_LIST_ID     = '6c74528ac7'


#endpoint='https://us14.api.mailchimp.com/3.0/reports' 
endpoint='https://us14.api.mailchimp.com/3.0/campaign-folders'
#endpoint='https://us14.api.mailchimp.com/3.0/reports?offset=0&count=100'
#print(endpoint)
r = endpoint+'?count=100&offset='+str(offset), auth=("", MAILCHIMP_API_KEY)
print(r)
offset=0
i=0
gonext=True
"""
while gonext:
    r = requests.get(endpoint+'?count=100&offset='+str(offset), auth=("", MAILCHIMP_API_KEY))
    #print(r.status_code)
    #print(len(r.text))
    #print(r.json())
    if(len(r.text)>800):
        #with open('mailchimp/reports'+str(i)+'.json', 'w') as outfile:
        with open('mailchimp/campaign-folders'+str(i)+'.json', 'w') as outfile:
            json.dump(r.json(), outfile)
    else:
        gonext=False
    i+=1
    offset+=100
    time.sleep(0.3)
    #print(offset)
"""