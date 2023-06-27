from connection import PostgreSQLConnector
import psycopg2

class DataImporter:
    def __init__(self, menu_file, sales_file):
        self.menu_file = menu_file
        self.sales_file = sales_file
        self.db_connection = PostgreSQLConnector()
        self.db_connection.connect()

    def import_data(self):
        conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")
        cur = conn.cursor()

        # menu.csv insertion
        with open(self.menu_file, 'r') as m:
            next(m)
            cur.copy_from(m, 'menu', sep=',')

        # sales.csv insertion
        with open(self.sales_file, 'r') as s:
            next(s)
            cur.copy_from(s, 'sales', sep=',')

        conn.commit()
        cur.close()
        conn.close()

# Usage
menu_file_path = '/Users/aayushabista/Assignment1_Python/data/menu.csv'
sales_file_path = '/Users/aayushabista/Assignment1_Python/data/sales.csv'

data_importer = DataImporter(menu_file_path, sales_file_path)
data_importer.import_data()

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
