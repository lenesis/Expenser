#Lenesis
import sqlite3
import datetime
from tabulate import tabulate
dbase = sqlite3.connect('expenser.db')
c = dbase.cursor()
def init():
    with dbase:
        c.execute('''CREATE TABLE IF NOT EXISTS spentdata (
            amount INTEGER,
            category TEXT COLLATE NOCASE,
            messege TEXT,
            dateandtime TEXT)''')


def addSpent(amount, category, messege=''):
    with dbase:
        dateandtime = datetime.datetime.now().strftime('%Y - %m - %d | %H:%M')
        c.execute('INSERT INTO spentdata VALUES (:amount, :category, :messege, :datentime)', {'amount' : amount, 'category' : category, 'messege' : messege, 'datentime' : dateandtime})

def showSpent(category=None):
    if category:
        c.execute('SELECT * FROM spentdata WHERE category = :category', {'category' : category})
        results = c.fetchall()
        c.execute('SELECT sum(amount) FROM spentdata WHERE category = :category', {'category' : category})
        total = c.fetchone()[0]
    else:
        c.execute('SELECT * FROM spentdata')
        results = c.fetchall()
        c.execute('SELECT sum(amount) FROM spentdata')
        total = c.fetchone()[0]
    return total, results
    dbase.close()

