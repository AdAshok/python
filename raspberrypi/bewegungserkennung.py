#!/usr/bin/python
#Bewegungssensor

import time 
import RPi.GPIO as GPIO
import mysql.connector


#GPIO Layout verwenden
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.IN)

lastMove = 0

#Hanlde mysql connection 
def mysqlConnect(statement):
    cnx = mysql.connector.connect(user='pi', password='raspberry', host='localhost', database='EIT11C')
    cursor = cnx.cursor()
    cursor.execute(statement)
    cnx.commit()
    cursor.close()
    cnx.close()


statement = "UPDATE Flags SET wert=0 WHERE name='bewegung';"


while 1:
    if GPIO.input(40) == GPIO.HIGH:
        if lastMove == 0:
            print("Bewegung")
            mysqlConnect(statement)
        lastMove = int(round(time.time()*1000))
    elif GPIO.input(40) == GPIO.LOW:
        if lastMove != 0:
            if lastMove <= (int(round(time.time()*1000))-1000):
                lastMove = 0
                print("Keine Bewegung")


