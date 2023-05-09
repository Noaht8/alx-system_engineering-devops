#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests
import json

def count_words(subreddit, word_list):
  """
  Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).

  Args:
    subreddit: The name of the subreddit to query.
    word_list: A list of keywords to count.

  Returns:
    A list of tuples, where each tuple contains the keyword and its count.
  """

  # Make the API request
  response = requests.get('https://api.reddit.com/r/{subreddit}/hot/.json'.format(subreddit=subreddit))
  if response.status_code != 200:
    print('Error: {}'.format(response.status_code))
    return

  # Parse the JSON response
  data = json.loads(response.content)

  # Get the titles of all hot articles
  titles = [post['title'] for post in data['data']['children']]

  # Count the occurrences of each keyword in the titles
  counts = {}
  for word in word_list:
    word = word.lower()
    counts[word] = titles.count(word)

  # Sort the counts by descending order
  sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

  # Print the sorted counts
  for word, count in sorted_counts:
    print('{0}: {1}'.format(word, count))

  return sorted_counts
