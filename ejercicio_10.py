# -*- coding: utf-8 -*-
import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']


WORDS = [
    'hola',
    'mundo',
    'cruel'
]


def random_word():
    index = random.randint(0, len(WORDS) - 1)
    return WORDS[index]


def display_board(tries, hidden_word):
    print(IMAGES[tries])
    print(hidden_word)
    print('Intento {}'.format(tries))


def run():
    word = random_word()
    print(word)
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(tries, hidden_word)
        current_word = str(input('Escoga una palabra '))

        letter_indexes = []
        for index in range(len(word)):
            if index == current_word:
                letter_indexes.append(index)
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(tries, hidden_word)
                print('PERDISTE')
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_word
            letter_indexes = []


if __name__ == '__main__':
    run()
