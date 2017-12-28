# Twitter hashtags visualization

Main goals:

1. Gather Twitter user's hashtags and analyze them.
2. Visualize data in a creative way.

## Setup

First clone the repo. I'm using [Python 3.6](https://www.python.org/downloads/) with the following packages:

* [NumPy](http://www.numpy.org/)
* [Pandas](http://pandas.pydata.org/)
* [Tweepy](http://www.tweepy.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)

To install all dependencies create a virtual env and run:

```bash
pip install -r requirements.txt
```

Now that we have all the requirements, we need to create a Twitter App.

### Creating a Twitter App

In order to extract tweets for a posterior analysis, we need to access to our Twitter account and create an app. The website to do this is [https://apps.twitter.com/](https://apps.twitter.com/). (If you don't know how to do this, you can follow this [quick tutorial video](https://www.youtube.com/watch?v=6wAHcHGgpFU) to create an account and an application.)

From this app that we're creating we will save the following information in a script called `credentials.py`:
* Consumer Key (API Key)
* Consumer Secret (API Secret)
* Access Token
* Access Token Secret

The content of this script is the following:
```python
# Description...

# Consumer:
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# Access:
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
```
