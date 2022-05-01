import os
from src.menuModelos.manobrasBarras import *
from tkinter import *
from PIL import ImageTk, Image

class JanBar6:
    def configBar6(self, toplevel, status):
        self.cavidade = Frame(toplevel)
        self.cavidade.pack()


        image = PhotoImage(file='src/menuModelos/barras/img/bar6.png')  # objeto imagem
        #Button(toplevel, text = '  ', image = image).pack(side = TOP)
        Label(toplevel, image=image).pack(expand=YES, fill=BOTH)

        self.operacoes = Button(self.cavidade, text='B3').pack(side=LEFT)

        Label(toplevel, text=status, bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)
