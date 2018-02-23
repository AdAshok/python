#!/usr/bin/python
#Doppelklatschen

import time 
gpioPort = 40  
import RPi.GPIO as GPIO
import mysql.connector

#MySQL Verbindung
statement = "UPDATE Flags SET wert=0 WHERE name='bewegung';"

#GPIO Layout verwenden
GPIO.setmode(GPIO.BOARD)

GPIO.setup(gpioPort, GPIO.IN)

lastSound = 0

def mysqlConnect(statement):
    cnx = mysql.connector.connect(user='pi', password='raspberry', host='localhost', database='EIT11C')
    cursor = cnx.cursor()
    cursor.execute(statement)
    cnx.commit()
    cursor.close()
    cnx.close()

while 1:
    if GPIO.input(gpioPort) == GPIO.HIGH:
        if lastSound == 0 or (lastSound + 500) < int(round(time.time()*1000)):
            lastSound = int(round(time.time()*1000))
            time.sleep(0.1)
            print("Klatchen1")
        else:
            print("Klatschen2")
            lastSound = 0 
            time.sleep(0.1)
            mysqlConnect(statement) 
