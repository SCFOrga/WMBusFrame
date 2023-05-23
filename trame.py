"""
Auteur: Quentin ROBERT
Date: 2023-03-06
Description: Classe Trame
Cette classe permet de recuperer les informations d'une trame reçue par le recepteur WM-BUS.
"""
    

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
    data = telesplit[20:20 + data_length]
    return data


def get_rssi(telesplit):
    data_length = get_length(telesplit) - 19
    rssi = telesplit[20 + data_length]
    rssi = -int(rssi, 16) / 2
    return rssi


def get_type(data):
    device_type = data[1]
    return device_type


def battery_level(data):
    value = data[len(data) - 1]
    if value == '01':
        battery = 'OK'
    else:
        battery = 'LOW'
    return battery


def determine_type(device_type):
    typestr = ''
    if device_type == '01':
        typestr = 'Temperature'
    elif device_type == '02':
        typestr = 'Temperature & Humidite'
    elif device_type == '03':
        typestr = 'PT100 Temperature'
    elif device_type == '04':
        typestr = 'Pulsation'
    elif device_type == '05':
        typestr = "Compteur d'energie"
    elif device_type == '23':
        typestr = 'Contact'
    elif device_type == '24':
        typestr = 'CO2'
    elif device_type == '25':
        typestr = '4-20mA Analogique'
    elif device_type == '26':
        typestr = '0-5V Analogique'
    elif device_type == '27':
        typestr = '0-10V Analogique'
    else:
        typestr = 'Inconnu'

    return typestr


def get_pulses(data):
    pulse1 = int(data[3], 16) + int(data[4], 16)*2**8 + int(data[5], 16)*2**16 + int(data[6], 16)*2**24
    pulse2 = int(data[7], 16) + int(data[8], 16)*2**8 + int(data[9], 16)*2**16 + int(data[10], 16)*2**24
    return pulse1, pulse2


def get_temp(data):
    value = int(data[3], 16) + int(data[4], 16)*2**8
    idk = "0x%s" % (data[4])
    if int(idk, 16) & 0x80 == 0x80:
        value = (65536 - value) / 10
    else:
        value = value / 10
    return value


def get_temp_humidity(data):
    temp = int(data[3], 16) + int(data[4], 16)*2**8
    if int(data[4], 16) & 0x80 == 0x80:
        temp = (65536 - temp) / 10
    else:
        temp = temp / 10
    humidity = int(data[5], 16) + int(data[6], 16)*2**8
    humidity = humidity / 10
    return temp, humidity


def get_co2(data):
    co2 = int(data[3], 16) + int(data[4], 16)*2**8
    temp = int(data[5], 16) + int(data[6], 16)*2**8
    idk = "0x%s" % (data[6])
    if int(idk, 16) & 0x80 == 0x80:
        temp = (65536 - temp) / 10
    else:
        temp = temp / 10
    humidity = int(data[7], 16) + int(data[8], 16)*2**8
    humidity = humidity / 10
    lastminco2 = int(data[9], 16) + int(data[10], 16)*2**8
    print(data[9])
    print(data[10])
    print(lastminco2)
    co2sample = int(data[11], 16)
    return co2, temp, humidity, lastminco2, co2sample


def get_4_20_analog(data):
    value = int(data[3], 16) + int(data[4], 16)*2**8
    value = value / 100
    return value


def get_0_5_analog(data):
    value = int(data[3], 16) + int(data[4], 16)*2**8
    value = value / 100
    return value


def get_0_10_analog(data):
    value = int(data[3], 16) + int(data[4], 16)*2**8
    value = value / 100
    return value


class Trame:
    def __init__(self, telesplit):
        self.identifier = gettx_id(telesplit)
        self.data = get_data(telesplit)
        self.type = determine_type(get_type(self.data))
        self.length = get_length(telesplit)
        self.rssi = get_rssi(telesplit)
        if self.type == 'Pulsation' or self.type == 'Contact':
            self.pulse1, self.pulse2 = get_pulses(self.data)
            if self.identifier == '11523820':
                self.pulse2 = 0
        if self.type == 'Temperature' or self.type == 'PT100 Temperature':
            self.temp = get_temp(self.data)
        if self.type == 'Temperature & Humidite':
            self.temp, self.humidity = get_temp_humidity(self.data)
        if self.type == 'CO2':
            self.co2, self.temp, self.humidity, self.lastminco2, self.co2sample = get_co2(self.data)
        if self.type == '4-20mA Analogique':
            self.value = get_4_20_analog(self.data)
        if self.type == '0-5V Analogique':
            self.value = get_0_5_analog(self.data)
        if self.type == '0-10V Analogique':
            self.value = get_0_10_analog(self.data)
        if self.type == "Compteur d'energie":
            self.pulse1, self.pulse2 = get_pulses(self.data)

    def __str__(self):
        return "\n" + \
                "Identifiant : " + self.identifier + "\n" + \
               "Type : " + self.type + "\n" + \
               "Longueur : " + str(self.length) + "\n" + \
               "Donnees : " + self.data_type() + "\n" + \
               "RSSI : " + str(self.rssi) + "dbm" + "\n" + \
               "Batterie : " + battery_level(self.data) + "\n"

    def get_identifier(self):
        return self.identifier

    def data_type(self):
        if self.type == 'Pulsation' or self.type == 'Contact':
            value = "\n" + "    Pulse 1 : " + str(self.pulse1) + "\n" + "    Pulse 2 : " + str(self.pulse2)
        elif self.type == 'Temperature' or self.type == 'PT100 Temperature':
            value = "\n" + "    Temperature : " + str(self.temp) + "°C"
        elif self.type == 'Temperature & Humidite':
            value = "\n" + "    Temperature : " + str(self.temp) + "°C" + "\n" + "    Humidite : " + str(self.humidity)\
                    + "%RH"
        elif self.type == 'CO2':
            value = "\n" + "    CO2 : " + str(self.co2) + "ppm" + "\n" + "    Temperature : " + str(self.temp) + "°C" + \
                    "\n" + "    Humidite : " + str(self.humidity) + "%RH" + "\n" + "    CO2 dernier minimal : " + \
                    str(self.lastminco2) + "ppm" + "\n" + "    CO2 sample : " + str(self.co2sample)
        elif self.type == '4-20mA Analogique':
            value = "\n" + "    Valeur : " + str(self.value) + "mA"
        elif self.type == '0-5V Analogique':
            value = "\n" + "    Valeur : " + str(self.value) + "V"
        elif self.type == '0-10V Analogique':
            value = "\n" + "    Valeur : " + str(self.value) + "V"
        else:
            value = 'Donnees non disponibles pour ce type de trame inconnue'
        return value

    def get_type(self):
        return self.type

    def get_length(self):
        return self.length

    def get_data(self):
        return self.data

    def get_rssi(self):
        return self.rssi

