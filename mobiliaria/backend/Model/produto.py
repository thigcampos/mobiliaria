import sqlite3

from mobiliaria.backend.Banco.open_db_connection import connect_db

from .utils.gerar_sql_insert import gerar_sql_insert_produto


# Classe Produto
class Produto:
    # Funcoes da classe que são definidas aparticar de açoes do produto
    # Funções definem as ações, ou seja, o que a classe faz
    def criar_produto(
        nome_produto,
        categoria,
        preco,
        descricao,
        estoque,
        ficha_tecnica,
        id_fornecedor,
    ):
        try:
            conn, cursor = connect_db()
            cursor.execute(
                gerar_sql_insert_produto(
                    nome_produto,
                    categoria,
                    preco,
                    descricao,
                    estoque,
                    ficha_tecnica,
                    id_fornecedor,
                )
            )

            # Salvando no banco de dados
            conn.commit()
            print("Produto Inserido!")

        except Exception as e:
            print("erro", e)
            conn.close()

    def buscar_dados_produto():
        # Busca todos os dados de todos os clientes e exibe no terminal
        try:
            conn, cursor = connect_db()
            # Lendo os dados e apresentando na
            cursor.execute(
                """
            SELECT * FROM produtos;
            """
            )

            produtos = []
            for linha in cursor.fetchall():
                produtos.append(linha)

            # Fechando a conexão como banco de dados
            conn.close()
            print("Todos os dados de 'produto' buscados")
            return produtos
        except Exception as e:
            print("erro", e)
            conn.close()

    def buscar_dados_estoque():
        # Busca  todos os pedidos e exibe no terminal
        try:
            conn, cursor = connect_db()
            produtos = {}
            cursor.execute(
                """
                SELECT categoria, sum(estoque) FROM produtos GROUP BY categoria;
                """
            )
            for linha in cursor.fetchall():
                produtos[linha[0]]=linha[1]            
            # Fechando a conexão como banco de dados
            conn.close()
            print("Os dados do estoque foram buscados!")
            return produtos
        except:
            print("Erro: não foi possível realizar a busca")
            conn.close()

    def atualizar_dados_produto(estoque, id_produto):
        # Atualiza os dados daquele cliente especificado pelo cpf
        try:
            conn, cursor = connect_db()
            cursor.execute(
                """
            UPDATE produtos 
            SET estoque = ? 
            WHERE id_produto = ?;
            """,
                (estoque, id_produto),
            )

            # Salvando no banco de dados
            conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()
            print("Dados de 'produto' atualizados")
        except Exception as e:
            conn, cursor = connect_db()
            print("erro")
            conn.close()

    def deletar_produto(id_produto):
        # Deleta os dados daquele cliente especificado pelo cpf
        try:
            conn, cursor = connect_db()
            cursor.execute(
                """
                DELETE FROM produtos
                WHERE id_produto = ?
                """,
                (id_produto,),
            )

            # Salvando no banco de dados
            conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()
            print("Dados de 'produto' deletados")
        except Exception as e:
            print("erro")
            conn.close()
