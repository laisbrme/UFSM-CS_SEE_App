'''
    Barramento Simples - Manobra no Disjuntor
'''

from tkinter import *
from __init__ import *
import os

class barra1:
    def manobra1(self):
        self.app = Tk()
        app.title("Barramento Simples - Manobra no Disjuntor")
        aux1 = os.getcwd() + '/ufsm-see.ico'
        aux = aux1.replace("\\", '/')
        diretorio = aux.replace('/', '//')
        app.iconbitmap(diretorio)

        Label(app, text='BARRAMENTO SIMPLES', font='Times 14 bold').pack()

        Scrollbar(app).pack()

        container1 = Config()
        container2 = Elementos()
        manobra    = Manobras()

        container1.imagem(app, caminho='1.png')
        Label(app, text='Elementos:', font='Times 12 bold').pack(anchor=NW)
        container2.criaBotoesCheck(app, numS=10, numD=5, numTC=4, numTP=1, numRele=1)

        container3 = Frame()
        Button(container3, text='Energizar', command=manobra.avisoSemComando()).pack(side=LEFT)
        Button(container3, text='Fechar', command=app.destroy).pack(side=RIGHT)

        app.mainloop()