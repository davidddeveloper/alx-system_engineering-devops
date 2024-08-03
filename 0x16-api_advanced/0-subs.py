#!/usr/bin/python3
"""A python scripts that consume the reddit api
to count the number of subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ subscribers count """

    endpoint = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except Exception:
        return 0
