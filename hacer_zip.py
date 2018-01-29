# -*- coding:utf-8 -*-

import os

def run():
    url = '/home/efren/Plataformas/HPUB_2';

    os.chdir(url)
    arr = os.system('ls -l')

def chooseBook():
    print('====================================')
    id_book = str(input('Inglesa ID del libro '))
    name_book = id_book.upper()
    subject_book = name_book[0:1]

    



if __name__ == '__main__':
    chooseBook()