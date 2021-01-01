from os import system, name
from time import sleep
import mysql.connector

db = mysql.connector.connect(
    host="185.201.11.44",
    user="u257284371_iot",
    password="ansh1Rutu"
)
cursor  = db.cursor()



def rpi_operate_gpio(pin, status, mode):
    # process raspberry pi gpio

    # update changes after operating gpio
    print('PIN: GPIO ' + str(pin) + '\nSTATUS: ' + str(status) + '\nMODE: ' + str(mode) + '\n')

    cursor.execute("UPDATE u257284371_iot.MESSAGES SET RESPONSE = 'UNCHANGED' WHERE ID = 1")
    db.commit()
    print('saved changes')



while True:
    cursor.execute("SELECT RESPONSE FROM u257284371_iot.MESSAGES WHERE ID = 1;")
    response = cursor.fetchone()
    db.commit()
    if response[0].startswith('CHANGED'):
        detect_change(response[0])
        print('buffering')
        sleep(5)
        system('clear')

    else:
        # print(response[0])
        sleep(1.5)