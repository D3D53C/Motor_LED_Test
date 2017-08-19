#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test File for Motor and LED objects"""
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
    
    Motor_O.clockwise()
    while True:
        Var = int(input("Welchen Speed (0 - 99)"))
        Motor_O.change_speed(Var)
    
if __name__ == '__main__':
    main()
