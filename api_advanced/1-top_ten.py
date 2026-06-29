#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/oteniyatobi)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    try:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
    except ValueError:
        print(None)