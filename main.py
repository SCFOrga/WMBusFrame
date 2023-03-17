import serial
from trame import Trame
from mysqlol import insert_data


def main():
    ser = serial.Serial('COM10', 19200, parity='N', bytesize=8, stopbits=2, timeout=0.1)  # open serial port
    while True:                                                         # Boucle infinie
        if ser.in_waiting > 0:                                          # Si on a reçu des données
            telegram = ser.readall().hex(' ')                           # On récupère les données
            xe = ''                                                     # On initialise une variable
            previous = '00'                                             # On initialise une variable
            telesplit = telegram.split()                                # On sépare les données
            for i in telesplit:                                         # On parcourt les données
                if previous == '16' and i == '68':                      # Si on a un doublon de trame
                    break                                               # On sort de la boucle
                xe += i                                                 # On ajoute les données à la variable
                previous = i                                            # On met à jour la variable

            trame = Trame(telesplit)
            if trame.identifier.startswith('0'):
                continue
            else:
                print("Nouvelle trame : ")                              # On affiche un message
                print(xe)
                print(trame)                                            # On affiche les informations de la trame
                insert_data(trame)


if __name__ == '__main__':
    main()
