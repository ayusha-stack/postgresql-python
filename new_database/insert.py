from new_database.connection import PostgreSQLConnector
import psycopg2

class InsertValue:
    def __init__(self):
        self.connection = PostgreSQLConnector()
        
        self.connection.connect()

    def insert_sql_from_file(self,filename):
        try:
            with open(filename, "r") as insert_sql_file:
                insert_sql = insert_sql_file.read()
                self.connection.cursor.execute(insert_sql)
                self.connection.connection.commit() #calling of the connection class 
                print("Values created successfully!")

        #for the exception case need to add this line         
        except FileNotFoundError:
            print(f"'the {filename}' was not found")

        except psycopg2.Error as error:
            print("Error while connecting to Postgresql:", error)


        def disconnect(self):
            self.connection.disconnect()