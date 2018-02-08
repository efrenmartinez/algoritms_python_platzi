'''
Encripta/desencripta frases usando diccionarios
'''

# -*- coding: utf-8 -*-

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B'
}


def cypher(message):
    list_message = message.split(' ')
    list_message_hidden = []

    for word in list_message:
        message_hidden = ''
        for letter in word:
            message_hidden += KEYS[letter]
        list_message_hidden.append(message_hidden)

    return ' '.join(list_message_hidden)


def decypher(message_decypher):
    list_message_decypher = message_decypher.split(' ')
    list_message = []

    for word in list_message_decypher:
        message = ''
        for letter in word:
            for key, value in KEYS.items():
                if letter == value:
                    message += key
        list_message.append(message)

    return ' '.join(list_message)


def run():
    while True:
        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---
            Bienvenido a criptografía. ¿Qué deseas hacer?
            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu frase : '))
            message_hidden = cypher(message)
            print('Frase encriptada : {}'.format(message_hidden))
        elif command == 'd':
            message = str(input('Escribe tu frase encriptada: '))
            message_hidden = decypher(message)
            print('Tú frase : {}'.format(message_hidden))
        elif command == 's':
            exit()
        else:
            print('Elija otra opción.')


if __name__ == '__main__':
    run()
