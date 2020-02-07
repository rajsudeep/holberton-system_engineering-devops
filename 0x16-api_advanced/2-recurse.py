#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Returns a list of hot titles """
    headers = {'User-Agent': ''}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    try:
        response = requests.get(url, headers=headers).json().get('data')
        for post in response.get('children'):
            hot_list.append(post.get('data').get('title'))
        after = response.get('after')
        recurse(subreddit, hot_list, after)
        return hot_list
    except:
        return None
