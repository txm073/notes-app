from notes.db import Database
from datetime import datetime


class Note:

    def __init__(self, title: str, content: str, date: datetime):
        self.title = title
        self.content = content
        self.date = date

    def update(self, field, value):
        pass

    def delete(self):
        pass