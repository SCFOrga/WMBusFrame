"""
Tester for the class Trame in trame.py
"""

from trame import Trame
from mysqlol import insert_data


def main():
    tel = "68 19 44 AE 0C 10 11 11 11 01 07 7A 6B 00 00 00 2F 2F 0F 7F 27 27 01 67 01 01 6C 16"
    telesplit = tel.split(' ')
    trame = Trame(telesplit)
    print(trame)


if __name__ == '__main__':
    main()
