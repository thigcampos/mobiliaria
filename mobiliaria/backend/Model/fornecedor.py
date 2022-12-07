import sqlite3

from mobiliaria.backend.Banco.open_db_connection import connect_db

from .utils.gerar_sql_insert import *


# Classe Cliente
class Fornecedor:
    # Funções definem as ações, ou seja, o que a classe faz
    @staticmethod
    def criar_fornecedor(
        nome_fornecedor,
        cnpj_fornecedor,
        email,
        telefone,
        cep,
        logradouro,
        numero,
        complemento,
    ):
        try:
            conn, cursor = connect_db()
            cursor.execute(
                gerar_sql_insert_fornecedor(
                    nome_fornecedor,
                    cnpj_fornecedor,
                    email,
                    telefone,
                    cep,
                    logradouro,
                    numero,
                    complemento,
                )
            )
            # Salvando no banco de dados
            conn.commit()
            print("Fornecedor Inserido!")

        except:
            print("erro")
            conn.close()

    def buscar_dados_fornecedores():
        # Busca todos os dados de todos os clientes e exibe no terminal
        try:
            # Lendo os dados e apresentando na
            conn, cursor = connect_db()
            cursor.execute(
                """
            SELECT * FROM fornecedores;
            """
            )

            fornecedores = []
            for linha in cursor.fetchall():
                fornecedores.append(linha)

            # Salvando no banco de dados
            # conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()
            print("Todos os dados de 'fornecedores' buscados")
            return fornecedores
        except:
            print("erro")
            conn.close()

    def atualizar_dados_fornecedores(nome, cnpj_fornecedor):
        # Atualiza os dados daquele cliente especificado pelo cpf
        try:
            conn, cursor = connect_db()
            cursor.execute(
                """
            UPDATE fornecedores 
            SET nome_fornecedor = ? 
            WHERE cnpj_fornecedor = ?;
            """,
                (nome, cnpj_fornecedor),
            )

            # Salvando no banco de dados
            conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()
            print("Dados de 'fornecedores' atualizados")
        except:
            print("erro")
            conn.close()

    def deletar_fornecedor(cnpj_fornecedor):
        # Deleta os dados daquele cliente especificado pelo cpf
        try:
            conn, cursor = connect_db()
            cursor.execute(
                """
                DELETE FROM fornecedores
                WHERE cnpj_fornecedor = ?
                """,
                (cnpj_fornecedor,),
            )

            # Salvando no banco de dados
            conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()
            print("Dados de 'fornecedores' deletados")
        except:
            print("erro")
            conn.close()


# Fornecedor.criar_fornecedor(
#     "Thiago",
#     "12345678",
#     "thiagomoveistop@email.com",
#     "40028922",
#     "12345",
#     "Rua Japônes que Vai Dar Playstation",
#     3,
#     "bom dia",
# )

# Fornecedor.buscar_dados_fornecedores()

# Fornecedor.atualizar_dados_fornecedores("Henrique", "12345678")

# Fornecedor.deletar_clientes("12345678")
