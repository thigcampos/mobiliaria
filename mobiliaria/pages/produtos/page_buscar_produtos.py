import tkinter as tk

from mobiliaria.backend.Model.produto import Produto
from mobiliaria.pages.base_page import Page


class PageBuscaProdutos(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.data = tk.Listbox(self, width=100)

    def get_produtos(self):
        self._index = 1

        for produto in Produto.buscar_dados_produto():
            self.data.insert(self._index, str(produto))
            self._index += 1

        self.data.pack(expand=True)
