import sqlite3
import random
import requests

RAE_HTTP_SERVER = 'https://dle.rae.es'

lines = open('out.txt', 'r').readlines()
conn = sqlite3.connect('words.sql')
cur = conn.cursor()

def get_word() -> str:
    cur.execute('SELECT * FROM words ORDER BY RANDOM() LIMIT 1;')
    word, = random.choice(cur.fetchall())
    cur.execute(f"DELETE FROM words WHERE word='{word}'")
    conn.commit()
    return word

def get_html(word: str) -> str:
    target = word.replace(' ', '%20')
    return requests.get(f'{RAE_HTTP_SERVER}/{target}').text
    return resp.text

def check_html(response_text: str):
    