# -*- coding: utf-8 -*-
# -*- author: GXR -*-

"""
    文字识别图像验证码方法
"""


def verifiy_liangzhong():
    """
    图像验证码联众识别
    同级目录下保存验证码图片：yzm.png
    api_username：联众账号
    api_password：联众密码
    api_post_url：联众接口
    yzm_type：验证码类型
    返回格式：验证码内容(字符串)
    """
    import json
    import requests

    api_username = ("",)
    api_password = ""
    file_name = "yzm.png"
    api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
    yzm_min = ""
    yzm_max = ""
    yzm_type = "1013"
    tools_token = ""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Connection": "keep-alive",
        "Host": "v1-http-api.jsdama.com",
        "Upgrade-Insecure-Requests": "1",
    }
    files = {"upload": (file_name, open(file_name, "rb"), "image/png")}
    data = {
        "user_name": api_username,
        "user_pw": api_password,
        "yzm_minlen": yzm_min,
        "yzm_maxlen": yzm_max,
        "yzmtype_mark": yzm_type,
        "zztool_token": tools_token,
    }
    s = requests.session()
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    try:
        verifiy_code = json.loads(r.text)["data"]["val"]
    except:
        verifiy_code = ""

    return verifiy_code


def verifiy_baiduapi():
    """
    图像验证码百度智能云API识别(调用通用文字识别（高精度版）)
    同级目录下保存验证码图片：yzm.png
    APP_ID：百度智能云应用ID
    API_KEY：百度智能云应用KEY
    SECRET_KEY：百度智能云应用密钥
    返回格式：验证码内容(字符串)
    pip install baidu-aip
    """
    from aip import AipOcr

    try:
        APP_ID = ""
        API_KEY = ""
        SECRET_KEY = ""
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content("yzm.png")
        client.basicAccurate(image)
        options = {}
        # 是否检测图像朝向(非必选,string):true,false
        options["detect_direction"] = "false"
        # 是否返回识别结果中每一行的置信度(非必选,string):true,false
        options["probability"] = "true"
        res = client.basicAccurate(image, options)
        verifiy_code = res["words_result"][0]["words"]
    except:
        verifiy_code = ""

    return verifiy_code


def verifiy_tesserocr():
    """
    图像验证码OCR识别
    安装：tesseract、pip install tesserocr
    同级目录下保存验证码图片：yzm.png
    返回格式：验证码内容(字符串)
    """
    import tesserocr
    from PIL import Image

    def binarizing(img, threshold):
        """传入image对象进行灰度、二值处理"""
        # 转灰度,传入参数'L'
        img = img.convert("L")
        pixdata = img.load()
        w, h = img.size
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        # 返回处理后图片对象
        return img

    def depoint(img):
        """传入二值化后的图片进行降噪处理"""
        pixdata = img.load()
        w, h = img.size
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                count = 0
                # 上
                if pixdata[x, y - 1] > 245:
                    count = count + 1
                # 下
                if pixdata[x, y + 1] > 245:
                    count = count + 1
                # 左
                if pixdata[x - 1, y] > 245:
                    count = count + 1
                # 右
                if pixdata[x + 1, y] > 245:
                    count = count + 1
                # 左上
                if pixdata[x - 1, y - 1] > 245:
                    count = count + 1
                # 左下
                if pixdata[x - 1, y + 1] > 245:
                    count = count + 1
                # 右上
                if pixdata[x + 1, y - 1] > 245:
                    count = count + 1
                # 右下
                if pixdata[x + 1, y + 1] > 245:
                    count = count + 1
                if count > 4:
                    pixdata[x, y] = 255
        # 返回处理后图片对象
        return img

    # 传入图片生成图片对象
    img = Image.open("yzm.png")
    # 进行灰度、二值处理,二值范围参数:threshold
    img = binarizing(img, 200)
    # 进行降噪处理
    img = depoint(img)
    # # 打开图片
    # img.show()
    verifiy_code = tesserocr.image_to_text(img)
    # 返回识别结果
    return verifiy_code
