import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.produto import Produto
from mobiliaria.pages.base_page import Page


class PageDeletarProduto(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.id_produto = tk.ttk.Label(self, text="ID do Produto:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.id_produto_strvar = tk.StringVar()
        self.id_produto_entrada = tk.ttk.Entry(
            self, textvariable=self.id_produto_strvar
        ).grid(row=1, column=1)

        self.delete_button = tk.ttk.Button(
            self, text="Deletar", command=self.delete
        ).grid(row=2, column=1, sticky=tk.E, pady=5)

    def delete(self):
        try:
            id_produto = int(self.id_produto_strvar.get())

            Produto.deletar_produto(id_produto)
        except Exception as e:
            showerror(title="Erro", message=e)
