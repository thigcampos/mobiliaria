import tkinter as tk

from mobiliaria.pages.base_page import Page
from mobiliaria.backend.Model.pedido import Pedido

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



class PageGraficosPedido(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # Figure
        fig = Figure(figsize = (5,5), dpi = 77)
        subplot = fig.add_subplot(111)
        subplot.set_title('Vendas por mês')
        # Valores das vendas são armazenados em vendas 
        vendas = self.get_dados()
        # Escala de X
        subplot.set_xticks(list(vendas.keys()))
        # Escala de Y
        subplot.set_yticks(list(vendas.values()))
        # Legenda do eixo X
        subplot.set_xlabel('Mês')
        # Legenda do eixo Y
        subplot.set_ylabel('Vendas (em reais)')
        # Plot define os pontos seguindo o plano cartesiano 
        # subplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        subplot.plot(list(vendas.keys()), list(vendas.values()))
        # subplot.bar(list(vendas.keys()), list(vendas.values()))
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        get_widz = canvas.get_tk_widget()
        get_widz.pack(ipadx=75, ipady=30)
    
    def get_dados(self):
        dados = Pedido.buscar_pedidos_por_mes()
        return dados
        
