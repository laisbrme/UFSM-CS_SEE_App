'''
    Barramento Simples - Manobra no Disjuntor
'''

from tkinter import *
from __init__ import *
import os

class barra1:
    def manobra1(self):
        self.self.app = Tk()
        self.app.title("Barramento Simples - Manobra no Disjuntor")
        self.self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)

        Label(self.app, text='BARRAMENTO SIMPLES', font='Times 14 bold').pack()

        Scrollbar(self.app).pack()

        container1 = Config()
        container2 = Elementos()
        manobra    = Manobras()

        container1.imagem(self.app, caminho='b1.png')
        Label(self.app, text='Elementos:', font='Times 12 bold').pack(anchor=NW)
        container2.criaBotoesCheck(self.app, numS=10, numD=5, numTC=4, numTP=1, numRele=1)

        container3 = Frame()
        Button(container3, text='Energizar', command=manobra.avisoSemComando()).pack(side=LEFT)
        Button(container3, text='Fechar', command=self.app.destroy).pack(side=RIGHT)

        self.app.mainloop()