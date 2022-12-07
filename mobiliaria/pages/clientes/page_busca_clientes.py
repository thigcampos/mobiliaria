import tkinter as tk

from mobiliaria.backend.Model.cliente import Cliente
from mobiliaria.pages.base_page import Page


class PageBuscaClientes(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.data = tk.Listbox(self, width=75)

    def get_clientes(self):
        self._index = 1

        for cliente in Cliente.buscar_dados_clientes():
            self.data.insert(self._index, str(cliente))
            self._index += 1

        self.data.pack(side="bottom", fill="x", expand=False)
