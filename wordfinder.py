"""Word Finder: finds random words from a dictionary."""


# Reminded myself of choice here: https://docs.python.org/3/library/random.html
from random import choice

def get_words(filepath):
    words = []
    file = open(filepath, 'r')
    for line in file:
        word = line.removesuffix('\n')
        words.append(word)
    return words

class WordFinder:
    def __init__(self, filepath):
        self.words = get_words(filepath)
        print(f'{len(self.words)} words read')
    
    def random(self):
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    def __init__(self, filepath):
        raw_words = get_words(filepath)
        self.words = [word for word in raw_words if word.isalpha() and not word.startswith('#')]
        print(f'{len(self.words)} words read')