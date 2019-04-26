import sqlite3

connection = sqlite3.connect('master.db', check_same_thread=False)
cursor = connection.cursor()


cursor.execute('''CREATE TABLE cities(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name VARCHAR,
    city_location VARCHAR,
    );''')

cursor.execute('''parks(
    park_id INTEGER PRIMARY KEY AUTOINCREMENT,
    park_name VARCHAR,
    park_location VARCHAR,
    park_city VARCHAR,
    FOREIGN KEY (park_city) REFERENCES state(city_name)
    );''')




cursor.execute('''patients(
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    age VARCHAR,
    treatment VARCHAR
    );''')

cursor.execute('''doctors(
    doctors_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    specialty VARCHAR,
    office_address VARCHAR,
    office_phone VARCHAR
    );''')



connection.commit()
cursor.close()