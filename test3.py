#!/usr/local/bin/python3.11
# coding: UTF-8
"""
Script: WMBusFrame/test3.py
Création: qrobert, le 28/04/2023
"""


# Imports

import mysql.connector

# Fonctions


# Programme principal
def main():
    id = 0
    db = mysql.connector.connect(
        host="172.16.126.150",
        user="distant",
        passwd="eclipse",
        database="SCFDonnees")
    cursor = db.cursor()

    result = cursor.execute("SELECT MAX(id) from DonneesEau")
    
    print(result)


if __name__ == '__main__':
    main()

# Fin

