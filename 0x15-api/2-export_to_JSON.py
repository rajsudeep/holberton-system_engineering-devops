#!/usr/bin/python3
""" Finds employee information """
from requests import get
from sys import argv
import json


def get_employee_info_json(url, user_id):
    """ Print completed tasks of corresponding employee """
    user = get(url + 'users/' + user_id).json()
    user_name = user['name']
    todos = get(url + 'todos?userId={}'.format(user_id)).json()

    tasks = []
    for task in todos:
        task_info = {
            'username': user_name,
            'completed': task['completed'],
            'task': task['title'],
        }
        tasks.append(task_info)
    dict_tasks = {user_id: tasks}
    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(dict_tasks, f)


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    get_employee_info_json(url, user_id)
