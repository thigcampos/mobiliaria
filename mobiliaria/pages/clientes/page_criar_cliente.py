import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.cliente import Cliente
from mobiliaria.pages.base_page import Page


class PageCriarCliente(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.nome_cliente = tk.ttk.Label(self, text="Nome cliente:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.nome_cliente_strvar = tk.StringVar()
        self.nome_cliente_entrada = tk.ttk.Entry(
            self, textvariable=self.nome_cliente_strvar
        ).grid(row=0, column=1)
        # data do pedido
        self.cpf = tk.ttk.Label(self, text="CPF:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.cpf_strvar = tk.StringVar()
        self.cpf_entrada = tk.ttk.Entry(self, textvariable=self.cpf_strvar).grid(
            row=1, column=1
        )

        # quantidade de produto
        self.data_nascimento = tk.ttk.Label(self, text="Data de Nascimento:").grid(
            row=2, column=0, sticky=tk.W, padx=10, pady=10
        )
        self.data_nascimento_strvar = tk.StringVar()
        self.data_nascimento_entrada = tk.ttk.Entry(
            self, textvariable=self.data_nascimento_strvar
        ).grid(row=2, column=1)

        # id produto
        self.email = tk.ttk.Label(self, text="Email:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        self.email_strvar = tk.StringVar()
        self.email_entrada = tk.ttk.Entry(self, textvariable=self.email_strvar).grid(
            row=3, column=1
        )

        # id cliente
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

        self.button_sub = tk.ttk.Button(
            self, text="Salvar", command=self.insert_in_db
        ).grid(row=9, column=1, sticky=tk.E, pady=5)

    def insert_in_db(self):
        try:
            nome_cliente = self.nome_cliente_strvar.get()
            cpf = self.cpf_strvar.get()
            data_nascimento = self.data_nascimento_strvar.get()
            email = self.email_strvar.get()
            telefone = self.telefone_strvar.get()
            logradouro = self.logradouro_strvar.get()
            cep = self.cep_strvar.get()
            numero = int(self.numero_strvar.get())
            complemento = self.complemento_strvar.get()

            Cliente.criar_cliente(
                nome_cliente,
                cpf,
                data_nascimento,
                email,
                telefone,
                logradouro,
                cep,
                numero,
                complemento,
            )

        except ValueError as e:
            showerror(title="Erro", message=e)
