#!/usr/bin/python3
"""Module to query Reddit API for total subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return total subscribers for subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python3:api.advanced:v1.0 (by /u/api_advanced)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
