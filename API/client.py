from os import system
from time import sleep
import mysql.connector

db = mysql.connector.connect(
    host="185.201.11.44",
    user="u257284371_iot",
    password="ansh1Rutu"
)

while True:
    pin = int(input('SELECT A GPIO CHANNEL: '))
    if pin not in [1, 14, 15] and pin < 28:
        MODE = int(input('ENTER MODE ANALOG(A) / DIGITAL(D):  '))
        state = int(input('ENTER STATE:  '))
        if MODE == 'A':
            print('digital_set_gpio({}, {})'.format(pin, state))
            digital_set_gpio(pin, state)
            print('DONE!')
            sleep(3)
        if MODE == 'D':
            print('analog_set_gpio({}, {})'.format(pin, state))
            analog_set_gpio(pin, state)
            print('DONE!')
            sleep(3)
    else:
        print("INVALID GPIO. IT DOESN'T EXIST\n"
              'TRY AGAIN')
        sleep(3)
        system('clear')