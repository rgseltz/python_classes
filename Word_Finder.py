import random

class Word_Finder:
    """Makes a list of words and randomly picks one from them"""
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = self.read()

    def read(self):
        file = open(self.file_path, "r")
        return file.read().splitlines()
    
    def random(self):
        return random.choice(self.words)
    
