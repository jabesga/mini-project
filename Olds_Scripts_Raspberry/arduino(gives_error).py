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
import MFRC522
import signal
import time
import my_db
import socket

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global loop
    print "Ctrl+C captured, ending read."
    loop = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

#Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.socket(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("localhost", 9988))
s.listen(1)

#Constantes
UPBUTTON_PIN = 16  #GPIO23
DOWNBUTTON_PIN = 15 #GPIO22
SEGRELE_PIN = 13 #GPIO21
UPRELE_PIN = 12 #GPIO18
DOWNRELE_PIN = 11 #GPIO17

# Variables digitales de los botones
upButton, downButton = (False,)*2

#Flags y sucedaneos
last_uid = None
MIFAREReader = None
continue_reading = True
loop = True

# SETUP
def setup():
    print "Configuring Board settings..."

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(UPBUTTON_PIN, GPIO.IN)
    GPIO.setup(DOWNBUTTON_PIN, GPIO.IN)
    GPIO.setup(SEGRELE_PIN, GPIO.OUT)
    GPIO.setup(UPRELE_PIN, GPIO.OUT)
    GPIO.setup(DOWNRELE_PIN, GPIO.OUT)

    GPIO.output(SEGRELE_PIN, False)
    GPIO.output(UPRELE_PIN, False)
    GPIO.output(DOWNRELE_PIN, False)

    # Create an object of the class MFRC522
    global MIFAREReader
    MIFAREReader = MFRC522.MFRC522()

# Funcion para recoger el uid. Se compara con la anterior leida. Si es igual se fuerza el error.
def getID(): 
    uid = None
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    if status == MIFAREReader.MI_OK:
        (status, uid) = MIFAREReader.MFRC522_Anticoll()
        # MOSTRAR EJEMPLO
        if uid is [] or last_uid: # Las lecturas pares uid vale [] y las impares su valor real
            pass
    return (status, uid)

def logged():
    GPIO.output(SEGRELE_PIN, True)
    last_time_pressed = time.time()

    while True:
        current_time = time.time()

        upButton = GPIO.input(UPBUTTON_PIN)
        downButton = GPIO.input(DOWNBUTTON_PIN)
        if upButton == True and downButton == False:
            last_time_pressed = time.time()
            GPIO.output(UPRELE_PIN, True)
            GPIO.output(DOWNRELE_PIN, False)
        elif upButton == False and downButton == True:
            last_time_pressed = time.time()
            GPIO.output(UPRELE_PIN, False)
            GPIO.output(DOWNRELE_PIN, True)
        else:
            GPIO.output(UPRELE_PIN, False)
            GPIO.output(DOWNRELE_PIN, False)

        if current_time - last_time_pressed > 3:
            break

    GPIO.output(UPRELE_PIN, False)
    GPIO.output(DOWNRELE_PIN, False)
    GPIO.output(SEGRELE_PIN, False)

setup()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while True:
    upButton = GPIO.input(UPBUTTON_PIN)
    downButton = GPIO.input(DOWNBUTTON_PIN)

    if upButton == True:
            print "arriba"
    elif upButton == False and downButton == True:
            print "abajo"
    else:
            print "error"



