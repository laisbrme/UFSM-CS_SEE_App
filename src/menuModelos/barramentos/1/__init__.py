'''
    Classe de funções para as manobras dos barramentos.
'''

from tkinter import *


class Config:

    def imagem(self, app, caminho):
        self.img = PhotoImage(file=caminho)  # objeto imagem
        Label(app, image=self.img).pack(expand=YES, fill=BOTH)



class Elementos:

    numChave = []
    chaves = []
    numDisjuntores = []
    disjuntores = []
    numTrafosCs = []
    TrafosCs = []
    numTrafosPs = []
    TrafosPs = []
    numReles = []
    Reles = []

    def criaBotoesCheck(self, app, numS, numD, numTC, numTP, numRele):

        self.container1 = Frame(app)
        self.container2 = Frame(app)
        self.container3 = Frame(app)
        self.container4 = Frame(app)
        self.container5 = Frame(app)
        self.container6 = Frame(app)
        self.container1.pack(side=LEFT)
        self.container2.pack(side=LEFT)
        self.container3.pack(side=LEFT)
        self.container4.pack(side=LEFT)
        self.container5.pack(side=LEFT)


        if numS == 0:
            pass
        else:
            i = 0
            while i < numS:
                numChave = 'Chave ' + str(i+1) + '-' + str(i+2)
                Checkbutton(self.container1, text=numChave).pack(side=TOP)
                i+=2

        if numD == 0:
            pass
        else:
            for i in range(numD):
                numDisjuntores = 'Disjuntor ' + str(i+1)
                Checkbutton(self.container2, text=numDisjuntores).pack(side=TOP)

        if numTC == 0:
            pass
        else:
            for i in range(numTC):
                numTrafosCs = 'TC ' + str(i+1)
                Checkbutton(self.container3, text=numTrafosCs).pack(side=TOP)

        if numTP == 0:
            pass
        else:
            for i in range(numTP):
                numTrafosPs = 'TP ' + str(i+1)
                Checkbutton(self.container4, text=numTrafosPs).pack(side=TOP)

        if numRele == 0:
            pass
        else:
            for i in range(numRele):
                numReles = 'RELE ' + str(i+1)
                Checkbutton(self.container5, text=numReles).pack(side=TOP)


class Manobras:

    def semComando(self):
        pass

    def avisoSemComando(self):
        pass