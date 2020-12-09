import json
import requests


def pull(_params, _url):
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.post(_url, headers=headers, data=json.dumps(_params))
    if res.status_code == 200 and json.loads(res.text).get('code') == 0:
        data = json.loads(res.text, encoding='utf-8')
        return data['data'] if data['data'] else []
    else:
        return []
