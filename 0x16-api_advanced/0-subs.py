#!/usr/bin/python3
"""A python scripts that consume the reddit api
to count the number of subscribers of a subreddit"""
import praw


client_id = '34s4jgg_lvfFbwwAF2-LmA'
client_secret = 'F1nH_e_TAMQs5TjF_De0KcBvhEsQcQ'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent

        )


def get_subreddit_count(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    subscribers = subreddit.subscribers
    return subscribers
