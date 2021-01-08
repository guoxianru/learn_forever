# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    文字识别图片中表格内容
"""


def form_aliyunapi(img_path):
    """
    阿里云API识别(表格识别)
    APPCODE：应用密钥
    """
    from json import dumps
    from requests import post
    from base64 import b64decode, b64encode

    APPCODE = ""
    try:
        img_base64 = b64encode(open(img_path, "rb").read()).decode("ascii")
        url = "https://form.market.alicloudapi.com/api/predict/ocr_table_parse"
        old_format = False
        config = {"format": "xlsx", "finance": False, "dir_assure": False}
        if not old_format:
            param = {}
            param["image"] = img_base64
            if config is not None:
                param["configure"] = dumps(config)
            data = dumps(param)
        else:
            param = {}
            pic = {}
            pic["dataType"] = 50
            pic["dataValue"] = img_base64
            param["image"] = pic
            if config is not None:
                conf = {}
                conf["dataType"] = 50
                conf["dataValue"] = dumps(config)
                param["configure"] = conf
            inputs = {"inputs": [param]}
            data = dumps(inputs)
        headers = {
            "Authorization": "APPCODE %s" % APPCODE,
            "Content-Type": "application/json; charset=UTF-8",
        }
        response = post(url=url, headers=headers, data=data)
        if response.status_code == 200:
            if old_format:
                result = response.json()["outputs"][0]["outputValue"]["dataValue"]
            else:
                result = response.json()
            table = b64decode(result["tables"])
            with open("test.xlsx", "wb") as f:
                f.write(table)
    except Exception as e:
        print(e)


def form_txapi(img_path):
    """
    腾讯智能云API识别(表格识别)
    SecretId：应用ID
    SecretKey：应用KEY
    pip install tencentcloud-sdk-python
    """
    from json import loads
    from base64 import b64encode, b64decode
    from tencentcloud.common import credential
    from tencentcloud.common.profile.client_profile import ClientProfile
    from tencentcloud.common.profile.http_profile import HttpProfile
    from tencentcloud.ocr.v20181119 import ocr_client, models

    SecretId = ""
    SecretKey = ""
    try:
        img_base64 = b64encode(open(img_path, "rb").read()).decode("ascii")
        cred = credential.Credential(SecretId, SecretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)
        req = models.TableOCRRequest()
        params = '{"ImageBase64":"%s"}' % str(img_base64)
        req.from_json_string(params)
        resp = client.TableOCR(req)
        table = b64decode(loads(resp.to_json_string())["Data"])
        with open("test.xlsx", "wb") as f:
            f.write(table)
    except Exception as e:
        print(e)


def form_baiduapi(img_path):
    """
    百度智能云API识别(表格识别)
    APP_ID：百度智能云应用ID
    API_KEY：百度智能云应用KEY
    SECRET_KEY：百度智能云应用密钥
    pip install baidu-aip
    """
    import time
    from aip import AipOcr
    from requests import get

    APP_ID = ""
    API_KEY = ""
    SECRET_KEY = ""
    try:
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        image = open(img_path, "rb").read()
        response = client.tableRecognition(image, {"result_type": "excel"})
        time.sleep(20)
        excel_url = response["result"]["result_data"]
        excel = get(excel_url)
        with open("test.xls", "wb") as f:
            f.write(excel.content)
    except Exception as e:
        print(e)
