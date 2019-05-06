import sys
import urllib
from parse_tweets import Parse_Tweets

class Twitter_Feed():

    def __init__(self):
        feed = self.menu()
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
        html = urllib.request.urlopen('https://twitter.com/' + feed)
        if html.getcode() == 200 and feed != '':
            pt = Parse_Tweets(html, feed)
            pt.parseTweets()

        else:
            print("Invalid Twitter Feed")
            sys.exit(1)

tf = Twitter_Feed()
tf.menu()