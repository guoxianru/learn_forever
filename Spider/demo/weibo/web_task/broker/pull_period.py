from .pull_task import PullTask
import json


class PullPeriod(PullTask):

    def __init__(self, _conf):
        PullTask.__init__(self, _conf, 'period')

    def parse(self, _datum):
        del _datum['id']
        item={
            'id':_datum['unique_id'],
            'session': self.session,
            'proj':self.proj,
            'app':self.app,
            'task':_datum['task'],
            'begin_time':_datum['begin_time'],
            'end_time': _datum['end_time'],
            'data':json.dumps(_datum, ensure_ascii=False),
        }
        return item
