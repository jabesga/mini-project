#!/usr/bin/env python
# -*- coding: utf8 -*-

#SDA    24      GPIO8
#SCK    23      GPIO11
#MOSI   19      GPIO10
#MISO   21      GPIO9
#IRQ    None    None
#GND    Any     Any Ground
#RST    22      GPIO25
#3.3V   1       3V3

#Imports, includes y sucedaneos
import RPi.GPIO as GPIO
import signal
import time
# import my_db

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global loop
    print "Ctrl+C captured, ending read."
    loop = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

#Constantes
SEGRELE_PIN = 13 #GPIO21
UPRELE_PIN = 12 #GPIO18
DOWNRELE_PIN = 11 #GPIO17

# SETUP
def setup():
    print "Configuring Board settings..."

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(SEGRELE_PIN, GPIO.OUT)
    GPIO.setup(UPRELE_PIN, GPIO.OUT)
    GPIO.setup(DOWNRELE_PIN, GPIO.OUT)

    GPIO.output(SEGRELE_PIN, False)
    GPIO.output(UPRELE_PIN, False)
    GPIO.output(DOWNRELE_PIN, False)


def upDoor():

    print "Activando rele de seguridad"
    GPIO.output(SEGRELE_PIN, True)
    started_time = time.time()
    duration = 15

    while time.time() - started_time < duration:
        print "Subiendo puerta"
        GPIO.output(UPRELE_PIN, True)
        GPIO.output(DOWNRELE_PIN, False)

    print "Desactivando todos los reles"
    GPIO.output(UPRELE_PIN, False)
    GPIO.output(DOWNRELE_PIN, False)
    GPIO.output(SEGRELE_PIN, False)

def downDoor():
    print "Activando rele de seguridad"
    GPIO.output(SEGRELE_PIN, True)
    started_time = time.time()
    duration = 15

    while time.time() - started_time < duration:
        print "Bajando puerta"
        GPIO.output(UPRELE_PIN, False)
        GPIO.output(DOWNRELE_PIN, True)

    print "Desactivando todos los reles"
    GPIO.output(UPRELE_PIN, False)
    GPIO.output(DOWNRELE_PIN, False)
    GPIO.output(SEGRELE_PIN, False)
