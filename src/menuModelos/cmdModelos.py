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


def criaJanBarras(janBar, titulo, textoImg, caminhoImg, numS, numD, numTC, numTP, numRele):
    #janBar = Tk()
    janBar.title(titulo)
    aux1 = os.getcwd() + '/ufsm-see.ico'
    aux = aux1.replace("\\", '/')
    diretorio = aux.replace('/', '//')
    janBar.iconbitmap(diretorio)

    Label(janBar, text=textoImg, font='Times 14 bold').pack()

    img = PhotoImage(file=caminhoImg)  # objeto imagem
    Label(janBar, image=img).pack(expand=YES, fill=BOTH)

    container2 = Elementos()
    Label(janBar, text='Elementos:', font='Times 12 bold').pack(anchor=NW)
    container2.criaBotoesCheck(janBar, numS, numD, numTC, numTP, numRele)

    container3 = Frame()
    Button(container3, text='Energizar', command=janBar.destroy).pack(side=LEFT)
    Button(container3, text='Fechar', command=janBar.destroy).pack(side=RIGHT)

    #janBar.mainloop()


class ComandosParaJanelasModelos():

    def semComando(self):
        pass

    def AbrirBar1(self):
        self.janBar = Tk()
        self.titulo = "Barramento Simples"
        self.janBar.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.janBar.iconbitmap(self.diretorio)
        self.janBar.minsize(width=300, height=200)



        self.janBar.mainloop()

    def AbrirBar2(self):
        self.janBar = Tk()
        self.titulo = "Barramento Simples com Barra de Transferência"
        self.janBar.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.janBar.iconbitmap(self.diretorio)
        self.janBar.minsize(width=300, height=200)



        self.janBar.mainloop()

    def AbrirBar3(self):
        self.janBar = Tk()
        self.titulo = "Barramento Simples com Seccionamento de Barra"
        self.janBar.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.janBar.iconbitmap(self.diretorio)
        self.janBar.minsize(width=300, height=200)



        self.janBar.mainloop()

    def AbrirBar4(self):
        self.janBar = Tk()
        self.titulo = "Barramento Simples com Geração Auxiliar"
        self.janBar.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.janBar.iconbitmap(self.diretorio)
        self.janBar.minsize(width=300, height=200)



        self.janBar.mainloop()

    def AbrirBar5(self):
        self.janBar = Tk()
        self.titulo = "Barramento Duplo a Quatro Chaves"
        self.janBar.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.janBar.iconbitmap(self.diretorio)
        self.janBar.minsize(width=300, height=200)



        self.janBar.mainloop()

    def AbrirBar6(self, janBar):
        self.container = Frame(janBar)
        self.titulo = "Barramento Disjuntor Duplo"
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')

        self.Jan6 = JanBar6()
        self.Jan6.configBar6(self.janBar, self.titulo)

    def AbrirBar7(self):
        self.janBar = Tk()
        self.titulo = "Barramento Duplo e Disjuntor e Meio"
        self.janBar.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.janBar.iconbitmap(self.diretorio)
        self.janBar.minsize(width=300, height=200)



        self.janBar.mainloop()

    def AbrirBar8(self):
        self.janBar = Tk()
        self.titulo = "Barramento em Anel"
        self.janBar.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.janBar.iconbitmap(self.diretorio)
        self.janBar.minsize(width=300, height=200)



        self.janBar.mainloop()