# -*- coding:utf-8 -*-


def palindromo():
    word = str(input('##Ingresa la palabra '))
    is_palindrome(word)


def is_palindrome(word):
    arr_word = list(word)
    new_word = ''
    for i in arr_word[::-1]:
        print(i)


if __name__ == '__main__':
    palindromo()
