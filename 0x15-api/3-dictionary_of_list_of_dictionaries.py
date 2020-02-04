#!/usr/bin/python3
""" Finds employee information """
from requests import get
from sys import argv
import json


def get_all(url):
    """ Print completed tasks of corresponding employee """
    users = get(url + 'users/').json()
    todos = get(url + 'todos/').json()

    dict_tasks = {}
    for user in users:
        tasks = []
        for task in todos:
            task_info = {
                'username': user['username'],
                'completed': task['completed'],
                'task': task['title'],
            }
            tasks.append(task_info)
        dict_tasks[user['id']] = tasks
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dict_tasks, f)


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    get_all(url)
