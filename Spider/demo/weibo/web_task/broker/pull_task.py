import hashlib
import time
from abc import ABCMeta, abstractmethod
import logging
from .pull import pull
import pymysql
import os
import sys

if not os.path.exists('log'):
    os.mkdir(os.path.join(os.getcwd(), 'log'))


class PullTask(metaclass=ABCMeta):
    DEFAULT_COUNT = 20

    def __init__(self, _conf, _type):
        self.type = _type
        self.mysql = _conf['mysql']
        self.api = _conf['api']
        self.db = None
        self.session = None
        self.data = []

    def __open_log(self):
        self.extra = {
            'project': self.proj,
            'app': self.app,
            'type': self.type
        }
        log_flag = str(self.__class__.__name__).lower()
        log_name = os.path.join(os.getcwd(), 'log/' + log_flag + '.log')
        log_formatter = logging.Formatter(
            "%(asctime)s, %(levelname)s, %(process)d, %(project)s, %(app)s, %(type)s, %(message)s")
        self.handler = logging.FileHandler(filename=log_name)
        self.handler.setFormatter(log_formatter)
        self.logger = logging.getLogger(log_flag)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.handler)

    def __close_log(self):
        self.logger.removeHandler(self.handler)
        self.handler.close()

    def __pull(self, _last_id=0):
        last_max_id = _last_id
        self.data.clear()
        while True:
            params = {
                'proj': self.proj,
                'app': self.app,
                'type': self.type,
                'last_max_id': last_max_id,
                'count': PullTask.DEFAULT_COUNT,
            }
            data = pull(params, self.api.pull())
            count = len(data)
            if count:
                last_max_id = data[-1]['id']
                self.data.extend(data)
            else:
                break

        self.logger.info('pull %s data' % (len(self.data),), extra=self.extra)
        return len(self.data)

    def __insert_db(self, _item):
        affected = 0
        if self.db:
            keys = _item.keys()
            fields = ','.join(keys)
            values = ','.join(['%(' + v + ')s' for v in keys])
            sql = "insert into %s(%s) values(%s)" % (self.type, fields, values)
            affected = 0
            try:
                cursor = self.db.cursor()
                affected = cursor.execute(sql, _item)
                self.db.commit()
                self.logger.info(repr(_item), extra=self.extra)
            except Exception as e:
                file = os.path.basename(__file__)
                line = str(sys._getframe().f_lineno)
                error = repr(e)
                msg = "[%s %s %s]" % (file, line, error)
                self.logger.error(msg.replace(',', '.'), extra=self.extra)
        return affected

    def __open_db(self):
        try:
            self.db = pymysql.connect(
                host=self.mysql['host'],
                user=self.mysql['user'],
                password=self.mysql['password'],
                database=self.mysql['database'],
                charset=self.mysql['charset'])
        except Exception as e:
            file = os.path.basename(__file__)
            line = str(sys._getframe().f_lineno)
            error = repr(e)
            msg = "[%s %s %s]" % (file, line, error)
            self.logger.error(msg.replace(',', '.'), extra=self.extra)

    def __close_db(self):
        if self.db:
            self.db.close()

    def _generate_session(self):
        sign = "%s-%s-%s-%s" % (self.proj, self.app, self.type, time.time())
        self.session = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()

    def run(self, _proj, _app, _last_id=0):
        self.proj = _proj
        self.app = _app
        finished_count = 0
        self._generate_session()
        self.__open_log()
        try:
            if self.__pull(_last_id) > 0:
                self.logger.info('start insert', extra=self.extra)
                self.__open_db()
                finished_count = 0
                for datum in self.data:
                    item = self.parse(datum)
                    finished_count += self.__insert_db(item)
                self.__close_db()
                self.logger.info('finish insert :' + str(finished_count) + ' data ', extra=self.extra)

        except Exception as e:
            file = os.path.basename(__file__)
            line = str(sys._getframe().f_lineno)
            error = repr(e)
            msg = "[%s %s %s]" % (file, line, error)
            self.logger.error(msg.replace(',', '.'), extra=self.extra)
        finally:
            self.__close_log()
        return self.session, finished_count

    @abstractmethod
    def parse(self, _datum):
        pass
