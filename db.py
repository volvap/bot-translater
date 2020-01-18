import sqlite3


class Database:
    def save_pair(self,rus,eng):
        with sqlite3.connect('words.db') as connection:
            cursor = connection.cursor()
            cursos.execute("""
                INSERT INTO trans VALUES({rus},{eng});

            """)
            return cursor.fetchall()


    def is_exist(self,rus):
        with sqlite3.connect('words.db') as connection:
            cursor = connection.cursor()
            cursos.execute("""
                SELECT COUNT(*) FROM trans WHERE rus = {rus});

                """)
            return cursor.fetchall()
