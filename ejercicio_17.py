# -*- coding: utf-8 -*-

from lamp import Lamp


def run():
    lamp = Lamp(is_turned_on=False)
    print("="*10)
    bool_on = str(input('Desea prender la lamparada (S/N) '))

    if bool_on == 'S':
        lamp.turn_on()
    elif bool_on == 'N':
        lamp.turn_off()


if __name__ == '__main__':
    run()
