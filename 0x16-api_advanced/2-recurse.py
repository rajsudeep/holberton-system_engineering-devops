#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Returns a list containing the titles of all hot articles """
    headers = {'User-Agent': ''}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?=after={}'.format(after)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return
    posts_x = response.json()
    posts = posts_x['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    posts_after = posts_x['data']['after']
    if posts_after:
        return recurse(subreddit, hot_list=hot_list, after=posts_after)
    else:
        return hot_list
