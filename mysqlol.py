import mysql.connector
from trame import Trame

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="*******",
    passwd="********",
    database="my_table")

# Create a cursor
cursor = db.cursor()

# Send a query that fills the database with the data from the frame


def insert_data(trame):
    sql = "INSERT INTO DonneesBrut (identifiant, donnees, donnees2, type, date_recept)" + \
     " VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)"
    if trame.type == 'Pulsation' or trame.type == 'Contact':
        val = (trame.identifier, trame.pulse1, trame.pulse2, trame.type)
    elif trame.type == 'Température' or trame.type == 'PT100 Température':
        val = (trame.identifier, trame.temp, 0, trame.type)
    elif trame.type == 'Humidité':
        val = (trame.identifier, trame.humidity, 0, trame.type)
    elif trame.type == 'Température & Humidité':
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

    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")
