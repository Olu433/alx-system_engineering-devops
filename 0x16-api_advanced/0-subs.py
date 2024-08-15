#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
<<<<<<< HEAD
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
=======
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
>>>>>>> refs/remotes/origin/master
