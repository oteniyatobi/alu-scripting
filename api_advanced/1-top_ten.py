#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    if not posts:
        print(None)
        return
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
        