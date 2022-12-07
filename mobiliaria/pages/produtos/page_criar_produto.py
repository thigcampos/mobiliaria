import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.produto import Produto
from mobiliaria.pages.base_page import Page


class PageCriarProduto(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.nome_produto = tk.ttk.Label(self, text="Nome:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.nome_produto_strvar = tk.StringVar()
        self.nome_produto_entrada = tk.ttk.Entry(
            self, textvariable=self.nome_produto_strvar
        ).grid(row=0, column=1)

        self.categoria = tk.ttk.Label(self, text="Categoria:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.categoria_strvar = tk.StringVar()
        self.categoria_entrada = tk.ttk.Entry(
            self, textvariable=self.categoria_strvar
        ).grid(row=1, column=1)

        # quantidade de produto
        self.preco = tk.ttk.Label(self, text="Preço:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        self.preco_strvar = tk.StringVar()
        self.preco_entrada = tk.ttk.Entry(self, textvariable=self.preco_strvar).grid(
            row=2, column=1
        )

        # id produto
        self.descricao = tk.ttk.Label(self, text="Descrição:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        self.descricao_strvar = tk.StringVar()
        self.descricao_entrada = tk.ttk.Entry(
            self, textvariable=self.descricao_strvar
        ).grid(row=3, column=1)

        # id cliente
        self.estoque = tk.ttk.Label(self, text="Estoque:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)
        self.estoque_strvar = tk.StringVar()
        self.estoque_entrada = tk.ttk.Entry(self, textvariable=self.estoque_strvar).grid(
            row=4, column=1
        )

        self.ficha_tecnica = tk.ttk.Label(self, text="Ficha Técnica:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)
        self.ficha_tecnica_strvar = tk.StringVar()
        self.ficha_tecnica_entrada = tk.ttk.Entry(
            self, textvariable=self.ficha_tecnica_strvar
        ).grid(row=5, column=1)

        self.id_fornecedor = tk.ttk.Label(self, text="ID Fornecedor:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=10)
        self.id_fornecedor_strvar = tk.StringVar()
        self.id_fornecedor_entrada = tk.ttk.Entry(
            self, textvariable=self.id_fornecedor_strvar
        ).grid(row=6, column=1)

        self.button_sub = tk.ttk.Button(self, text="Salvar", command=self.insert).grid(
            row=9, column=1, sticky=tk.E, pady=5
        )

    def insert(self):
        try:
            nome_produto = self.nome_produto_strvar.get()
            categoria = self.categoria_strvar.get()
            preco = float(self.preco_strvar.get())
            descricao = self.descricao_strvar.get()
            estoque = int(self.estoque_strvar.get())
            ficha_tecnica = self.ficha_tecnica_strvar.get()
            id_fornecedor = int(self.id_fornecedor_strvar.get())

            Produto.criar_produto(
                nome_produto,
                categoria,
                preco,
                descricao,
                estoque,
                ficha_tecnica,
                id_fornecedor,
            )

        except Exception as e:
            print(e)
