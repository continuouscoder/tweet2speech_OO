from bs4 import BeautifulSoup
from gtts import gTTS
import re

class Parse_Tweets():
    def __init__(self):
        """After some code refactor, I removed the html and feed definitions from this __init__."""
        pass

    def parseTweets(self, html, feed):
        """Twitter_Feed class passes raw HTML found to this method, giving the raw html as 'html'
        and the twitter account name as 'feed.'  Notice the call to the text2speech method, which
        passes the sanitized text."""
        dialogue = []
        bt = BeautifulSoup(html, features='lxml')
        for div in bt.findAll("div", {"class": "js-tweet-text-container"}):
            noUrl = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '',
                           div.text)  # code from http://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
            dialogue.append(noUrl)
        speech = ''.join(dialogue)
        self.text2speech(speech, feed)

    def text2speech(self, text, feed):
        """Using the gTTS library, the sanitized text is passed into this method.  As there may be
        errors on attempt, we use a try block, which catches exceptions as 'e.'  The gTTS library
        attempts to convert the sanitized text to speech and save the result as an mp3 file."""
        try:
            print(text)
            print("Converting text to audio speech.")
            tts = gTTS(text=text, lang='en')
            tts.save(feed + '.mp3')
            print("Twitter feed has been converted to an mp3")
        except Exception as e:
            print("Error on audio conversion: ")
            print(e)