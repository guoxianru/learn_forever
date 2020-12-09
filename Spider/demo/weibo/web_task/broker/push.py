import requests
import json
import time

def push(_params, _url):
    headers = {
        'Content-Type': 'application/json'
    }
    for _ in range(5):
        res = requests.post(_url, headers=headers, data=json.dumps(_params))
        time.sleep(0.2)
        if res.status_code == 200 and json.loads(res.text).get('code') == 0:
            return True
        else:
            return False
