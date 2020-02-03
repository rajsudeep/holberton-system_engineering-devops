#!/usr/bin/python3
""" Finds employee information """
from requests import get
from sys import argv


def get_employee_info(url, user_id):
    """ Print completed tasks of corresponding employee """
    user = get(url + 'users/' + user_id).json()
    user_name = user['name']

    todos = get(url + 'todos?userId={}'.format(user_id)).json()
    completed_todos = [task for task in todos if task.get('completed')]

    info = 'Employee {} is done with tasks({}/{}):'.format(
        user_name, len(completed_todos), len(todos))
    print(info)
    for task in completed_todos:
        print('\t ' + task.get('title'))


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    get_employee_info(url, user_id)
