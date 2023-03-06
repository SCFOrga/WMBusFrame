import serial
import time


def gettx_id(telesplit):
    n3 = telesplit[5]
    n2 = telesplit[6]
    n1 = telesplit[7]
    n0 = telesplit[8]
    tx_id = n0 + n1 + n2 + n3
    return tx_id


def get_length(telesplit):
    n1 = telesplit[1]
    # n1 to string
    n1 = int(n1, 16)
    length = n1
    return length


def get_data(telesplit):
    data_length = get_length(telesplit) - 19
    data = telesplit[20:20+data_length]
    return data


def get_type(data):
    device_type = data[1]
    return device_type


def determine_type(device_type):
    typestr = ''
    if type == '01':
        typestr = 'Température'
    elif type == '02':
        typestr = 'Température & Humidité'
    elif type == '03':
        typestr = 'PT100 Température'
    elif type == '04':
        typestr = 'Pulsation'
    elif type == '05':
        typestr = "Compteur d'énergie"
    elif type == '23':
        typestr = 'Contact'
    elif type == '24':
        typestr = 'CO2'
    elif type == '25':
        typestr = '4-20mA Analogique'
    elif type == '26':
        typestr = '0-5V Analogique'
    elif type == '27':
        typestr = '0-10V Analogique'

    return typestr


def main():
    ser = serial.Serial('COM10', 19200, parity='N', bytesize=8, stopbits=2, timeout=0.1) # open serial port

    while True:                                                         # Boucle infinie
        if ser.in_waiting > 0:                                          # Si on a reçu des données
            print("Nouvelle trame : ")                                  # On affiche un message
            telegram = ser.readall().hex(' ')                           # On récupère les données
            xe = ''                                                     # On initialise une variable
            previous = '00'                                             # On initialise une variable
            telesplit = telegram.split()                                # On sépare les données
            length = get_length(telesplit)                              # On récupère la longueur
            identifier = gettx_id(telesplit)                            # On récupère l'identifiant
            data = get_data(telesplit)                                  # On récupère les données
            for i in telesplit:                                         # On parcourt les données
                if previous == '16' and i == '68':                      # Si on a un doublon de trame
                    break                                               # On sort de la boucle
                xe += i + ' '                                           # On ajoute les données à la variable
                previous = i                                            # On met à jour la variable
            print('    Identifiant : ' + identifier)                    # On affiche l'identifiant
            print('    Type : ' + determine_type(get_type(data)))       # On affiche le type
            print('    Longueur : ' + str(length))                      # On affiche la longueur
            print('    Données : ' + ''.join(data))                     # On affiche les données

            time.sleep(0.1)                                             # On attend 100ms


if __name__ == '__main__':
    main()
