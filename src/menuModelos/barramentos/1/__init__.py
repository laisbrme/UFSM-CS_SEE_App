'''
    Classe de funções para as manobras dos barramentos.
'''

from tkinter import *

class Config:

    def imagem(self, app, texto, caminho):
        Label(app, text=texto, font=('Times', '14', 'bold')).grid(row=0, column=1,
                                            sticky=W, pady=3)

        self.foto = PhotoImage(file=caminho)  # objeto imagem
        self.can = Canvas(app)
        self.can.grid(row=1, column=1)
        self.can.create_image(2, 2, image=self.foto, anchor=N)  # do desenho

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
        if numS == 0:
            pass
        else:
            for i in range(numS):
                numChave = 'Chave ' + str(i+1)
                chaves = Checkbutton(app, text=numChave).grid(row=2 + i, column=0, sticky=W)
                i = +1

        if numD == 0:
            pass
        else:
            for i in range(numD):
                numDisjuntores = 'Disjuntor ' + str(i+1)
                disjuntores = Checkbutton(app, text=numDisjuntores).grid(row=2 + i, column=1, sticky=W)
                i = +1

        if numTC == 0:
            pass
        else:
            for i in range(numTC):
                numTrafosCs = 'TC ' + str(i+1)
                TrafosCs = Checkbutton(app, text=numTrafosCs).grid(row=2 + i, column=2, sticky=W)
                i = +1

        if numTP == 0:
            pass
        else:
            for i in range(numTP):
                numTrafosPs = 'TP ' + str(i+1)
                TrafosPs = Checkbutton(app, text=numTrafosPs).grid(row=2 + i, column=3, sticky=W)
                i = +1

        if numRele == 0:
            pass
        else:
            for i in range(numRele):
                numReles = 'RELE ' + str(i+1)
                Reles = Checkbutton(app, text=numReles).grid(row=2 + i, column=4, sticky=W)
                i = +1

class Manobras:

    def semComando(self):
        pass