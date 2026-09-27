import sqlite3
import csv


# The following script will populate the tables in jpcafe.db with
# data from the appropriate text files

db = sqlite3.connect('jpcafev2.db')

inventory = open('inventory.txt', 'r')
for line in inventory:
    line = line.strip()
    line = line.split(',')
    db.execute('''INSERT INTO Inventory VALUES (?,?,?,?,?,?)''',
               (line[0], line[1], line[2], line[3], line[4], line[5]))
    db.commit()
inventory.close()


with open('member.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    for line in csv_reader:
        db.execute('INSERT INTO Member VALUES' +
                   '(?,true,?,?)', (line[0], line[1], line[2]))
        db.commit()
