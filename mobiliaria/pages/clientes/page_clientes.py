import tkinter as tk

from mobiliaria.pages.base_page import Page

from .page_atualizar_cliente import PageAtualizarCliente
from .page_busca_clientes import PageBuscaClientes
from .page_criar_cliente import PageCriarCliente
from .page_deletar_cliente import PageDeletarCliente


class PageClientes(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.page_criar_cliente = PageCriarCliente(self)

        self.page_buscar_clientes = PageBuscaClientes(self)
        self.page_atualizar_cliente = PageAtualizarCliente(self)
        self.page_deletar_cliente = PageDeletarCliente(self)

        self.widgets_to_forget = [
            self.page_criar_cliente,
            self.page_buscar_clientes,
            self.page_atualizar_cliente,
            self.page_deletar_cliente,
        ]
        
        headerFrame=tk.Frame(self)
        headerFrame.pack(side="top")

        # Título do Frame
        title = tk.ttk.Label(headerFrame, text='Clientes', font=("Helvetica", 20))
        title.pack(side="top", fill="y", expand=True, ipady=10, anchor="w")

        tk.ttk.Button(
            headerFrame,
            text="Buscar Clientes",
            command=lambda: [self.go_busca(), self.page_buscar_clientes.get_clientes()],
        ).pack(padx=5, pady=15, side=tk.LEFT)

        tk.ttk.Button(headerFrame, text="Criar Cliente", command=self.go_criar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        tk.ttk.Button(headerFrame, text="Atualizar Cliente", command=self.go_atualizar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        tk.ttk.Button(headerFrame, text="Deletar Cliente", command=self.go_deletar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        self.page_criar_cliente.pack()


    def __forget_widgets(self):
        for widget in self.widgets_to_forget:
            widget.pack_forget()

    def go_busca(self):
        self.__forget_widgets()
        self.page_buscar_clientes.pack()

    def go_criar(self):
        self.__forget_widgets()
        self.page_criar_cliente.pack()

    def go_atualizar(self):
        self.__forget_widgets()
        self.page_atualizar_cliente.pack()

    def go_deletar(self):
        self.__forget_widgets()
        self.page_deletar_cliente.pack()
