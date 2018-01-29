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

def display_board(tries,hidden_word):
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

        other_word = []
        for i in list(word):
            if i == current_word:
                other_word.append(i)
        
        if len(other_word) == 0:
            tries += 1
            if tries == 7:
                display_board(tries, hidden_word)
                print('PERDISTE')
                break
        else:
            for idx in other_word:
                hidden_word[idx] = current_word
            
        other_word = []


if __name__ == '__main__':
    run()