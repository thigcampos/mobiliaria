# Importando o banco de dados para utiliza-lo
# import sqlite3
# from sqlite3 import Error

# def create_connection():
#     conn = None
#     try:
#         conn = sqlite3.connect('mobiliario.db')
#         return conn
#     except Error as e:
#         print(e)

#     return conn


# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     :return:
#     """
#     try:
#         cursor = conn.cursor()
#         cursor.execute(create_table_sql)
#     except Error as e:
#         print(e)
