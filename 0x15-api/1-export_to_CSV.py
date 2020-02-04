#!/usr/bin/python3
""" Finds employee information """
from requests import get
from sys import argv
import csv


def get_employee_info_csv(url, user_id):
    """ Print completed tasks of corresponding employee """
    user = get(url + 'users/' + user_id).json()
    user_name = user.get('username')
    todos = get(url + 'todos?userId={}'.format(user_id)).json()

    try:
        with open('{}.csv'.format(user_id), mode='w') as f:
            write = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in todos:
                write.writerow([
                    user_id,
                    user_name,
                    task.get('completed'),
                    task.get('title'),
                ])
    except IOError:
        print("I/O error")


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    get_employee_info_csv(url, user_id)
