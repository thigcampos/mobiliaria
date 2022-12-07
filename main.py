import tkinter as tk
from tkinter import Frame, Text, Tk, ttk
import sv_ttk

from mobiliaria.pages import (PageClientes, PageFornecedores, PagePedidos,
                              PageProduto)


class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        # Páginas
        page_produto = PageProduto(self)
        page_clientes = PageClientes(self)
        page_pedidos = PagePedidos(self)
        page_fornecedores = PageFornecedores(self)

        button_frame = Frame(self)
        container = Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        page_produto.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        page_clientes.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        page_pedidos.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        page_fornecedores.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # Menu
        menubar = tk.Menu(root)
        menubar.add_command(label="Pedidos", command=page_pedidos.show)
        menubar.add_command(label="Produtos", command=page_produto.show)
        menubar.add_command(label="Clientes", command=page_clientes.show)
        menubar.add_command(label="Fornecedores", command=page_fornecedores.show)
        root.config(menu=menubar)

        page_pedidos.show()


if __name__ == "__main__":
    root = Tk()
    root.title('Sistema de Mobiliaria')
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("900x600")
    sv_ttk.set_theme("light")
    root.mainloop()
