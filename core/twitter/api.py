import os

import tweepy

from core.db import Driver
from core.scrap import Scrapper

class Bot:

    def __init__(self):
        self.__auth = tweepy.OAuthHandler(
            os.getenv('TW_CONSUMER_KEY'),
            os.getenv('TW_CONSUMER_SECRET')
        )
        self.__auth.set_access_token(
            os.getenv('TW_ACCESS_TOKEN'),
            os.getenv('TW_ACCESS_TOKEN_SECRET')
        )
        self.api = tweepy.API(self.__auth)
        self.db = Driver()
        self.scrap = Scrapper()

    def get_content(self) -> str:
        word = self.db.get_word()
        self.scrap.get_info(word)

    def tweet_word(self, word: str, max_retries: int = 10) -> bool:
        content = self.get_content()
    
        attempt = 0
        while (not content and attempt < max_retries):
            content = self.get_content()
            attempt += 1

        self.api.update_status(content)