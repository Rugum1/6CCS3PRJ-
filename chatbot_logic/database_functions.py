
import sqlite3
import pandas


class DbFunctions:

    def connect_to_the_database(self,database_file):
        connection = None
        try:
            connection = sqlite3.connect(database_file)
            return connection
        except Exception as e:
            print(e)
        return connection

    def create_new_databse_table(self,sql):
        connection = self.connect_to_the_database('database.sqlite3')

        cursor = connection.cursor()
        cursor.execute(sql)
        print("Table created succesfully")
        connection.commit()
        connection.close()

    def insert_elements_in_database(self,table_name,file_name):
        connection = self.connect_to_the_database('database.sqlite3')
        df  = pandas.read_csv(file_name)
        df2 = df.dropna()
        df2.to_sql(table_name,connection, if_exists = 'append',index = False)
        connection.close()
        print("Elements inserted succesfully")

    def create_new_table(self,sql):
        connection = self.connect_to_the_database('database.sqlite3')
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("Table created succesfully")


    def select_term_from_db(self,sql,name):

        connection = self.connect_to_the_database('database.sqlite3')
        cursor = connection.cursor()
        cursor.execute(sql,(name,))


        row = cursor.fetchone()
        connection.close()
        return row[0]
