import pandas as pd
import numpy as np
import psycopg2
import config as cf
# import config as cf


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(database=cf.database_name,
                                           host=cf.database_host,
                                           user=cf.database_username,
                                           password=cf.database_password,
                                           port=cf.database_port)

    def connection_db(self):
        # test connection to db
        if self.connection.is_connected():
            db_info = self.connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
        else:
            print("Don't connected to MySQl Server")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        print(cursor)
        cursor.execute(query)
        print("Done execute query!")
        result = cursor.fetchall()
        return result

    def execute_query_pandas(self, query):
        sql_query = pd.read_sql_query(query, self.connection)
        df = pd.DataFrame(sql_query)
        return df

    def max_ind(self, table, column):
        query = 'select max({}) from {}'.format(column, table)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insert_db(self, query, value):
        cursor = self.connection.cursor()
        cursor.execute(query, value)
        self.connection.commit()
        print("Done insert into query!")

    def create_table(self, query):
        cursor = self.connection.cursor()
        print(cursor)
        cursor.execute(query)
        self.connection.commit()
