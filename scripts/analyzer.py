# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Tweets analizer script.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

from extractor import TweetsExtractor


class TweetsAnalyzer():

    def __init__(self, extractor):
        """
        Constructor function using a TweetsExtractor
        object.
        """

        # Construct object:
        self.extractor = extractor
        self.data = None
        self.hashtags = {}

        return

    def analyze(self, user):
        """
        Analyzer function to gather all data from
        a TweetsExtractor object.
        """

        # Extract data from extractor:
        self.data = self.extractor.extract(user)

        # Construct hashtags dictionary:
        for entity in self.data['Entities']:
            if entity['hashtags']:
                for hashtag in entity['hashtags']:
                    if hashtag['text'] in self.hashtags.keys():
                        self.hashtags[hashtag['text']] += 1
                    else:
                        self.hashtags[hashtag['text']] = 1
        return

    def hashtags(self):
        """
        Function to return a dictionary containing all
        hashtags from extracte data.
        """
        return self.hashtags


if __name__ == '__main__':
    extractor = TweetsExtractor()
    analyzer = TweetsAnalyzer(extractor, "FerroRodolfo")
    print(analyzer.hashtags)
