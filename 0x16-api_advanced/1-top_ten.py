#!/usr/bin/python3
"""
    queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit

"""
import requests


def top_ten(subreddit):
    """ retrive the top 10 hot post """
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(endpoint, allow_redirects=False)
    try:
        data = response.json()

        counter = 0
        for post in data['data']['children']:
            if counter == 10:
                break

            print(post.title)
            counter += 1
    except Exception:
        print(None)
