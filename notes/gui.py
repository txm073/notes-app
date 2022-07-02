from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from notes import Note
import os, sys


class NoteWidget(QWidget):

    def __init__(self, note: Note):
        pass


class NotesWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(NotesWindow, self).__init__(*args, **kwargs)

    def initUI(self):
        pass
