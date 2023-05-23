#!/usr/local/bin/python3.11
"""
Tester for the class Trame in trame.py
"""

from trame import Trame
from mysqlol import insert_data, list_data, count_id


def main():
    tel = "68 20 44 ae 0c 20 38 52 11 01 07 7a 65 00 00 00 2f 2f 0f 7f 04 04 01 46 00 00 00 28 00 00 00 33 01 34 16"
    telesplit = tel.split(' ')
    trame = Trame(telesplit)
    count_id()
    print(trame)


if __name__ == '__main__':
    main()