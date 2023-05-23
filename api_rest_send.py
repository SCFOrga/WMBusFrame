#!/usr/local/bin/python3.11
# Imports
import json
import requests
import mysql.connector
import mysqlol
import time
# Fonctions


# Programme principal

def sendistribute():
    sql = "TRUNCATE TABLE DonneesBrut"
    db = mysql.connector.connect(
        host="localhost",
        user="python",
        password="eclipse",
        database="SCFDonnees"
    )
    myjson = mysqlol.distribute(sql)
    myspecs = mysqlol.get_specs()
    id_eau = 0
    id_chauff = 0
    id_gaz = 0
    id_elec = 0
    id_temp = 0
    id_this = 0
    bigjson = []
    for row in myjson:
        for raw in myspecs:
            if row["identifiant"] == raw["identifiant"]:
                if raw["grandeur"] == "eau":
                    id_eau = id_eau + 1
                    id_this = id_eau
                elif raw["grandeur"] == "gaz":
                    id_gaz = id_gaz + 1
                    id_this = id_gaz
                elif raw["grandeur"] == "elec":
                    id_elec = id_elec + 1
                    id_this = id_elec
                elif raw["grandeur"] == "chauff":
                    id_chauff = id_chauff + 1
                    id_this = id_chauff
                elif raw["grandeur"] == "temp":
                    id_temp = id_temp + 1
                    id_this = id_temp
                bigjson.append({
                    "id": id_this,
                    "identifiant": row["identifiant"],
                    "donnees": row["donnees"] * raw["ratio"],
                    "donnees2": row["donnees2"] * raw["ratio"],
                    "grandeur": raw["grandeur"],
                    "date_recept": row["date_recept"]
                })
    bigjson = json.dumps(bigjson, indent=4)
    print(bigjson)
    response = requests.put("https://scf2023.lycee-lgm.fr/rest/create.php", bigjson)
    print(str(response) + "\tDonnées ajoutées à la bdd OVH")
    mycursor = db.cursor()
    mycursor.execute(sql)
    response = requests.get("https://scf2023.lycee-lgm.fr/rest/repart.php?table=DonneesElec&data=Elec") 
    print(str(response) + "\tDonnées elec réparties dans leurs tables")
    response = requests.get("https://scf2023.lycee-lgm.fr/rest/repart.php?table=DonneesChauff&data=Chauff")
    print(str(response) + "\tDonnées chauffage réparties dans leurs tables")
    response = requests.get("https://scf2023.lycee-lgm.fr/rest/repart.php?table=DonneesEau&data=Eau")
    print(str(response) + "\tDonnées eau réparties dans leurs tables")



def send():
    mydb = mysql.connector.connect(
    host="localhost",
    user="python",
    password="eclipse",
    database="SCFDonnees"
    )

    mycursor = mydb.cursor()
    mylist = []
    mycursor.execute("SELECT * FROM DonneesBrut")
    result = mycursor.fetchall()

    for row in result:
        mylist.append({"id": row[0],"identifiant":row[1],"donnees":row[2],"donnees2":row[3],"type":row[4].decode('utf-8'),"date_recept":row[5].isoformat()})
    myjson = json.dumps(mylist, indent=2)
    with open('file.json', 'w') as f:
        json.dump(mylist, f, indent=4)
    print(myjson)
    response = requests.put("https://scf2023.lycee-lgm.fr/test/create.php", myjson)
    print(response)
    response = requests.put("https://scf2023.lycee-lgm.fr/test/update.php", myjson)
    print(response)


# Fin
