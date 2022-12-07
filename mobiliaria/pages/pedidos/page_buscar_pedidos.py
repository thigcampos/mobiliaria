import tkinter as tk

from mobiliaria.backend.Model.pedido import Pedido
from mobiliaria.pages.base_page import Page


class PageBuscaPedidos(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.data = tk.Listbox(self, width=100)

    def get_pedidos(self):
        self._index = 1

        for pedido in Pedido.buscar_pedidos():
            self.data.insert(self._index, str(pedido))
            self._index += 1

        self.data.pack(expand=True)
