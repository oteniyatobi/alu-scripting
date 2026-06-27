#!/usr/bin/python3
"""Module to recursively query Reddit API for all hot article titles."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return list of all hot article titles for subreddit, or None."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/oteniyatobi)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    posts = data.get("children", [])
    if not posts:
        return hot_list if hot_list else None
    hot_list += [post.get("data", {}).get("title") for post in posts]
    next_after = data.get("after")
    if next_after is None:
        return hot_list
    return recurse(subreddit, hot_list, next_after)
