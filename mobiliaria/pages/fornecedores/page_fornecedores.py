import tkinter as tk

from mobiliaria.pages.base_page import Page

from .page_atualizar_fornecedor import PageAtualizarFornecedor
from .page_buscar_fornecedores import PageBuscarFornecedores
from .page_criar_fornecedor import PageCriarFornecedor
from .page_deletar_fornecedor import PageDeletarFornecedor


class PageFornecedores(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.page_criar_fornecedor = PageCriarFornecedor(self)
        self.page_buscar_fornecedores = PageBuscarFornecedores(self)
        self.page_atualizar_fornecedor = PageAtualizarFornecedor(self)
        self.page_deletar_fornecedor = PageDeletarFornecedor(self)
        self.widgets_to_forget = [
            self.page_criar_fornecedor,
            self.page_buscar_fornecedores,
            self.page_atualizar_fornecedor,
            self.page_deletar_fornecedor,
        ]

        # Criando Frame de Cabeçalho
        headerFrame=tk.Frame(self)
        headerFrame.pack(side="top")

        # Título do Frame
        title = tk.ttk.Label(headerFrame, text='Fornecedores', font=("Helvetica", 20))
        title.pack(side="top", fill="y", expand=True, ipady=10, anchor="w")

        # Botão de Buscar
        tk.ttk.Button(
            headerFrame,
            text="Buscar Fornecedores",
            command=lambda: [self.go_busca(), self.page_buscar_fornecedores.get_fornecedores()],
        ).pack(padx=5, pady=15, side=tk.LEFT)

        # Botão de Criar
        tk.ttk.Button(headerFrame, text="Criar Fornecedor", command=self.go_criar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        # Botão de Editar
        tk.ttk.Button(headerFrame, text="Atualizar Fornecedor", command=self.go_atualizar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        # Botão de Deletar
        tk.ttk.Button(headerFrame, text="Deletar Fornecedor", command=self.go_deletar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        # Frame Inicial
        self.page_criar_fornecedor.pack()

    def __forget_widgets(self):
        for widget in self.widgets_to_forget:
            widget.pack_forget()

    def go_busca(self):
        self.__forget_widgets()
        self.page_buscar_fornecedores.pack()

    def go_criar(self):
        self.__forget_widgets()
        self.page_criar_fornecedor.pack()

    def go_atualizar(self):
        self.__forget_widgets()
        self.page_atualizar_fornecedor.pack()

    def go_deletar(self):
        self.__forget_widgets()
        self.page_deletar_fornecedor.pack()
