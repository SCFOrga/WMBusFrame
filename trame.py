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


def determine_type(device_type):
    typestr = ''
    if device_type == '01':
        typestr = 'Température'
    elif device_type == '02':
        typestr = 'Température & Humidité'
    elif device_type == '03':
        typestr = 'PT100 Température'
    elif device_type == '04':
        typestr = 'Pulsation'
    elif device_type == '05':
        typestr = "Compteur d'énergie"
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
    pulse1 = data[6] + data[5] + data[4] + data[3]
    pulse2 = data[10] + data[9] + data[8] + data[7]
    pulse1 = int(pulse1, 16)
    pulse2 = int(pulse2, 16)
    return pulse1, pulse2


class Trame:
    def __init__(self, telesplit):
        self.identifier = gettx_id(telesplit)
        self.data = get_data(telesplit)
        self.type = determine_type(get_type(self.data))
        self.length = get_length(telesplit)
        self.rssi = get_rssi(telesplit)

    def __str__(self):
        return "Identifiant : " + self.identifier + "\n" + \
               "Type : " + self.type + "\n" + \
               "Longueur : " + str(self.length) + "\n" + \
               "Données : " + ''.join(self.data) + "\n" + \
               "RSSI : " + str(self.rssi) + "dbm"

    def get_identifier(self):
        return self.identifier

    def get_type(self):
        return self.type

    def get_length(self):
        return self.length

    def get_data(self):
        return self.data

    def get_rssi(self):
        return self.rssi
