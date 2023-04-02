"""
Let's say you're working on Twitter and your boss asked you to build a feature, perhaps a feature that allows anybody
to click a button next to their name and retrieve their most recent tweet and their oldest tweet.
"""


# Find 1st, Find Nth...

ARRAY = [
    {
        'tweet': 'hi',
        'date': 2012
    }, {
        'tweet': 'my',
        'date': 2014
    }, {
        'tweet': 'teddy',
        'date': 2018
    }]


def find_first_and_last_tweet(array):
    print(array[0])  # O(1)
    print(array[-1])  # O(1)


find_first_and_last_tweet(ARRAY)


# Now our boss come back to us and say he wants us to compare the dates of tweets


def compare_dates(input):
    for element in input:
        print(element['date'])


compare_dates(ARRAY)
