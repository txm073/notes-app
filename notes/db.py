import sqlite3
import random
import os


class Database:

    __keys__: tuple = ("id", "title", "content", "date")
    __tablename__: str = "notes"

    def __init__(self, db_path: str = None):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

        init_cmd = \
            f"""
            CREATE TABLE IF NOT EXISTS {self.__tablename__} (
                INTEGER id,
                TEXT title,
                TEXT content,
                TEXT date
            )
            """
        self.cursor.execute(init_cmd)

    def add_data(self, **data):
        assert tuple(data.keys()) == self.__keys__[1:], f"data parameter should contain the keys {self.__keys__[1:]}"
        row_id = 0
        ids = self.fetch_column("id");
        while (not row_id or row_id in ids):
            row_id = random.randint(1, 0xffffffff)
        wildcards = ", ".join(["?" for i in range(len(self.__keys__))])
        self.cursor.execute(f"INSERT INTO {self.__tablename__} VALUES ({wildcards})", (row_id, *tuple(data.values())))

    def fetch_all(self):
        self.cursor.execute(f"SELECT * FROM {self.__tablename__}")
        return self.cursor.fetchall()

    def fetch_row(self, row_id):
        self.cursor.execute(f"SELECT * FROM {self.__tablename__} WHERE id == {row_id}")
        return {k: v for k, v in zip(self.__keys__, self.cursor.fetchone())}

    def fetch_column(self, field):
        self.cursor.execute(f"SELECT {field} FROM {self.__tablename__}")
        return [result[0] for result in self.cursor.fetchall()]

    def update_row(self, row_id, field, value):
        self.cursor.execute(f"UPDATE {self.__tablename__} SET {field} = '{value}' WHERE id == {row_id}")

    def delete_row(self, row_id):
        self.cursor.execute(f"DELETE * FROM {self.__tablename__} WHERE id == {row_id}")