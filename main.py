#!/usr/bin/env python3
# -*- coding: utf-8 -*-



"""Android.py:	Is the Code for a School Project"""
import time

__author__ = "Marc Steinebrunner"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "0.5"
__email__ = "marc.steinebrunner@gmail.com"
__status__ = "In Progress"


from LED import LED_C as LED_NO
from motor import Motor as Motor_NO

LED_O = LED_NO(7)
Motor_O = Motor_NO(11,13,15)

def main():
    BuchtabenString =     " A-Z = 1-26\n"\
                          " Ä = 27\n"\
                                " Ü = 28\n"\
                                " Ö = 29\n"\
                                " 0-9 = 30-39\n"

    Var = int(input("Wollen sie das Programm im Test Modus[1] starten oder im Alphabet modus[2]: "))
    if Var == 1:
        Motor_O.clockwise()
        while True:
                Motor_O.change_speed(10)
                LED_O.ON()
                time.sleep(2)
                Motor_O.change_speed(20)
                LED_O.OFF()
                time.sleep(2)
                Motor_O.change_speed(50)
                LED_O.ON()
                time.sleep(2)
                Motor_O.change_speed(99)
                LED_O.Flash(5)
                time.sleep(5)
                Motor_O.change_speed(50)
                LED_O.OFF()
                time.sleep(2)
                Motor_O.change_speed(10)
                LED_O.ON()
                time.sleep(2)
                Motor_O.change_speed(0)
                LED_O.OFF()
    elif Var == 2:
            while True:
                Buchstabe = int(input(BuchtabenString))
                LED_O.Alphabet(Buchstabe)

if __name__ == '__main__':
    main()
