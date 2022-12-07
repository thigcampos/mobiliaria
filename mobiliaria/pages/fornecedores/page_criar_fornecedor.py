import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.fornecedor import Fornecedor
from mobiliaria.pages.base_page import Page


class PageCriarFornecedor(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.nome_fornecedor = tk.ttk.Label(self, text="Nome do Fornecedor:").grid(
            row=0, column=0, sticky=tk.W, padx=10, pady=10
        )
        self.nome_fornecedor_strvar = tk.StringVar()
        self.nome_fornecedor_entrada = tk.ttk.Entry(
            self, textvariable=self.nome_fornecedor_strvar
        ).grid(row=0, column=1)

        self.cnpj_fornecedor = tk.ttk.Label(self, text="CNPJ do Fornecedor:").grid(
            row=1, column=0, sticky=tk.W, padx=10, pady=10
        )
        self.cnpj_fornecedor_strvar = tk.StringVar()
        self.cnpj_fornecedor_entrada = tk.ttk.Entry(
            self, textvariable=self.cnpj_fornecedor_strvar
        ).grid(row=1, column=1)

        self.email = tk.ttk.Label(self, text="Email:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        self.email_strvar = tk.StringVar()
        self.email_entrada = tk.ttk.Entry(self, textvariable=self.email_strvar).grid(
            row=3, column=1
        )

        self.telefone = tk.ttk.Label(self, text="Telefone:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)
        self.telefone_strvar = tk.StringVar()
        self.telefone_entrada = tk.ttk.Entry(self, textvariable=self.telefone_strvar).grid(
            row=4, column=1
        )

        self.logradouro = tk.ttk.Label(self, text="Logradouro:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)
        self.logradouro_strvar = tk.StringVar()
        self.logradouro_entrada = tk.ttk.Entry(
            self, textvariable=self.logradouro_strvar
        ).grid(row=5, column=1)

        self.cep = tk.ttk.Label(self, text="CEP:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=10)
        self.cep_strvar = tk.StringVar()
        self.cep_entrada = tk.ttk.Entry(self, textvariable=self.cep_strvar).grid(
            row=6, column=1
        )

        self.numero = tk.ttk.Label(self, text="Número:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=10)
        self.numero_strvar = tk.StringVar()
        self.numero_entrada = tk.ttk.Entry(self, textvariable=self.numero_strvar).grid(
            row=7, column=1
        )

        self.complemento = tk.ttk.Label(self, text="Complemento:").grid(row=8, column=0, sticky=tk.W, padx=10, pady=10)
        self.complemento_strvar = tk.StringVar()
        self.complemento_entrada = tk.ttk.Entry(
            self, textvariable=self.complemento_strvar
        ).grid(row=8, column=1)

        self.button_sub = tk.ttk.Button(self, text="Salvar", command=self.insert).grid(
            row=9, column=1, sticky=tk.E, pady=5
        )

    def insert(self):
        try:
            nome_fornecedor = self.nome_fornecedor_strvar.get()
            cnpj_fornecedor = self.cnpj_fornecedor_strvar.get()
            email = self.email_strvar.get()
            telefone = self.telefone_strvar.get()
            logradouro = self.logradouro_strvar.get()
            cep = self.cep_strvar.get()
            numero = int(self.numero_strvar.get())
            complemento = self.complemento_strvar.get()

            Fornecedor.criar_fornecedor(
                nome_fornecedor,
                cnpj_fornecedor,
                email,
                telefone,
                cep,
                logradouro,
                numero,
                complemento,
            )
        except ValueError as e:
            showerror(title="Erro", message=e)

