#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit
"""
import requests


def top_ten(subreddit):
    """
    Return the total number of subscribers on a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(
                    url, headers=headers, params=params, allow_redirects=False
                    )
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
