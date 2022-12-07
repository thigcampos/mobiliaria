import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.produto import Produto
from mobiliaria.pages.base_page import Page


class PageAtualizarProduto(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.id_produto = tk.ttk.Label(self, text="ID do Produto:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.id_produto_strvar = tk.StringVar()
        self.id_produto_entrada = tk.ttk.Entry(
            self, textvariable=self.id_produto_strvar
        ).grid(row=0, column=1)

        self.estoque = tk.ttk.Label(self, text="Estoque:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.estoque_strvar = tk.StringVar()
        self.estoque_entrada = tk.ttk.Entry(
            self, textvariable=self.estoque_strvar
        ).grid(row=1, column=1)

        self.update_button = tk.ttk.Button(
            self, text="Atualizar", command=self.update
        ).grid(row=2, column=1, sticky=tk.E, pady=5)

    def update(self):
        try:
            estoque = self.estoque_strvar.get()
            id_produto = int(self.id_produto_strvar.get())

            Produto.atualizar_dados_produto(estoque, id_produto)
        except Exception as e:
            showerror(title="Erro", message=e)
