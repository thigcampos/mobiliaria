import tkinter as tk

from mobiliaria.pages.base_page import Page
from mobiliaria.backend.Model.produto import Produto

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



class PageGraficosProduto(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # Figure
        fig = Figure(figsize = (6,6), dpi = 85)
        subplot = fig.add_subplot(111)
        subplot.set_title('Estoque por Categoria')
        # Valores do estoque são armazenados em estoque 
        estoque = self.get_dados()
        # Escala de X
        subplot.set_xticklabels(list(estoque.keys()),fontsize=8)
        # Escala de Y
        subplot.set_yticks(list(estoque.values()))
        # Legenda do eixo X
        subplot.set_ylabel('Qtde. Estoque')
        # Legenda do eixo Y
        subplot.set_xlabel('Categorias')
        # Plot define os pontos seguindo o plano cartesiano 
        # subplot.plot(list(estoque.keys()), list(estoque.values()))
        subplot.bar(list(estoque.keys()), list(estoque.values()))
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        get_widz = canvas.get_tk_widget()
        get_widz.pack(ipadx=75, ipady=30)
    
    def get_dados(self):
        dados = Produto.buscar_dados_estoque()
        return dados
        
