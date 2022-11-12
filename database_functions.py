
import sqlite3




def connect_to_the_database(database_file):
    connection = None
    try:
        connection = sqlite3.connect(database_file)
        return connection
    except Exception as e:
        print(e)
    return connection

def create_new_databse_table(sql):
    connection = connect_to_the_database('database.sqlite3')

    cursor = connection.cursor()
    cursor.execute(sql)
    print("Table created succesfully")
    connection.commit()
    connection.close()

def insert_elements_in_database(sql, data):

    sql = "INSERT INTO CS_TERM VALUES {}".format(elements)
    for element in data:




sql = '''CREATE TABLE CS_TERM(
   NAME CHAR(100) NOT NULL,
   DESCRIPTION VARCHAR NOT NULL
)'''
create_new_databse_table(sql)
