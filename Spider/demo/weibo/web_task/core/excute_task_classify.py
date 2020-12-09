# _*_ coding:utf-8 _*_
"""
author:files
contact: wp_byy@163.com
datetime:2020/10/23 12:58 下午
software: PyCharm
文件说明：任务进行细分，执行。
"""
from core.comment_name_list import CommentNameList
from core.share_and_digg_name_list import PassivityTask
from core.weibo_active_counts import AtiveTask
from core.tools import compare_data,write_error_txt


def excute_passive(url, value, file_name,app):
    user_list = []

    if value['task'] == 'comment':
        if app == 'weibo':
            user_list = CommentNameList(url).run()
        elif app == 'kuaishou':
            print('kuaishou comment')
            use_list = []

    elif value['task'] == 'share':
        if app == 'weibo':
            user_list = PassivityTask(url, value['task']).run()
        elif app == 'kuaishou':
            pass

    elif value['task'] == 'digg':
        if app == 'weibo':
            user_list = PassivityTask(url, value['task']).run()
        elif app == 'kuaishou':
            pass

    else:
        print(f"new task type:{value['task']}")

    new_task_data = compare_data(value['data'], user_list, url, value['task'], file_name)
    print(f"crawl {value['task']} {url}")
    print(f"----------{value['task']}任务有:{len(value['data'])}条,审核通过{len(new_task_data)}条")
    return new_task_data, value['task']


def excute_active(url, value,file_name):
    data_list = []
    task_type = ''
    for value_data in value['data']:
        if value['task'] == 'original_image_text':
            task_type = value['task']
            user_counts_data = AtiveTask(url).run()
            # user_counts_data = AtiveTask(url).extend_run()

        elif value['task'] == 'original_article':
            task_type = value['task']
            user_counts_data = AtiveTask(url).run()

        else:
            print(f"new task type:{value['task']}")
            user_counts_data = {}

        if not user_counts_data:
            print('error', url, value)
            write_error_txt(file_name, value)
            continue
            # raise

        value_data.update(user_counts_data)
        data_list.append(value_data)
    return data_list, task_type


if __name__ == '__main__':
    pass
