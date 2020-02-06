# API Advanced

Concept Guidance:
* [Reddit API](https://www.reddit.com/dev/api/)

### [0. How many subs?](./0-subs.py)
> Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0
> Requirements:
> * Prototype: def number_of_subscribers(subreddit)
> * If not a valid subreddit, return 0
> * NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects

### [1. Top Ten](./1-top_ten.py)
> Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
> Requirements:
> * Prototype: def top_ten(subreddit)
> * If not a valid subreddit, print None
> * NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects

### [2. Recurse it!](./2-recurse.py)
> Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None

### [100. Count it!](./100-count.py)
> Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not)
> Requirements:
> * Prototype: def count_words(subreddit, word_list)
> * Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically. Words with no matches should be skipped and not printed
> * Results are based on the number of times a keyword appears, not titles it appears in. ‘java java java’ counts as 3 separate occurrences of java
> * To make life easier, ‘java.’ or ‘java!’ or ‘java_’ should not count as ‘java’
> * If no posts match or the subreddit is invalid, print a newline