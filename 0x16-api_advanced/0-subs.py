#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyBot/1.0'}
    
    # Construct the URL for the subreddit's about.json
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid or not found, return 0
            return 0
    except:
        # If any error occurs during the request, return 0
        return 0
