import psycopg2
from python.config import config

class PostgreSQLConnector:
    def __init__(self):
        self.conn = None

    def connect(self):
        """ Connect to the PostgreSQL database server """
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)
            
            # create a cursor
            cur = self.conn.cursor()
            
            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
            
            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')


if __name__ == '__main__':
    pg_connector = PostgreSQLConnector()
    pg_connector.connect()
