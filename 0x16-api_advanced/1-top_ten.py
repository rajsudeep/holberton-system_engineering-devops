#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def top_ten(subreddit):
    """ Print the titles of the first 10 hot posts """
    headers = {'User-Agent': ''}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    try:
        response = requests.get(url, headers=headers).json().get('data')
        for post in response.get('children'):
            print(post.get('data').get('title'))
    except:
        print(None)
