import sys
import urllib
from parse_tweets import Parse_Tweets

class Twitter_Feed():
    """Twitter Feed class prompts user for Twitter account to scrape."""
    def __init__(self):
        """Below, self.pt = Parse_Tweets() connects to the parsing class, rather than using
        direct instantiation."""
        feed = self.menu()
        self.pt = Parse_Tweets()
        self.twitterAccountFeed(feed)

    def menu(self):
        print(" ")
        print("/-- Tweet2Speech - Converts a user's Twitter feed to a spoken mp3 file --\\")
        print(" ")
        print("    [*] Be sure to have gTTS and bs4 modules installed before running")
        print("    [*] Input a twitter handle without the @ (i.e. DalaiLama)")
        print("    [*] An mp3 file will be output in the home folder")
        print("  ")
        feed = input("Enter the Twitter Name you want to capture (i.e. DalaiLama) : ")
        return feed

    def twitterAccountFeed(self, feed):
        """If we find data, it will be passed to the Parse_Tweets class using the syntax
        self.pt.parseTweets(html, feed) where pt was defined in this classes __init__ and
        the value for html is the raw data found when getting the twitter.com feed.  The
        Feed Name is passed as the paramter 'feed.'"""
        html = urllib.request.urlopen('https://twitter.com/' + feed)
        if html.getcode() == 200 and feed != '':
            self.pt.parseTweets(html, feed)

        else:
            print("Invalid Twitter Feed")
            sys.exit(1)

if __name__ == '__main__':
    Twitter_Feed().menu()
