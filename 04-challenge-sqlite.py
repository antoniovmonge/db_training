import sqlite3

connection = sqlite3.connect('users-sqlite.db')

cursor = connection.cursor()

# ----------------------------------
# FIRST STEP

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email_address TEXT
    )
    '''
)
# ---------------------------------

# SECOND STEP

fiveUsers = [
    ('Taliban','Pachacho','taliban@explota.com'),
    ('Jibiri', 'Jibiri', 'jibiri@jibiri.com'),
    ('Rafaela', 'Carra', 'mexplota@mexplota.mexplo'),
    ('Donald', 'Trump', 'subnormal@naranja.com'),
    ('Otro', 'Pachacho', 'please@stop.ya')
]

cursor.executemany(
    '''
    INSERT INTO Users(first_name, last_name, email_address) VALUES (?, ?, ?)
    ''', fiveUsers)

# records = cursor.execute("SELECT * FROM Users")

# print(cursor.fetchall())

# for record in records:
#     print(record)

# ---------------------------------

cursor.execute(
    '''
    SELECT email_address FROM Users
    '''
)
print(cursor.fetchall())

cursor.execute('SELECT * FROM Users')
print(cursor.fetchall())

connection.commit()
connection.close()
