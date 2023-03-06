import serial
import time
from trame import Trame


def main():
    ser = serial.Serial('COM10', 19200, parity='N', bytesize=8, stopbits=2, timeout=0.1)    # open serial port

    while True:                                                         # Boucle infinie
        if ser.in_waiting > 0:                                          # Si on a reçu des données
            print("Nouvelle trame : ")                                  # On affiche un message
            telegram = ser.readall().hex(' ')                           # On récupère les données
            xe = ''                                                     # On initialise une variable
            previous = '00'                                             # On initialise une variable
            telesplit = telegram.split()                                # On sépare les données
            for i in telesplit:                                         # On parcourt les données
                if previous == '16' and i == '68':                      # Si on a un doublon de trame
                    break                                               # On sort de la boucle
                xe += i                                                 # On ajoute les données à la variable
                previous = i                                            # On met à jour la variable

            trame = Trame(telesplit)                                    # On crée un objet trame
            print(xe)                                                   # On affiche la trame
            print(trame)                                                # On affiche les informations de la trame

            time.sleep(0.1)                                             # On attend 100ms


if __name__ == '__main__':
    main()
