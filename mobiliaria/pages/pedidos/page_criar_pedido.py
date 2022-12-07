import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.pedido import Pedido
from mobiliaria.pages.base_page import Page


class CriarPedido(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # valor total
        self.valor_total = tk.ttk.Label(self, text="Valor Total:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.valor_total_strvar = tk.StringVar()
        self.valor_total_entrada = tk.ttk.Entry(
            self, textvariable=self.valor_total_strvar
        ).grid(row=0, column=1)
        # data do pedido
        self.data_pedido = tk.ttk.Label(self, text="Data do Pedido:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.data_pedido_strvar = tk.StringVar()
        self.data_pedido_entrada = tk.ttk.Entry(
            self, textvariable=self.data_pedido_strvar
        ).grid(row=1, column=1)

        # quantidade de produto
        self.qtde_produto = tk.ttk.Label(self, text="Quantidade:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        self.qtde_produto_strvar = tk.StringVar()
        self.qtde_produto_entrada = tk.ttk.Entry(
            self, textvariable=self.qtde_produto_strvar
        ).grid(row=2, column=1)

        # id produto
        self.id_produto = tk.ttk.Label(self, text="ID do Produto:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        self.id_produto_strvar = tk.StringVar()
        self.id_produto_entrada = tk.ttk.Entry(
            self, textvariable=self.id_produto_strvar
        ).grid(row=3, column=1)

        # id cliente
        self.id_cliente = tk.ttk.Label(self, text="ID do Cliente:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)
        self.id_cliente_strvar = tk.StringVar()
        self.id_cliente_entrada = tk.ttk.Entry(
            self, textvariable=self.id_cliente_strvar
        ).grid(row=4, column=1)

        self.button_sub = tk.ttk.Button(
            self, text="Salvar", command=self.insert_in_db
        ).grid(row=5, column=1, sticky=tk.E, pady=5)

    def insert_in_db(self):
        try:
            valor_total = float(self.valor_total_strvar.get())
            data_pedido = self.data_pedido_strvar.get()
            qtde_produto = int(self.qtde_produto_strvar.get())
            id_produto = int(self.id_produto_strvar.get())
            id_cliente = int(self.id_cliente_strvar.get())

            # print(valor_total, data_pedido, type(data_pedido), qtde_produto, id_produto, id_cliente)
            Pedido.criar_pedido(
                valor_total, data_pedido, qtde_produto, id_produto, id_cliente
            )
        except ValueError as e:
            showerror(title="ERRO", message=e)
