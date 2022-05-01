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


def criaJanBarras(toplevel, titulo, textoImg, caminhoImg, numS, numD, numTC, numTP, numRele):
    #toplevel = Tk()
    toplevel.title(titulo)
    aux1 = os.getcwd() + '/ufsm-see.ico'
    aux = aux1.replace("\\", '/')
    diretorio = aux.replace('/', '//')
    toplevel.iconbitmap(diretorio)

    Label(toplevel, text=textoImg, font='Times 14 bold').pack()

    img = PhotoImage(file=caminhoImg)  # objeto imagem
    Label(toplevel, image=img).pack(expand=YES, fill=BOTH)

    container2 = Elementos()
    Label(toplevel, text='Elementos:', font='Times 12 bold').pack(anchor=NW)
    container2.criaBotoesCheck(toplevel, numS, numD, numTC, numTP, numRele)

    container3 = Frame()
    Button(container3, text='Energizar', command=toplevel.destroy).pack(side=LEFT)
    Button(container3, text='Fechar', command=toplevel.destroy).pack(side=RIGHT)

    #toplevel.mainloop()


class ComandosParaJanelasModelos():

    def semComando(self):
        pass

    def AbrirBar1(self):
        self.toplevel = Tk()
        self.titulo = "Barramento Simples"
        self.toplevel.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.toplevel.iconbitmap(self.diretorio)
        self.toplevel.minsize(width=300, height=200)



        self.toplevel.mainloop()

    def AbrirBar2(self):
        self.toplevel = Tk()
        self.titulo = "Barramento Simples com Barra de Transferência"
        self.toplevel.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.toplevel.iconbitmap(self.diretorio)
        self.toplevel.minsize(width=300, height=200)



        self.toplevel.mainloop()

    def AbrirBar3(self):
        self.toplevel = Tk()
        self.titulo = "Barramento Simples com Seccionamento de Barra"
        self.toplevel.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.toplevel.iconbitmap(self.diretorio)
        self.toplevel.minsize(width=300, height=200)



        self.toplevel.mainloop()

    def AbrirBar4(self):
        self.toplevel = Tk()
        self.titulo = "Barramento Simples com Geração Auxiliar"
        self.toplevel.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.toplevel.iconbitmap(self.diretorio)
        self.toplevel.minsize(width=300, height=200)



        self.toplevel.mainloop()

    def AbrirBar5(self):
        self.toplevel = Tk()
        self.titulo = "Barramento Duplo a Quatro Chaves"
        self.toplevel.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.toplevel.iconbitmap(self.diretorio)
        self.toplevel.minsize(width=300, height=200)



        self.toplevel.mainloop()

    def AbrirBar6(self):
        self.toplevel = Tk()
        self.titulo = "Barramento Disjuntor Duplo"
        self.toplevel.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.toplevel.iconbitmap(self.diretorio)
        self.toplevel.minsize(width=300, height=200)

        self.Jan6 = JanBar6()
        self.Jan6.configBar6(self.toplevel, self.titulo)

        self.toplevel.mainloop()

    def AbrirBar7(self):
        self.toplevel = Tk()
        self.titulo = "Barramento Duplo e Disjuntor e Meio"
        self.toplevel.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.toplevel.iconbitmap(self.diretorio)
        self.toplevel.minsize(width=300, height=200)



        self.toplevel.mainloop()

    def AbrirBar8(self):
        self.toplevel = Tk()
        self.titulo = "Barramento em Anel"
        self.toplevel.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.toplevel.iconbitmap(self.diretorio)
        self.toplevel.minsize(width=300, height=200)



        self.toplevel.mainloop()