# -*- coding: utf-8 -*-

class Lamp:
    _LAMPS = ['1', '0']

    def __init__(self, is_turned_on):
        self._is_turned_on = False
    

    def turn_on(self):
        self._is_turned_on = True
        self.display_image()


    def turn_off(self):
        self._is_turned_on = False
        self.display_image()

    def display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


    