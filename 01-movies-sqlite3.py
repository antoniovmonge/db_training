import sqlite3

# Create connection
connection = sqlite3.connect('movies.db')

# Create cursor
cursor = connection.cursor()

# Create a table
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Movies (
        Title TEXT,
        Director TEXT,
        Year INT
    )
    '''
)

connection.commit()
connection.close()
