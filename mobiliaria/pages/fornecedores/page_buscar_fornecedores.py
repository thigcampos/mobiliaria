import tkinter as tk

from mobiliaria.backend.Model.fornecedor import Fornecedor
from mobiliaria.pages.base_page import Page


class PageBuscarFornecedores(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.data = tk.Listbox(self, width=100)

    def get_fornecedores(self):
        self._index = 1

        for fornecedor in Fornecedor.buscar_dados_fornecedores():
            self.data.insert(self._index, str(fornecedor))
            self._index += 1

        self.data.pack(expand=True)
