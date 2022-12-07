import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.pedido import Pedido
from mobiliaria.pages.base_page import Page


class PageDeletarpedido(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.id_pedido = tk.ttk.Label(self, text="ID do Pedido:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.id_pedido_strvar = tk.StringVar()
        self.id_pedido_entrada = tk.ttk.Entry(
            self, textvariable=self.id_pedido_strvar
        ).grid(row=1, column=1)

        self.delete_button = tk.ttk.Button(
            self, text="Deletar", command=self.delete
        ).grid(row=2, column=1, sticky=tk.E, pady=5)

    def delete(self):
        try:
            id_pedido = int(self.id_pedido_strvar.get())

            Pedido.deletar_pedido(id_pedido)
        except Exception as e:
            showerror(title="Erro", message=e)