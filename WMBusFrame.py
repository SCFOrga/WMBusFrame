#!/usr/bin/python3

import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 19200, parity='N', bytesize=8, stopbits=2, timeout=0.1)

while True:
    try:
        if ser.in_waiting > 0:
            print("frame : ", end='')
            telegram = ser.readall().hex()
            xe = ''
            telesplit = telegram.split()
            for i in telesplit:
                xe += i + ' '
                print(i)
            time.sleep(0.1)
    except KeyboardInterrupt:
        break

print("End of reception")