from connection import PostgreSQLConnector
import psycopg2


class CreateTable:
    def __init__(self):
        self.db_connection = PostgreSQLConnector()
        self.db_connection.connect()

    def create_sql_from_file(self,filename):
        try:
            with open(filename, "r") as create_sql_file:
                create_sql = create_sql_file.read()
                self.db_connection.cursor.execute(create_sql)
                self.db_connection.PostgreSQLConnector.commit() # classing connection from another file
                print("Tables created successfully!")
        except FileNotFoundError:
            print(f"'the {filename}' is not found")

        except psycopg2.Error as error:
            print("Error while connecting to Postgres:", error)

        def disconnect(self):
            self.db_connection.disconnect()