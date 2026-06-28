#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for subreddit, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3:alu-api:v1.0 (by /u/oteniyatobi)"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data").get("children")
    for post in posts[:10]:
        print(post.get("data").get("title"))
