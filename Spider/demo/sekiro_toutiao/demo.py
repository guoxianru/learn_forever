import requests

data = {
    "group": "ws-group-sekiro_toutiao",
    "action": "toutiao_decode",
    "decode_str": "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1852FA0C573622&cp=5F05E356F2C20E1",
}
res = requests.post("https://sekiro.virjar.com/invoke", data=data)
print(res.json()["data"])
print(res.text)