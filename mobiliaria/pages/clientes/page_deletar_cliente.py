import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.cliente import Cliente
from mobiliaria.pages.base_page import Page


class PageDeletarCliente(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.cpf = tk.ttk.Label(self, text="CPF:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.cpf_strvar = tk.StringVar()
        self.cpf_entrada = tk.ttk.Entry(self, textvariable=self.cpf_strvar).grid(
            row=1, column=1
        )

        self.delete_button = tk.ttk.Button(
            self, text="Deletar", command=self.delete
        ).grid(row=2, column=1, sticky=tk.E, pady=5)

    def delete(self):
        try:
            cpf_cliente = self.cpf_strvar.get()

            Cliente.deletar_clientes(cpf_cliente)
        except Exception as e:
            showerror(title="Erro", message=e)
