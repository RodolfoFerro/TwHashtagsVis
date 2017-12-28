# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Tweets extractor script.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

# We import our access keys:
from credentials import *    # This will allow us to use the keys as variables


# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


def extract(user):
    """
    Function to extract latest 200 tweets from a
    user provided.
    """
    # We create an extractor object from API:
    extractor = twitter_setup()

    # We create a tweet list as follows:
    tweets = extractor.user_timeline(screen_name=user, count=200)
    print("Number of tweets extracted: {}.\n".format(len(tweets)))

    return tweets


if __name__ == '__main__':
    tweets = extract("FerroRodolfo")
