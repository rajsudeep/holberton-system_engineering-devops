#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a subreddit """
    headers = {'User-Agent': 'Unix'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers).json().get('data')
    if response:
        return response.get('subscribers')
    return 0
