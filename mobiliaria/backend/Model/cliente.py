import sqlite3
from datetime import datetime

from mobiliaria.backend.Banco.open_db_connection import connect_db

from .utils.gerar_sql_insert import *


# Classe Cliente
class Cliente:
    # Funções definem as ações, ou seja, o que a classe faz
    @staticmethod
    def criar_cliente(
        nome_cliente,
        cpf,
        data_nascimento,
        email,
        telefone,
        logradouro,
        cep,
        numero,
        complemento,
    ):
        try:
            conn, cursor = connect_db()
            cursor.execute(
                gerar_sql_insert_cliente(
                    nome_cliente,
                    cpf,
                    data_nascimento,
                    telefone,
                    email,
                    cep,
                    logradouro,
                    numero,
                    complemento,
                )
            )

            # Salvando no banco de dados
            conn.commit()
            print("Cliente Inserido!")

        except Exception as e:
            print("Erro: cliente não criado\n", e)
            conn.close()

    @staticmethod
    def buscar_dados_clientes():
        # Busca todos os dados de todos os clientes e exibe no terminal
        try:
            conn, cursor = connect_db()
            # Lendo os dados e apresentando na
            cursor.execute(
                """
            SELECT * FROM clientes;
            """
            )

            clientes = []
            for linha in cursor.fetchall():
                clientes.append(linha)

            # Salvando no banco de dados
            # conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()

            print("Todos os dados de 'clientes' buscados")
            return clientes

        except Exception as e:
            print("erro: não foi possível realizar a busca")
            conn.close()

    @staticmethod
    def atualizar_dados_clientes(nome, cpf_cliente):
        # Atualiza os dados daquele cliente especificado pelo cpf
        try:
            conn, cursor = connect_db()
            cursor.execute(
                """
            UPDATE clientes 
            SET nome_cliente = ? 
            WHERE cpf = ?;
            """,
                (nome, cpf_cliente),
            )

            # Salvando no banco de dados
            conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()
            print("Dados de 'clientes' atualizados")
        except Exception as e:
            print("erro")
            conn.close()

    @staticmethod
    def deletar_clientes(cpf_cliente):
        # Deleta os dados daquele cliente especificado pelo cpf
        try:
            conn, cursor = connect_db()
            cursor.execute(
                """
                DELETE FROM clientes
                WHERE cpf = ?
                """,
                (cpf_cliente,),
            )

            # Salvando no banco de dados
            conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()
            print("Cliente deletado")
        except Exception as e:
            print("erro")
            conn.close()


# Cliente.criar_cliente(
#     "emyle",
#     "12345678910",
#     datetime.now(),
#     "email@email.email",
#     "40028922",
#     "rua",
#     "cep",
#     "2",
#     "sim",
# )

# Cliente.buscar_dados_clientes()

# Cliente.atualizar_dados_clientes('Thiago', '12345678910')

# Cliente.deletar_clientes("12345678910")
