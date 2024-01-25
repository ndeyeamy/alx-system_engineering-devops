#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'CustomUserAgent'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and return the number of subscribers
            return data['data']['subscribers']

        # Check if the subreddit is invalid (status code 404)
        elif response.status_code == 404:
            print(f"The subreddit '{subreddit}' is not valid.")
            return 0

        # Handle other errors
        else:
            print(f"Error: {response.status_code}")
            return 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
