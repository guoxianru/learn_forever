# _*_ coding:utf-8 _*_
"""
author:files
contact: wp_byy@163.com
datetime:2020/10/21 5:33 下午
software: PyCharm
文件说明：
test_pull() 获取任务到数据库
task_main() 执行任务并上传到服务器
"""
import os
import json
import datetime
from broker.job_conf import jobs
from broker.test_broker import map_active, map_passive
from broker.read_period import ReadPeriod
from broker.push_period import PushPeriod
from broker.update_period import UpdatePeriod
from broker.test_broker import test_pull

from core.tools import get_today_file_name, conf,write_error_txt
from core.excute_task_classify import excute_active, excute_passive
from core.kuaishou import kuaishou_task

def push_job(proj, app, task_type, active_json_data):
    push = PushPeriod(conf)
    rep = push.run(proj, app, task_type, active_json_data)
    return rep


def update_job(proj, app, task_type, active_json_data):
    update = UpdatePeriod(conf)
    rep = update.run(proj, app, task_type, active_json_data)
    return rep


def map_task(_job, _task, _mode):
    if 'passive' == _mode:
        return map_passive(_job, _task, _mode)
    elif 'active' == _mode:
        return map_active(_job, _task, _mode)
    else:
        print('wrong mode ' + _mode)
        exit(0)


def do_job(_job_map, _conf, proj, app):
    active_task_count = 0
    passive_task_count = {
        "comment": 0,
        "digg": 0,
        "share": 0,
    }
    file_name = get_today_file_name(proj, app)
    for task in _job_map:
        if task not in _conf.keys():
            print('unregisted task ' + task)
            exit(0)
        data = map_task(_job_map[task], task, _conf[task])

        if app == 'kuaishou':
            kuaishou_task(data,file_name,app)
            continue

        for url, value in data.items():

            # if '/u/' in url or url == '':
            if 'https://weibo.com/' not in url and 'https://m.weibo.cn/' not in url or '/u/' in url:
                write_error_txt(file_name,value)
                print(url)
                continue

            if value['mode'] == 'passive':
                # continue
                # 被动任务
                new_task_data, task_type = excute_passive(url, value, file_name,app)
                flag_passive_data = push_job(proj, app, task_type, new_task_data)

                passive_task_count[task_type] += len(new_task_data)
                # for flag in flag_passive_data:
                #     if flag.get("response"):
                #         passive_task_count[task_type] += len(new_task_data)

                # print(f'push_job {task_type} result:', flag_passive_data)
                # print(f'update_job {task_type} result:',update_job(proj, app, task_type, new_task_data))

            elif value['mode'] == 'active':
                # continue
                # 主动任务
                active_json_data, task_type = excute_active(url, value,file_name)
                flag_active_data = push_job(proj, app, task_type, active_json_data)
                for flag in flag_active_data:
                    if flag.get("response"):
                        active_task_count += 1
                        print(f'已上报{active_task_count}条,push_job {task_type} result:', flag_active_data)

                # flag = update_job(proj, app, task_type, active_json_data)
                # print(f'update_job {task_type} result:',flag)
            else:
                raise
    print(f'---------原创(主动)任务审核通过{active_task_count}条')
    print(f'---------互动(被动)任务审核通过{passive_task_count}条')


def task_main():
    task = ReadPeriod(conf)
    task.open_db()
    print('configure', jobs)
    for job in jobs:
        data = task.get(job['proj'], job['app'])

        file_name = get_today_file_name(job['proj'], job['app'])
        if not os.path.exists('log/'+file_name):
            os.mkdir(os.path.join(os.getcwd(),'log', file_name))

        print('total', len(data))
        job_map = {}
        for datum in data:
            if datum['task'] not in job_map.keys():
                job_map[datum['task']] = []
            job_map[datum['task']].append(datum)
        do_job(job_map, job['task'], job['proj'], job['app'])
    task.close_db()


if __name__ == '__main__':
    # 拉取任务
    test_pull()

    # 执行任务
    task_main()
