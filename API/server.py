from os import system, name
from time import sleep
import mysql.connector

db = mysql.connector.connect(
    host="185.201.11.44",
    user="u257284371_iot",
    password="ansh1Rutu"
)
cursor  = db.cursor()