#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""rgb_led.py:	RGB_LED class"""

__author__ = "Marc Steinebrunner"
__copyright__ = "Copyright (c) 2017 Marc Steinebrunner"
__version__ = "Development v0.01"
__email__ = "marc.steinebrunner@gmail.com"
__status__ = "Dev"

import RPi.GPIO as GPIO

class RGB_LED(object):

    def __init__(self, Pin_R, Pin_G, Pin_B):
        self.Pin = [Pin_R, Pin_G, Pin_B]
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.Pin[0], GPIO.OUT)
        GPIO.setup(self.Pin[1], GPIO.OUT)
        GPIO.setup(self.Pin[2], GPIO.OUT)

        self.frequenz = 50
        
        self.PWM = [GPIO.PWM(self.Pin[0], self.frequenz), GPIO.PWM(self.Pin[1], self.frequenz), GPIO.PWM(self.Pin[2], self.frequenz)]
        self.RGB = [0, 0, 0]
        self.status = False


    def hex_to_rgb(self, hex):
        self.RGB[0] = (int(hex[0:0 + 2], 16)*100/255)
        self.RGB[1] = (int(hex[2:2 + 2], 16)*100/255)
        self.RGB[2] = (int(hex[4:4 + 2], 16)*100/255)

    def on(self, hex):
        self.hex_to_rgb(hex)
        self.PWM[0].ChangeDutyCycle(self.RGB[0])
        self.PWM[1].ChangeDutyCycle(self.RGB[1])
        self.PWM[2].ChangeDutyCycle(self.RGB[2])

    def off(self):
        for i in range(0,2):
            self.PWM[i].stop()

    
