# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Tweets visualizer script.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

from extractor import TweetsExtractor
from analyzer import TweetsAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class TweetsVisualizer():

    def __init__(self, analyzer):
        """
        Constructor function using a TweetsExtractor
        object.
        """

        # Construct object:
        self.analyzer = analyzer
        self.data = self.analyzer.data
        self.hashtags = self.analyzer.hashtags

        return

    def retweets(self):
        """
        Function to plot time series of retweets.
        """

        # We create time series for data:
        data = self.data
        tret = pd.Series(data=data['RTs'].values, index=data['Date'])

        # Lenghts along time:
        plt.title("Retweets along time")
        tret.plot(figsize=(16, 4), label="Retweets", color='g', legend=True)

        return

    def likes(self):
        """
        Function to plot time series of likes.
        """

        # We create time series for data:
        data = self.data
        tfav = pd.Series(data=data['Likes'].values, index=data['Date'])

        # Lenghts along time:
        plt.title("Likes along time")
        tfav.plot(figsize=(16, 4), label="Likes", color='b', legend=True)

        return

    def lengths(self):
        """
        Function to plot time series of lengths.
        """

        # We create time series for data:
        data = self.data
        tlen = pd.Series(data=data['len'].values, index=data['Date'])

        # Lenghts along time:
        plt.title("Lenghts along time")
        tlen.plot(figsize=(16, 4), label="Leghts", color='r', legend=True)

        return


if __name__ == '__main__':
    extractor = TweetsExtractor()
    analyzer = TweetsAnalyzer(extractor)
    analyzer.analyze("FerroRodolfo")
    visualizer = TweetsVisualizer(analyzer)
    visualizer.time_series()
