import hashlib
import time
import os
import sys
import copy
import json
import pymysql
from broker.api_conf import api
from broker.mysql_conf import mysql
from broker.job_conf import jobs

conf = {
    'api': api,
    'mysql': mysql
}
from broker.pull_period import PullPeriod
from broker.read_period import ReadPeriod
from broker.push_period import PushPeriod
from broker.update_period import UpdatePeriod


def test_pull():
    pull = PullPeriod(conf)
    for job in jobs:
        count, session = pull.run(job['proj'], job['app'])
        print(job['proj'], job['app'], session, count)


def test_main():
    task = ReadPeriod(conf)
    task.open_db()
    print('configure',jobs)
    for job in jobs:
        data = task.get(job['proj'], job['app'])
        print('total', len(data))
        job_map = {}
        for datum in data:
            if datum['task'] not in job_map.keys():
                job_map[datum['task']] = []
            job_map[datum['task']].append(datum)
        do_job(job_map, job['task'])
    task.close_db()


def do_job(_job_map, _conf):
    for task in _job_map:
        if task not in _conf.keys():
            print('unregisted task ' + task)
            exit(0)
        data=map_task(_job_map[task], task, _conf[task])
        #######
        print(data)

def map_task(_job, _task, _mode):
    if 'passive' == _mode:
        return map_passive(_job, _task, _mode)
    elif 'active' == _mode:
        return map_active(_job)
    else:
        print('wrong mode ' + _mode)
        exit(0)


def map_passive(_job, _task, _mode):
    maped_job = {}
    for item in _job:
        data = json.loads(item["data"], encoding="utf-8")
        # print(data)
        if data['link'] not in maped_job.keys():
            maped_job[data['link']] = {
                'task': _task,
                'mode': _mode,
                'data': []
            }
        maped_job[data['link']]['data'].append(data)
    return maped_job


def map_active(_job, _task, _mode):
    maped_job = {}
    for item in _job:
        data = json.loads(item["data"], encoding="utf-8")
        # print(data)
        if data['staff_link'] not in maped_job.keys():
            maped_job[data['staff_link']] = {
                'task': _task,
                'mode': _mode,
                'data': []
            }
        maped_job[data['staff_link']]['data'].append(data)

    return maped_job



def test_push():
    fp = open('broker/comment_result.json', 'r')
    data = json.load(fp, encoding='utf-8')
    print(data)
    fp.close()
    push=PushPeriod(conf)
    rep=push.run('benteng_2','weibo','comment',data)
    print(rep)


def update_job():
    fp = open('broker/comment_result.json', 'r')
    data = json.load(fp, encoding='utf-8')
    print(data)
    fp.close()
    update=UpdatePeriod(conf)
    rep=update.run('benteng_2','weibo','comment',data)
    print(rep)

if __name__ == '__main__':

    test_pull()
    # test_main()
    test_push()
    #update_job()

