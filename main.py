#!/usr/bin/env python3
# -*- coding: utf-8 -*-



"""This is a Test Code for my LED and Motor Driver"""
import time

__author__ = "Marc Steinebrunner"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "0.1"
__email__ = "marc.steinebrunner@gmail.com"
__status__ = "In Progress"


from LED import LED_C as LED_NO
from motor import Motor as Motor_NO

LED_O = LED_NO(7)
Motor_O = Motor_NO(11,13,15)

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


if __name__ == '__main__':
    main()
