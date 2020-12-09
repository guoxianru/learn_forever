import time

import logging
from .push import push

import os
import sys

if not os.path.exists('log'):
    os.mkdir(os.path.join(os.getcwd(), 'log'))


class PushPeriod():

    def __init__(self, _conf):
        self.api = _conf['api']
        self.db = None
        self.data = []

    def __open_log(self):
        self.extra = {
            'project': self.proj,
            'app': self.app,
            'task': self.task
        }
        log_flag = str(self.__class__.__name__).lower()
        log_name = os.path.join(os.getcwd(), 'log/' + log_flag + '.log')
        log_formatter = logging.Formatter(
            "%(asctime)s, %(levelname)s, %(process)d, %(project)s, %(app)s, %(task)s, %(message)s")
        self.handler = logging.FileHandler(filename=log_name)
        self.handler.setFormatter(log_formatter)
        self.logger = logging.getLogger(log_flag)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.handler)

    def __close_log(self):
        self.logger.removeHandler(self.handler)
        self.handler.close()

    def _push_result(self, _data):
        result = []
        for datum in _data:
            params = {
                'proj': self.proj,
                'app': self.app,
                'task': self.task,
                'data': datum
            }
            response = push(params, self.api.push())
            params['response'] = response
            result.append(params)
            self.logger.info('push %s' % (repr(response),), extra=self.extra)
        return result

    def run(self, _proj,_app,_task,_data):
        self.proj = _proj
        self.app = _app
        self.task = _task
        self.__open_log()
        response = []
        try:
            response = self._push_result(_data)
        except Exception as e:
            file = os.path.basename(__file__)
            line = str(sys._getframe().f_lineno)
            error = repr(e)
            msg = "[%s %s %s]" % (file, line, error)
            self.logger.error(msg.replace(',', '.'), extra=self.extra)
        finally:
            self.__close_log()
            return response
