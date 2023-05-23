#!/usr/local/bin/python3.11
import api_rest_send
import time

while True:
    api_rest_send.sendistribute()
    time.sleep(600)