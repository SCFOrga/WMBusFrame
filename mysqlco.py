#!/usr/local/bin/python3.11
import mysql.connector
import json
from trame import Trame


# Send a query that fills the database with the data from the frame
def get_specs():
    mydb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="eclipse",
        database="SCFDonnees"
    )
    sql = "SELECT * FROM Specs"
    mycursor = mydb.cursor()
    mylist = []
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for row in result:
        mylist.append({"identifiant": row[0], "grandeur": row[1], "ratio": row[2], "unite": row[3]})
    return mylist


def distribute(sql):
    mydb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="eclipse",
        database="SCFDonnees"
    )
    sql = "SELECT * FROM DonneesBrut"
    mycursor = mydb.cursor()
    mylist = []
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for row in result:
        mylist.append({"identifiant":row[1],"donnees":row[2],"donnees2":row[3],"type":row[4],"date_recept":row[5].isoformat()})
    return mylist

def filltables():
    mydb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="eclipse",
        database="SCFDonnees"
    )
    mycursor = mydb.cursor()
    mylist = []



def insert_data(trame):
    db = mysql.connector.connect(
        host="localhost",
        user="python",
        passwd="eclipse",
        database="SCFDonnees")
    cursor = db.cursor()
    sql = "INSERT INTO DonneesBrut (identifiant, donnees, donnees2, type, date_recept)" + \
     " VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)"
    if trame.type == 'Pulsation' or trame.type == 'Contact':
        val = (trame.identifier, trame.pulse1, trame.pulse2, trame.type)
    elif trame.type == 'Temperature' or trame.type == 'PT100 Temperature':
        val = (trame.identifier, trame.temp, 0, trame.type)
    elif trame.type == 'Humidité':
        val = (trame.identifier, trame.humidity, 0, trame.type)
    elif trame.type == 'Temperature & Humidité':
        val = (trame.identifier, trame.temp, trame.humidity, trame.type)
    elif trame.type == 'CO2':
        val = (trame.identifier, trame.co2, trame.temp, trame.type)
    elif trame.type == '4-20 Analogique':
        val = (trame.identifier, trame.value, 0, trame.type)
    elif trame.type == '0-5 Analogique':
        val = (trame.identifier, trame.value, 0, trame.type)
    elif trame.type == '0-10 Analogique':
        val = (trame.identifier, trame.value, 0, trame.type)
    else:
        val = (trame.identifier, trame.data, 0, "Inconnu")

    try:
        cursor.execute(sql, val)
        db.commit()
        print(cursor.rowcount, "donnée ajouté à la bdd.")
    except mysql.connector.errors.ProgrammingError as e:
        print(e)

def list_data():
    db = mysql.connector.connect(
    host="localhost",
    user="python",
    passwd="eclipse",
    database="SCFDonnees")

    cursor = db.cursor()
    sql = "DESCRIBE DonneesBrut"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

def count_id():
    db = mysql.connector.connect(
    host="localhost",
    user="python",
    passwd="eclipse",
    database="SCFDonnees")

    cursor = db.cursor()
    sql = "SELECT DISTINCT identifiant FROM DonneesBrut"
    cursor.execute(sql)
    result = cursor.fetchall()

    print("Identifiants différents :")
    i = 1
    for x in result:
        print(x[0])
    
