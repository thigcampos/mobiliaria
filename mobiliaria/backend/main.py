# main

# Modelos de Classes - utilizar o paradigma de orientação a objetos.
# Utilizar o banco de dados relacional Sqlite.
# Efetuar o tratamento de erros (try/except/finally).
# Criar Menu de opções.
# Utilizar diversos tipos de dados, além de tuplas, listas e dicionários.
# Estruturas de repetição, decisão.
# Funções, Lambda, Compreensão de listas.
# Utilizar cores, formatação.
# Efetuar o CRUD em todas as tabelas.
# Gerar um gráfico utilizando o módulo externo matplotlib.
# Criar a lógica necessária para atender ao tema.
# Otimizar o código utilizando os recursos da linguagem python.

# Tutorial SQLITE: https://www.sqlitetutorial.net/sqlite-python/
# Gerenciador de BD - DBBrowser: https://sqlitebrowser.org/

import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("mobiliario.db")
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    sql_create_table_clientes = """ CREATE TABLE IF NOT EXISTS clientes (
                                        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nome_cliente VARCHAR(120) NOT NULL,
                                        cpf VARCHAR(15) NOT NULL,
                                        data_nascimento TEXT NOT NULL, 
                                        email VARCHAR(100) NOT NULL,
                                        telefone VARCHAR(20) NOT NULL,
                                        logradouro TEXT NOT NULL,
                                        cep VARCHAR(9) NOT NULL,
                                        numero INTEGER NOT NULL,
                                        complemento VARCHAR(50)
                                    ); """

    sql_create_table_fornecedores = """CREATE TABLE IF NOT EXISTS fornecedores (
                                        id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT, 
                                        nome_fornecedor TEXT NOT NULL,
                                        cnpj_fornecedor VARCHAR(15) NOT NULL, 
                                        email VARCHAR(100) NOT NULL,
                                        telefone VARCHAR(20) NOT NULL,
                                        cep VARCHAR(9) NOT NULL,
                                        logradouro TEXT NOT NULL,
                                        numero INTEGER NOT NULL,
                                        complemento VARCHAR(50)
                                    );"""

    sql_create_table_produtos = """ CREATE TABLE IF NOT EXISTS produtos(
                                        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nome_produto VARCHAR(25) NOT NULL,
                                        categoria TEXT NOT NULL,
                                        preco FLOAT NOT NULL,
                                        descricao TEXT NOT NULL, 
                                        estoque INTEGER NOT NULL, 
                                        ficha_tecnica TEXT NOT NULL,
                                        id_fornecedor INTEGER,
                                        foreign key (id_fornecedor) references fornecedores(id_fornecedor)
                                );"""
    sql_create_table_pedidos = """ CREATE TABLE IF NOT EXISTS pedidos(
                                        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                                        valor_total FLOAT NOT NULL, 
                                        data_pedido VARCHAR(11) NOT NULL,
                                        qtde_produto INTEGER, 
                                        id_produto INTEGER NOT NULL,
                                        id_cliente INTEGER NOT NULL,
                                        foreign key (id_produto) references produtos(id_produto),
                                        foreign key (id_cliente) references clientes(id_cliente)
                                );"""

    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_table_clientes)
        create_table(conn, sql_create_table_fornecedores)
        create_table(conn, sql_create_table_produtos)
        create_table(conn, sql_create_table_pedidos)
        print("Tabelas criadas com sucesso!")

    else:
        print("Error! cannot create the database connection.")


if __name__ == "__main__":
    main()
