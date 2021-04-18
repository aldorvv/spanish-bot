import os
from typing import Tuple

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

    def get_content(self) -> Tuple[str, str]:
        word = self.db.get_word()
        return word, self.scrap.get_info(word)

    def tweet_word(self, max_retries: int = 10) -> Tuple[str, bool]:
        word, content = self.get_content()
        if not isinstance(content, str):
            return f'Error while tweeting {word} Error: {e}', False
    
        attempt = 0
        while (not content and attempt <= max_retries): 
            content = self.get_content()
            attempt += 1

        try:
            self.api.update_status(content)
            return f'Successfully tweeted {word}', True
        except Exception as e:
            return f'Error while tweeting {word} Error: {e}', False
