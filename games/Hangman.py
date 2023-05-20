import random
from words import words


def get_valid_word(words):
    word = random.choice(words)  # randomly choose something from the list
    while "-" in words or " " in words:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    # not completed yet

