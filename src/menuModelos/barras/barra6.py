import os
from src.menuModelos.manobrasBarras import *
from tkinter import *

class JanBar6:
    def configBar6(self, app, status):
        self.cavidade = Frame(app)
        self.cavidade.pack()

        self.image = PhotoImage(file='src/menuModelos/barras/img/bar6.png')  # objeto imagem
        Label(app, image=self.image).pack(expand=YES, fill=BOTH)

        self.operacoes = Button(self.cavidade, text='B3').pack(side=LEFT)

        Label(app, text=status, bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)
