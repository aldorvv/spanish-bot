import os

import requests
from bs4 import BeautifulSoup

class Scrapper:

    def __init__(self):
        self.server = os.getenv('RAE_SERVER')

    def __get_html(self, word: str) -> str:
        target = word.replace(' ', '%20')
        return requests.get(f'{self.server}/{target}').text

    def get_info(self, word: str) -> str:

        html_response = self.__get_html(word)
        soup = BeautifulSoup(html_response, features="html.parser")
        et = soup.select('.n2')
        meaning = soup.select('.j')

        if et and meaning:
            str_meaning = ''.join([letter for letter in meaning[0].text if not letter.isdigit()])
            str_et = ''.join([letter for letter in et[0].text if not letter.isdigit()])
            return f'{word}\n{str_et}\n{str_meaning}'
        
        if not et and meaning:
            str_meaning = ''.join([letter for letter in meaning[0].text if not letter.isdigit()])
            return f'{word}\n{str_meaning}'

        return ''

        