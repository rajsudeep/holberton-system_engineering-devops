#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a subreddit """
    headers = {'User-Agent': ''}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=headers).json().get('data')
        return response.get('subscribers')
    except:
        return 0
