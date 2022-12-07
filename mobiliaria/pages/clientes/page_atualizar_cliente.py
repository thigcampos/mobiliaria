import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.cliente import Cliente
from mobiliaria.pages.base_page import Page


class PageAtualizarCliente(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.nome_cliente = tk.ttk.Label(self, text="Nome do Cliente:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.nome_cliente_strvar = tk.StringVar()
        self.nome_cliente_entrada = tk.ttk.Entry(
            self, textvariable=self.nome_cliente_strvar
        ).grid(row=0, column=1)

        self.cpf = tk.ttk.Label(self, text="CPF:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.cpf_strvar = tk.StringVar()
        self.cpf_entrada = tk.ttk.Entry(self, textvariable=self.cpf_strvar).grid(
            row=1, column=1
        )

        self.update_button = tk.ttk.Button(
            self, text="Atualizar", command=self.update
        ).grid(row=2, column=1, sticky=tk.E, pady=5)

    def update(self):
        try:
            nome = self.nome_cliente_strvar.get()
            cpf_cliente = self.cpf_strvar.get()

            Cliente.atualizar_dados_clientes(nome, cpf_cliente)
        except Exception as e:
            showerror(title="Erro", message=e)
