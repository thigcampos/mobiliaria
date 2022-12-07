import tkinter as tk
from tkinter.messagebox import showerror

from mobiliaria.backend.Model.fornecedor import Fornecedor
from mobiliaria.pages.base_page import Page


class PageDeletarFornecedor(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.cnpj_fornecedor = tk.ttk.Label(self, text="CNPJ do Fornecedor:").grid(
            row=1, column=0, sticky=tk.W, padx=10, pady=10
        )
        self.cnpj_fornecedor_strvar = tk.StringVar()
        self.cnpj_fornecedor_entrada = tk.ttk.Entry(
            self, textvariable=self.cnpj_fornecedor_strvar
        ).grid(row=1, column=1)

        self.delete_button = tk.ttk.Button(
            self, text="Deletar", command=self.delete
        ).grid(row=2, column=1, sticky=tk.E, pady=5)

    def delete(self):
        try:
            cnpj_fornecedor = self.cnpj_fornecedor_strvar.get()
            Fornecedor.deletar_fornecedor(cnpj_fornecedor)
        except Exception as e:
            showerror(title="Erro", message=e)
