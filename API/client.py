from os import system
from time import sleep
import mysql.connector

db = mysql.connector.connect(
    host="185.201.11.44",
    user="u257284371_iot",
    password="ansh1Rutu"
)


def digital_set_gpio(gpio_id, state):
    if not db.is_connected():
        print('DATABASE TIMED OUT. RECONNECTING......')
        db.reconnect(attempts=2, delay=0)
    cursor = db.cursor()
    cursor.execute("UPDATE u257284371_iot.MESSAGES SET RESPONSE = 'CHANGED: {}' WHERE ID = 1;".format(str(gpio_id)))
    cursor.execute("UPDATE u257284371_iot.GPIO_STREAM SET DIGITAL_STATUS = {} WHERE GPIO_ID = {};".format(str(state),
                                                                                                          str(gpio_id)))
    cursor.execute("UPDATE u257284371_iot.GPIO_STREAM SET PWM_STATUS = NULL WHERE GPIO_ID = {};".format(str(gpio_id)))
    cursor.execute("UPDATE u257284371_iot.MESSAGES SET RESPONSE = 'D' WHERE ID = 2;")
    cursor.close()
    db.commit()


def analog_set_gpio(gpio_id, value):
    if not db.is_connected():
        print('DATABASE TIMED OUT. RECONNECTING......')
        db.reconnect(attempts=2, delay=0)
    cursor = db.cursor()
    cursor.execute("UPDATE u257284371_iot.MESSAGES SET RESPONSE = 'CHANGED: {}' WHERE ID = 1;".format(str(gpio_id)))
    cursor.execute("UPDATE u257284371_iot.GPIO_STREAM SET PWM_STATUS = {} WHERE GPIO_ID = {};".format(str(state),
                                                                                                      str(gpio_id)))
    cursor.execute(
        "UPDATE u257284371_iot.GPIO_STREAM SET DIGITAL_STATUS = NULL WHERE GPIO_ID = {};".format(str(gpio_id)))
    cursor.execute("UPDATE u257284371_iot.MESSAGES SET RESPONSE = 'A' WHERE ID = 2;")
    cursor.close()
    db.commit()


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