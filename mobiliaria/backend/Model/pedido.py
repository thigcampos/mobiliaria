import sqlite3
from datetime import datetime

from mobiliaria.backend.Banco.open_db_connection import connect_db

from .utils.gerar_sql_insert import gerar_sql_insert_pedido


# Classe Pedido
class Pedido:
    # Funções da classe pedido
    @staticmethod
    def criar_pedido(
        valor_total,
        data_pedido,
        qtde_produto,
        id_produto,
        id_cliente,
    ):
        try:
            conn, cursor = connect_db()
            cursor.execute(
                gerar_sql_insert_pedido(
                    valor_total,
                    data_pedido,
                    qtde_produto,
                    id_produto,
                    id_cliente,
                )
            )

            # Salvando no banco de dados
            conn.commit()
            print("Pedido inserido!")

        except Exception as e:
            print("Erro: Não foi possivel realizar essa ação\n", e)
            conn.close()

    @staticmethod
    def buscar_pedidos():
        # Busca  todos os pedidos e exibe no terminal
        try:
            conn, cursor = connect_db()
            cursor.execute(
                """
            SELECT * FROM pedidos;
            """
            )
            pedidos = [pedido for pedido in cursor.fetchall()]

            # Fechando a conexão como banco de dados
            conn.close()
            print("Todos os pedidos foram buscados!")
            return pedidos
        except:
            print("Erro: não foi possível realizar a busca")
            conn.close()

    @staticmethod
    def buscar_pedidos_por_mes():
        # Busca  todos os pedidos e exibe no terminal
        meses = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        try:
            conn, cursor = connect_db()
            pedidos = {}
            for mes in meses:
                cursor.execute(
                    """
                    SELECT sum(valor_total) FROM pedidos WHERE data_pedido LIKE '%-{teste}-%';
                    """.format(teste=mes)
                )
                for item in cursor.fetchall():
                    if item[0] == None:
                        pedidos[mes]=0
                    else:
                        pedidos[mes]=item[0]
            
            # Fechando a conexão como banco de dados
            conn.close()
            # print("Todos os pedidos foram buscados!")
            return pedidos
        except:
            print("Erro: não foi possível realizar a busca")
            conn.close()

    @staticmethod
    def atualizar_dados_pedido(valor_total, id_pedido):
        # Atualiza os dados daquele cliente especificado pelo cpf
        try:
            conn, cursor = connect_db()
            cursor.execute(
                """
            UPDATE pedidos 
            SET valor_total = ? 
            WHERE id_pedido = ?;
            """,
                (valor_total, id_pedido),
            )

            # Salvando no banco de dados
            conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()
            print("Os dados desse pedido foram atualizados")
        except Exception as e:
            print("Erro", e)
            conn.close()

    @staticmethod
    def deletar_pedido(id_pedido):
        # Deleta os dados daquele cliente especificado pelo cpf
        try:
            conn, cursor = connect_db()
            cursor.execute(
                """
                DELETE FROM pedidos
                WHERE id_pedido = ?
                """,
                (id_pedido,),
            )

            # Salvando no banco de dados
            conn.commit()
            # Fechando a conexão como banco de dados
            conn.close()
            print("Pedido deletado!")
        except Exception as e:
            print("Erro: Não foi possivel executar essa ação", e)
            conn.close()


# Pedido.criar_pedido(100.0, "1234", 10, 1, 1)
