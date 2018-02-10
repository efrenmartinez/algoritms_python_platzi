'''
Lee y escribe el archivo 'archivo.txt'
'''
# -*- coding:utf-8 -*-

def run():
    file = 'files/archivo.txt'
    day = '{"1": 0, "2": 2}'
    open_file = open(file, 'r+')
    print(open_file.readline())
    open_file.write(day)
    open_file.close()


if __name__ == '__main__':
    run()
