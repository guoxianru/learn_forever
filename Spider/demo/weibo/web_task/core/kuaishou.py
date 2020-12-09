from core.excute_task_classify import excute_active, excute_passive



def kuaishou_task(data,file_name,app):
    for url, value in data.items():
        print(url,value)

        if value['mode'] == 'passive':
            new_task_data, task_type = excute_passive(url, value, file_name,app)
            print(new_task_data,task_type)
            pass

        elif value['mode'] == 'active':
            print('-'*50)
            pass
        else:
            raise

        break