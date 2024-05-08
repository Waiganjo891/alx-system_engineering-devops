#!/usr/bin/python3
"""
It counts words
"""
import requests
from collections import Counter
from typing import List


def count_words(subreddit: str, word_list: List[str]) -> None:
    """
    Base case: No more pages to fetch
    """
    if not has_more_posts(subreddit):
        return
    posts = fetch_hot_posts(subreddit)
    titles = [post['title'].lower() for post in posts]
    word_counts = Counter(
                    word for title in titles for word in word_list if word in title
                    )
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")


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
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [keyword.lower() for keyword in sys.argv[2].split()]
        count_words(subreddit, keywords)
