#!/usr/bin/python3
""" Finds employee information """
from requests import get
from sys import argv
import json


def get_all(url):
    """ Print completed tasks of all employees """
    users = get(url + 'users/').json()
    todos = get(url + 'todos/').json()

    dict_tasks = {}
    for user in users:
        tasks = []
        for task in todos:
            if user['id'] == task['userId']:
                task_info = {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': user['username'],
                }
                tasks.append(task_info)
        dict_tasks[user['id']] = tasks
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dict_tasks, f)


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    get_all(url)
