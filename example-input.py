#!/usr/env/bin python

import json
import requests, time

DEVICE_ID = ''
ACCESS_TOKEN = ''

#
deviceId = DEVICE_ID
littleBitsInputUrl = "https://api-http.littlebitscloud.cc/v3/devices/" + deviceId + "/input"
authToken = ACCESS_TOKEN

#
headers = { "Authorization": "Bearer " + authToken }
r = requests.get(littleBitsInputUrl, headers=headers, stream=True)

#
for line in r.iter_lines():
    if line:
        result = json.loads(line.split('data:')[1])
        print result['payload']