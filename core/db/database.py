import sqlite3
import os

class Driver:

    def __init__(self, db_name: str):
        self.__conn = sqlite3.connect(os.getenv('WORDS_DB'))
        self.cursor = self.__conn.cursor()

    def get_word(self, delete_from_db: bool = True) -> str:
        table = s.getenv('WORDS_TABLE')
        self.cursor.execute(f'SELECT * FROM {table} ORDER BY RANDOM() LIMIT 1;')
        word, = self.cursor.fetchone()

        if delete_from_db:
            self.cursor.execute(f'DELETE FROM {table} WHERE word='{word}')
            self.__conn.commit()

        return word

    def close(self):
        self.cursor.close()
        self.__conn.close()
