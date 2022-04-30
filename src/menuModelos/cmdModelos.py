'''
    Classes para:
        - Configurar janelas
        - Barra de menus
'''

import os
'''
from src.menuModelos.barras.barra1 import *
from src.menuModelos.barras.barra2 import *
from src.menuModelos.barras.barra3 import *
from src.menuModelos.barras.barra4 import *
from src.menuModelos.barras.barra5 import *
'''
from src.menuModelos.barras.barra6 import *
#from src.menuModelos.barras.barra7 import *
#from src.menuModelos.barras.barra8 import *


def criaJanBarras(app, titulo, textoImg, caminhoImg, numS, numD, numTC, numTP, numRele):
    #app = Tk()
    app.title(titulo)
    aux1 = os.getcwd() + '/ufsm-see.ico'
    aux = aux1.replace("\\", '/')
    diretorio = aux.replace('/', '//')
    app.iconbitmap(diretorio)

    Label(app, text=textoImg, font='Times 14 bold').pack()

    img = PhotoImage(file=caminhoImg)  # objeto imagem
    Label(app, image=img).pack(expand=YES, fill=BOTH)

    container2 = Elementos()
    Label(app, text='Elementos:', font='Times 12 bold').pack(anchor=NW)
    container2.criaBotoesCheck(app, numS, numD, numTC, numTP, numRele)

    container3 = Frame()
    Button(container3, text='Energizar', command=app.destroy).pack(side=LEFT)
    Button(container3, text='Fechar', command=app.destroy).pack(side=RIGHT)

    #app.mainloop()


class ComandosParaJanelasModelos():

    def semComando(self):
        pass

    def AbrirBar1(self):
        self.app = Tk()
        self.titulo = "Barramento Simples"
        self.app.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.minsize(width=300, height=200)



        self.app.mainloop()

    def AbrirBar2(self):
        self.app = Tk()
        self.titulo = "Barramento Simples com Barra de Transferência"
        self.app.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.minsize(width=300, height=200)



        self.app.mainloop()

    def AbrirBar3(self):
        self.app = Tk()
        self.titulo = "Barramento Simples com Seccionamento de Barra"
        self.app.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.minsize(width=300, height=200)



        self.app.mainloop()

    def AbrirBar4(self):
        self.app = Tk()
        self.titulo = "Barramento Simples com Geração Auxiliar"
        self.app.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.minsize(width=300, height=200)



        self.app.mainloop()

    def AbrirBar5(self):
        self.app = Tk()
        self.titulo = "Barramento Duplo a Quatro Chaves"
        self.app.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.minsize(width=300, height=200)



        self.app.mainloop()

    def AbrirBar6(self):
        self.app = Tk()
        self.titulo = "Barramento Disjuntor Duplo"
        self.app.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.minsize(width=300, height=200)

        self.Jan6 = JanBar6()
        self.Jan6.configBar6(self.app, self.titulo)

        self.app.mainloop()

    def AbrirBar7(self):
        self.app = Tk()
        self.titulo = "Barramento Duplo e Disjuntor e Meio"
        self.app.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.minsize(width=300, height=200)



        self.app.mainloop()

    def AbrirBar8(self):
        self.app = Tk()
        self.titulo = "Barramento em Anel"
        self.app.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.minsize(width=300, height=200)



        self.app.mainloop()