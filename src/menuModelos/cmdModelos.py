'''
    Classes para:
        - Configurar janelas
        - Barra de menus
'''

import os
from src.menuModelos.barra6 import *
from src.menuModelos.manobrasBarras import *

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
        print('Acesso na classe Modelos')

    def AbrirBar1(self):
        print('Acesso na classe Modelos')

    def AbrirBar2(self):
        pass

    def AbrirBar3(self):
        pass

    def AbrirBar4(self):
        pass

    def AbrirBar5(self):
        pass

    def AbrirBar6(self):
        print('Abrindo Barra 6')
        self.app = Tk()
        self.titulo = "Barramento Dijuntor Duplo"
        print(self.titulo)
        self.app.title(self.titulo)
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.mainloop()

    def AbrirBar7(self):
        pass

    def AbrirBar8(self):
        pass