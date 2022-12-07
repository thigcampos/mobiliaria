import tkinter as tk

from mobiliaria.pages.base_page import Page
from .page_grafico import PageGraficosPedido
from .page_atualizar_pedido import PageAtualizarPedido
from .page_buscar_pedidos import PageBuscaPedidos
from .page_criar_pedido import CriarPedido
from .page_deletar_pedido import PageDeletarpedido

class PagePedidos(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.page_grafico_pedidos = PageGraficosPedido(self)
        self.criar_pedido = CriarPedido(self)
        self.page_busca_pedidos = PageBuscaPedidos(self)
        self.page_atualizar_pedido = PageAtualizarPedido(self)
        self.page_deletar_pedido = PageDeletarpedido(self)
        self.widgets_to_forget = [
            self.criar_pedido,
            self.page_grafico_pedidos,
            self.page_busca_pedidos,
            self.page_atualizar_pedido,
            self.page_deletar_pedido
        ]

        # Criando Frame de Cabeçalho
        headerFrame=tk.Frame(self)
        headerFrame.pack(side="top")

        # Título do Frame
        title = tk.ttk.Label(headerFrame, text='Pedidos', font=("Helvetica", 20))
        title.pack(side="top", fill="y", expand=True, ipady=10, anchor="w")

        # Botão de Gráficos
        tk.ttk.Button(headerFrame, text="Gráfico", command=self.go_chart).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        # Botão de Buscar
        tk.ttk.Button(
            headerFrame,
            text="Buscar Pedidos",
            command=lambda: [self.go_busca(), self.page_busca_pedidos.get_pedidos()],
        ).pack(padx=5, pady=15, side=tk.LEFT)

        # Botão de Criar
        tk.ttk.Button(headerFrame, text="Criar Pedido", command=self.go_criar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        # Botão de Editar
        tk.ttk.Button(headerFrame, text="Atualizar Pedido", command=self.go_atualizar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        # Botão de Deletar
        tk.ttk.Button(headerFrame, text="Deletar Pedido", command=self.go_deletar).pack(
            padx=5, pady=15, side=tk.LEFT
        )

        # Frame Inicial
        self.page_grafico_pedidos.pack()


    def __forget_widgets(self):
        for widget in self.widgets_to_forget:
            widget.pack_forget()

    def go_busca(self):
        self.__forget_widgets()
        self.page_busca_pedidos.pack()

    def go_chart(self):
        self.__forget_widgets()
        self.page_grafico_pedidos.pack()

    def go_atualizar(self):
        self.__forget_widgets()
        self.page_atualizar_pedido.pack()

    def go_deletar(self):
        self.__forget_widgets()
        self.page_deletar_pedido.pack()

    def go_criar(self):
        self.__forget_widgets()
        self.criar_pedido.pack()