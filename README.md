# WMBus Frame Processing

This project is designed to capture Wireless Meter Bus (WMBus) frames from an Enless receiver, process those frames using the `trame.py` class file, and display the results in the console. There are three main files included in this project:

- `trame.py`: This file contains the `Trame` class, which is used for processing the received frames.
- `main.py`: This file is used to get the frames from the receiver using a serial port.
- `tester.py`: This file can be used to test the `trame.py` file without having to use a serial port with a static frame.

The results of the processing are displayed in the console. However they are written in french.
Give me your discord if you want to help translate the results to english, or any other language.

## Prerequisites

- Python 3.11 or higher
- A WMBus receiver
- Some WMBus transmitters
- A computer with a serial port
- MariaDB with the good database (`BDD.sql`)

## Getting Started

To begin with, you will need to install Python 3.9 or higher on your computer. You can download the latest version of Python from the [Python website](https://www.python.org/downloads/).

You then need to download the Enless A.I.R application from the [Enless website](https://enless-wireless.com/en/download-center/) and configure the Receiver as you need.

When everything is ready, you can clone this repository to your local machine and run the `main.py` file to start capturing frames.

If the USB port is not the same for you, feel free to modify `main.py` to select the right serial port (example: tty\USB0 on linux | Use `sudo dmesg | grep tty`)

Before anything you will have to install mariadb with the right database, the database is given in the repository, you can import the database using the file `BDD.sql`

```sh
git clone https://github.com/SCFOrga/WMBusFrame.git
cd WMBusFrame
python main.py
```

## Usage

To use this project, simply run the `main.py` file and wait for the frames to be captured. The frames will be displayed in the console as they are received, and the Trame class will be used to process the frames and display the results.

You can modify the serial values in the `main.py` file to suit your needs. For example, you can change the baud rate, parity, or stop bits. Simply open the main.py file in a text editor and modify the values as desired.

You can also use the `tester.py` file to test the `trame.py` file without having to use a serial port. Simply run the `tester.py` file and the static frame will be processed and the results will be displayed in the console and uploaded onto the database.

## Credits

This project was created by [Akariiinnn](https://github.com/Akariiinnn) and is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).
