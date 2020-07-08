"""
docker run -d -p 5600:5600 -p 5601:5601 -p 5602:5602 -p 5603:5603 --name sekiro-server registry.cn-beijing.aliyuncs.com/virjar/sekiro-server:latest
"""

import requests

data = {
    "group": "ws-group-sekiro_toutiao",
    "action": "toutiao_decode",
    "decode_str": "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1852FA0C573622&cp=5F05E356F2C20E1",
}
# res = requests.post("https://sekiro.virjar.com/invoke", data=data)
res = requests.post("http://47.94.245.242:5602/invoke", data=data)
print(res.json()["data"])
