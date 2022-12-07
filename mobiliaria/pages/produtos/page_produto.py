import tkinter as tk

from mobiliaria.pages.base_page import Page
from .page_grafico_produto import PageGraficosProduto
from .page_atualizar_produto import PageAtualizarProduto
from .page_buscar_produtos import PageBuscaProdutos
from .page_criar_produto import PageCriarProduto
from .page_deletar_produto import PageDeletarProduto


class PageProduto(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.page_criar_produto = PageCriarProduto(self)
        self.page_grafico_produto = PageGraficosProduto(self)
        self.page_atualizar_produto = PageAtualizarProduto(self)
        self.page_busca_produtos = PageBuscaProdutos(self)
        self.page_deletar_produto = PageDeletarProduto(self)

        self.widgets_to_forget = [
            self.page_criar_produto,
            self.page_grafico_produto,
            self.page_atualizar_produto,
            self.page_busca_produtos,
            self.page_deletar_produto,
        ]

        headerFrame=tk.Frame(self)
        headerFrame.pack(side="top")

        # Título do Frame
        title = tk.Label(headerFrame, text='Produtos', font=("Helvetica", 20))
        title.pack(side="top", fill="y", expand=True, ipady=10, anchor="w")

        # Botão de Gráficos
        tk.ttk.Button(headerFrame, text="Gráfico", command=self.go_chart).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        tk.ttk.Button(
            headerFrame,
            text="Buscar Produtos",
            command=lambda: [self.go_busca(), self.page_busca_produtos.get_produtos()],
        ).pack(padx=5, pady=15, side=tk.LEFT)

        tk.ttk.Button(headerFrame, text="Criar Produto", command=self.go_criar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        tk.ttk.Button(headerFrame, text="Atualizar Produto", command=self.go_atualizar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        tk.ttk.Button(headerFrame, text="Deletar Produto", command=self.go_deletar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        self.page_grafico_produto.pack()

    def __forget_widgets(self):
        for widget in self.widgets_to_forget:
            widget.pack_forget()

    def go_busca(self):
        self.__forget_widgets()
        self.page_busca_produtos.pack()

    def go_chart(self):
        self.__forget_widgets()
        self.page_grafico_produto.pack()


    def go_atualizar(self):
        self.__forget_widgets()
        self.page_atualizar_produto.pack()

    def go_deletar(self):
        self.__forget_widgets()
        self.page_deletar_produto.pack()

    def go_criar(self):
        self.__forget_widgets()
        self.page_criar_produto.pack()
