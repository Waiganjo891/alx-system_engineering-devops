#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
"""
import requests
from typing import List


def recurse(subreddit: str, hot_list: List[str] = []) -> List[str]:
    """
    Recursively fetches hot articles from a given subreddit and
    returns a list of their titles.
    """
    if not has_more_posts(subreddit):
        return hot_list
    posts = fetch_hot_posts(subreddit)
    for post in posts:
        hot_list.append(post['title'])
    return recurse(subreddit, hot_list)


def fetch_hot_posts(subreddit: str) -> List[dict]:
    """
    Fetches hot posts from the specified subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []
    data = response.json()
    return data['data']['children']


def has_more_posts(subreddit: str) -> bool:
    """
    Checks if there are more posts to fetch.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.head(url, headers=headers)
    return response.status_code == 200 and "X-Ratelimit-Remaining" in response.headers


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
