# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests

# username = "apoorv@gmail.com", password = "Test 12_44"
def invalid_credentials(test_input):

    username = test_input[0]
    password = test_input[1]

    base_url = "https://api.shipt.com/auth/v2/oauth/token?white_label_key=shipt"

    headers={
        'X-User-Type' : 'Customer',
        'Content-Type' : 'application/x-www-form-urlencoded'
    }

    data_invalid = {
        "username" : username,
        "password": password,
        "grant_type" : "password"
    }

    param_shipt = {
        "white_label_key" : "shipt"
    }

    response = requests.post(base_url, headers=headers, params = param_shipt, data=data_invalid)

    print("Response : ", response.text)

    #print(response.text)

    if response.status_code == 401:
        return response.json()['error']['message']