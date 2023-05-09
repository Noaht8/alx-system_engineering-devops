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

  # Check if the subreddit is valid.
  if not subreddit:
    print("Invalid subreddit.")
    return

  # Get the hot articles for the subreddit.
  response = requests.get("https://api.reddit.com/r/{}/hot.json?limit=100".format(subreddit))
  if response.status_code != 200:
    print("Error fetching hot articles for subreddit {}.".format(subreddit))
    return

  # Parse the response and get the titles of the articles.
  data = json.loads(response.content)
  titles = [article["title"] for article in data["data"]["children"]]

  # Count the number of times each keyword appears in the titles.
  counts = {}
  for title in titles:
    for word in word_list:
      if word.lower() in title.lower():
        if word not in counts:
          counts[word] = 1
        else:
          counts[word] += 1

  # Sort the counts by their value, in descending order.
  sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

  # Print the sorted counts.
  for word, count in sorted_counts:
    print("{}: {}".format(word, count))

  return sorted_counts
