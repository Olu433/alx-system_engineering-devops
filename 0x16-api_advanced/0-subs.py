#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers to the subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom-User-Agent/0.0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Ensure the request was successful
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
    except requests.RequestException as e:
        # Handle any network-related errors
        pass

    # If request wasn't successful, return 0
    return 0
