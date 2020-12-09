import copy
import logging
import pymysql
import os
import sys

if not os.path.exists('log'):
    os.mkdir(os.path.join(os.getcwd(), 'log'))


class UpdatePeriod():

    def __init__(self, _conf):
        self.mysql = _conf['mysql']
        self.db = None

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

    def _build_update_sqls(self, _tab, _unique_ids):
        sqls = []
        for unique_id in _unique_ids:
            sqls.append("update %s set status=1 where  data->'$.unique_id' ='%s'" % (_tab, unique_id))
        return sqls

    def _write_trans(self, _sqls):
        if self.db:
            cursor = self.db.cursor()
            try:
                for sql in _sqls:
                    cursor.execute(sql)
                self.db.commit()
                return True
            except Exception as e:
                self.db.rollback()
                file = os.path.basename(__file__)
                line = str(sys._getframe().f_lineno)
                error = repr(e)
                msg = "[%s %s %s]" % (file, line, error)
                self.logger.error(msg.replace(',', '.'), extra=self.extra)
                return False
            finally:
                cursor.close()
        else:
            return False

    def trim_unique_id(self, _data):
        unique_ids = [x['unique_id'] for x in _data]
        return unique_ids

    def run(self, _proj, _app, _task, _data):
        self.proj = _proj
        self.app = _app
        self.task = _task
        result = False
        self.__open_log()
        try:
            self.__open_db()
            sqls = self._build_update_sqls('period', self.trim_unique_id(_data))
            if len(sqls):
                if self._write_trans(sqls):
                    for datum in _data:
                        self.logger.info('success for ' + repr(datum).replace(',', '.'), extra=self.extra)
                    result = True

        except Exception as e:
            file = os.path.basename(__file__)
            line = str(sys._getframe().f_lineno)
            error = repr(e)
            msg = "[%s %s %s]" % (file, line, error)
            self.logger.error(msg.replace(',', '.'), extra=self.extra)
        finally:
            self.__close_db()
            self.__close_log()
        return result
