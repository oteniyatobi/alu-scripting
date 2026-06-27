#!/usr/bin/python3
"""Module to count keywords in Reddit hot article titles recursively."""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Print sorted count of keywords from all hot article titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            w = word.lower()
            if w not in counts:
                counts[w] = 0
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/oteniyatobi)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        title_words = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            w = word.lower()
            counts[w] += title_words.count(w)
    next_after = data.get("after")
    if next_after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return
    count_words(subreddit, word_list, counts, next_after)
