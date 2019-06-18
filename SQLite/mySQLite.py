import sqlite3
import time
import datetime

# region Establish a connection
conn = sqlite3.connect('tutorial.db')
cursor = conn.cursor()
# endregion

def create_table():
    # Run the SQL commands
    cursor.execute('CREATE TABLE IF NOT EXISTS user (id VARCHAR(20) PRIMARY KEY,\
                   name VARCHAR(128), course VARCHAR(128), datastamp TEXT)')

def data_entry():
    # Run the SQL commands
    cursor.execute("INSERT INTO user VALUES ('1', 'double Z', 'Python', '2019-06-18')")

    # region Commit and Close the connection
    conn.commit()
    cursor.close()
    conn.close()
    # endregion



if __name__=='__main__':
    create_table()
    # data_entry()
    # more_data()
    read_from_db()
