import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join("/tmp", "dictionary.txt")
urllib.request.urlretrieve("http://bit.ly/2iQ3dlZ", DICTIONARY)
scrabble_scores = [
    (1, "E A O I N R T L S U"),
    (2, "D G"),
    (3, "B C M P"),
    (4, "F H V W Y"),
    (5, "K"),
    (8, "J X"),
    (10, "Q Z"),
]
LETTER_SCORES = {
    letter: score for score, letters in scrabble_scores for letter in letters.split()
}


# start coding
def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    scrabble_list = []
    file = open("dictionary.txt", "r")
    for word in file.readlines():
        scrabble_list.append(word.strip())
    return scrabble_list


def load_words_alt():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f:
        words = [word.strip() for word in f]
    return words


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    score = 0
    for letter in word:
        if letter.isascii():
            score += LETTER_SCORES[letter.upper()]
    return score


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    max_scoring_word = ""
    for word in words:
        if calc_word_value(max_scoring_word) < calc_word_value(word):
            max_scoring_word = word
    return max_scoring_word
