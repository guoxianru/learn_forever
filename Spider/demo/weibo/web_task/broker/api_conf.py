import hashlib
import time
from urllib.parse import urljoin

DEBUG = False
if DEBUG:
    APP_ID = 'domino081'
    APP_SECRET = 'h73h56sb12u7s3p'
    host = 'http://test-v10.alpha-car.cn'

else:
    APP_ID = 'domino081'
    APP_SECRET = 'jhgs78bc43si9fcz3qapujf5cv41'
    host = 'http://v10.alpha-car.cn'


def get_token():
    t_s = str(time.time()).split('.')[0]
    sha1 = hashlib.sha1()
    sha1.update((APP_ID + APP_SECRET + str(t_s)).encode('utf-8'))
    token = sha1.hexdigest()
    return token, t_s


class api:
    @staticmethod
    def pull():
        token, t_s = get_token()
        return urljoin(host, '/opens/domino-tasks' + '?' + 'token=' + token + '&app_id=' + APP_ID + '&timestamp=' + t_s)

    @staticmethod
    def push():
        token, t_s = get_token()
        return urljoin(host, '/opens/domino-data' + '?' + 'token=' + token + '&app_id=' + APP_ID + '&timestamp=' + t_s)
