#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Returns a list of hot titles """
    h = {'User-Agent': ''}
    p = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    try:
        response = requests.get(url, headers=h, params=p).json().get('data')
        for post in response.get('children'):
            hot_list.append(post.get('data').get('title'))
        if response.get('after') is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, response.get('after'))
    except:
        return None
