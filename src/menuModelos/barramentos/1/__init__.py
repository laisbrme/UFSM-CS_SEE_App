'''
    Classe de funções para as manobras dos barramentos.
'''

from tkinter import *


class Config:

    def imagem(self, app, caminho):
        self.img = PhotoImage(file=caminho)  # objeto imagem
        Label(app, image=self.img).pack()


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
        self.container6.pack(side=BOTTOM)


        if numS == 0:
            pass
        else:
            for i in range(numS):
                numChave = 'Chave ' + str(i+1)
                Checkbutton(self.container1, text=numChave).pack(side=TOP)
                i = +1

        if numD == 0:
            pass
        else:
            for i in range(numD):
                numDisjuntores = 'Disjuntor ' + str(i+1)
                Checkbutton(self.container2, text=numDisjuntores).pack(side=TOP)
                i = +1

        if numTC == 0:
            pass
        else:
            for i in range(numTC):
                numTrafosCs = 'TC ' + str(i+1)
                Checkbutton(self.container3, text=numTrafosCs).pack(side=TOP)
                i = +1

        if numTP == 0:
            pass
        else:
            for i in range(numTP):
                numTrafosPs = 'TP ' + str(i+1)
                Checkbutton(self.container4, text=numTrafosPs).pack(side=TOP)
                i = +1

        if numRele == 0:
            pass
        else:
            for i in range(numRele):
                numReles = 'RELE ' + str(i+1)
                Checkbutton(self.container5, text=numReles).pack(side=TOP)
                i = +1

        Button(self.container6, text='Energizar', command=app.destroy).pack(side=LEFT)
        Button(self.container6, text='Fechar', command=app.destroy).pack(side=RIGHT)

class Manobras:

    def semComando(self):
        pass