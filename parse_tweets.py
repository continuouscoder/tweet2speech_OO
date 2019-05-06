from bs4 import BeautifulSoup
from gtts import gTTS
import re

class Parse_Tweets():
    def __init__(self, html, feed):
        self.html = html
        self.feed = feed

    def parseTweets(self):
        dialogue = []
        bt = BeautifulSoup(self.html, features='lxml')
        for div in bt.findAll("div", {"class": "js-tweet-text-container"}):
            noUrl = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '',
                           div.text)  # code from http://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
            dialogue.append(noUrl)
        speech = ''.join(dialogue)
        self.text2speech(speech)

    def text2speech(self, text):
        try:
            print(text)
            print("Converting text to audio speech.")
            tts = gTTS(text=text, lang='en')
            tts.save(self.feed + '.mp3')
            print("Twitter feed has been converted to an mp3")
        except Exception as e:
            print("Error on audio conversion: ")
            print(e)