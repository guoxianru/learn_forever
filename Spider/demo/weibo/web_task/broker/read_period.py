import logging
import os
import sys

import pymysql

if not os.path.exists('log'):
    os.mkdir(os.path.join(os.getcwd(), 'log'))


class ReadPeriod():
    def __init__(self, _conf):
        self.logger = None
        self.mysql = _conf['mysql']
        self.db = None
        self.data = {}

    def __open_log(self):
        self.extra = {
            'project': self.proj,
            'app': self.app,
        }
        log_flag = str(self.__class__.__name__).lower()
        log_name = os.path.join(os.getcwd(), 'log/' + log_flag + '.log')
        log_formatter = logging.Formatter(
            "%(asctime)s, %(levelname)s, %(process)d, %(project)s, %(app)s, %(message)s")
        self.handler = logging.FileHandler(filename=log_name)
        self.handler.setFormatter(log_formatter)
        self.logger = logging.getLogger(log_flag)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.handler)

    def __close_log(self):
        self.logger.removeHandler(self.handler)
        self.handler.close()

    def get(self, _proj, _app):
        self.proj = _proj
        self.app = _app
        self.__open_log()
        data = self.__read_fresh_data()
        self.__close_log()
        return data

    def __read_data(self, _sql):
        if self.db:
            cursor = self.db.cursor(pymysql.cursors.DictCursor)
            try:
                res = cursor.execute(_sql)
                data = cursor.fetchall()
                return list(data)
            except Exception as e:
                file = os.path.basename(__file__)
                line = str(sys._getframe().f_lineno)
                error = repr(e)
                msg = "[%s %s %s]" % (file, line, error)
                self.logger.error(msg.replace(',', '.'), extra=self.extra)
                return []
            finally:
                cursor.close()
        else:
            return []

    def __read_fresh_data(self):
        sql = "SELECT id,task,data FROM period WHERE proj='%s' AND app='%s' AND created_at < NOW() and  begin_time<=now() and end_time >now() and STATUS=0 ORDER BY created_at" % (
            self.proj, self.app)
        data = self.__read_data(sql)
        self.logger.info("read %d fresh data" % (len(data),), extra=self.extra)
        return data

    def open_db(self):
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

    def close_db(self):
        if self.db:
            self.db.close()
