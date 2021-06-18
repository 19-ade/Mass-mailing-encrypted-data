import sqlite3

# creating the database
conn = sqlite3.connect('mass_mailing.db')

# create a cursor for database
cursor = conn.cursor()


# create table

def creation():
    cursor.execute(" CREATE TABLE mail_list(\n"

                   "    Name text,\n"
                   "    Email text,\n"
                   "    DOB integer\n"
                   "   )")


# NULL, INTEGER, REAL , TEXT, BLOB(IMAGES, MP3 FILE)
# cursor.fetchall() to return all the queries in a list


def input_(name, email, dob):  # function to append new data into table
    cursor.execute("INSERT INTO mail_list VALUES (?, ?, ?)", [name, email, dob])
    conn.commit()


def delete_(query, column):  # function to delete data based on column
    if column == 'DOB':

        cursor.execute("DELETE FROM mail_list WHERE DOB = ? ", (query,))
    elif column == 'Email':
        cursor.execute("DELETE FROM mail_list WHERE Email = ? ", (query,))
    elif column == 'Name':
        cursor.execute("DELETE FROM mail_list WHERE Name = ? ", (query,))
    conn.commit()


def get_query():  # function returns the contents of the table
    cursor.execute("SELECT * FROM mail_list")
    l = cursor.fetchall()

    return l

def view_specific(query, column):
    if column == 'DOB':

        cursor.execute("SELECT rowid, * FROM mail_list WHERE DOB = ? ", (query,))
    elif column == 'Email':
        cursor.execute("SELECT rowid, * FROM mail_list WHERE Email = ? ", (query,))
    elif column == 'Name':
        cursor.execute("SELECT rowid, * FROM mail_list WHERE Name = ? ", (query,))
    l = cursor.fetchall()
    return l


def view_specific(query, column):
    if column == 'DOB':

        cursor.execute("SELECT rowid, * FROM mail_list WHERE DOB = ? ", (query,))
    elif column == 'Email':
        cursor.execute("SELECT rowid, * FROM mail_list WHERE Email = ? ", (query,))
    elif column == 'Name':
        cursor.execute("SELECT rowid, * FROM mail_list WHERE Name = ? ", (query,))
    l = cursor.fetchall()
    return l


def reset():  # Deletes all data in the table
    cursor.execute("DELETE FROM mail_list")
    conn.commit()


def initialize():  # initializes data with default dataset.
    array = [
        ("Anwesan de", 'f20190518@hyderabad.bits-pilani.ac.in', 19092000),
        ("Aditya Goyal", 'wdenny@gmail.com', 12042001),
        ("Abhinav gupta", 'f20190380@hyderabad.bits-pilani.ac.in', 16012000),
        ('Nirav jayesh parmar', 'f20190540@hyderabad.bits-pilani.ac.in', 7022002)

    ]
    cursor.executemany("INSERT INTO mail_list VALUES (?, ?, ?)", array)
    conn.commit()


# reset()
# creation()
#initialize()
#print(get_query())
#print(view_specific(16012000, 'DOB'))
