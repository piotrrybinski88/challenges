from data import DICTIONARY, LETTER_SCORES
from collections import namedtuple


def find_word_value(word):
    Word = namedtuple('Word', 'word points')
    return Word(word, sum([LETTER_SCORES[letter] for letter in word.upper()]))


def find_most_value_word():
    with open(DICTIONARY, 'r') as file:
        data = file.read()
    return max(
        list(
            map(find_word_value, data.split())
            ),
        key=lambda x: x.points
    )


if __name__ == '__main__':
    print(find_most_value_word())
