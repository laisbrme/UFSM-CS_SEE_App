'''
    Classes para:
        - Barra de menus
'''

from tkinter import *

'''
from src.barras.barra1 import *
from src.barras.barra2 import *
from src.barras.barra3 import *
from src.barras.barra4 import *
from src.barras.barra5 import *
from src.barras.barra6 import *
from src.barras.barra7 import *
from src.barras.barra8 import *
'''


class ComandosParaJanelasModelos:
    def __init__(self):
        pass

    def semComando(self):
        pass

    def AbrirBar1(self):
        self.janBar = Tk()
        self.janBar.title("Barramento Simples")
        self.janBar.overrideredirect(True)
        self.janBar.minsize(width=300, height=200)
        self.janBar.resizable(False, False)
        self.janBar.eval('tk::PlaceWindow . center')

        self.janBar.mainloop()

    def AbrirBar2(self):
        self.janBar = Tk()
        self.janBar.title("Barramento Principal com Barra de Transferência")
        self.janBar.overrideredirect(True)
        self.janBar.minsize(width=300, height=200)
        self.janBar.resizable(False, False)
        self.janBar.eval('tk::PlaceWindow . center')

        self.janBar.mainloop()

    def AbrirBar3(self):
        self.janBar = Tk()
        self.janBar.title("Barramento Principal com Seccionamento de Barra")
        self.janBar.overrideredirect(True)
        self.janBar.minsize(width=300, height=200)
        self.janBar.resizable(False, False)
        self.janBar.eval('tk::PlaceWindow . center')

        self.janBar.mainloop()

    def AbrirBar4(self):
        self.janBar = Tk()
        self.janBar.title("Duplo Barramento Simples com Geração Auxiliar")
        self.janBar.overrideredirect(True)
        self.janBar.minsize(width=300, height=200)
        self.janBar.resizable(False, False)
        self.janBar.eval('tk::PlaceWindow . center')

        self.janBar.mainloop()

    def AbrirBar5(self):
        self.janBar = Tk()
        self.janBar.title("Barramento Duplo com Disjuntor a Quatro Chaves")
        self.janBar.overrideredirect(True)
        self.janBar.minsize(width=300, height=200)
        self.janBar.resizable(False, False)
        self.janBar.eval('tk::PlaceWindow . center')

        self.janBar.mainloop()

    def AbrirBar6(self):
        self.janBar = Tk()
        self.janBar.title("Barramento Duplo com Disjuntor Duplo")
        self.janBar.overrideredirect(True)
        self.janBar.minsize(width=300, height=200)
        self.janBar.resizable(False, False)
        self.janBar.eval('tk::PlaceWindow . center')

        self.janBar.mainloop()

    def AbrirBar7(self):
        self.janBar = Tk()
        self.janBar.title("Barramento Duplo com Disjuntor e Meio")
        self.janBar.overrideredirect(True)
        self.janBar.minsize(width=300, height=200)
        self.janBar.resizable(False, False)
        self.janBar.eval('tk::PlaceWindow . center')

        self.janBar.mainloop()

    def AbrirBar8(self):
        self.janBar = Tk()
        self.janBar.title("Barramento em Anel")
        self.janBar.overrideredirect(True)
        self.janBar.minsize(width=300, height=200)
        self.janBar.resizable(False, False)
        self.janBar.eval('tk::PlaceWindow . center')

        self.janBar.mainloop()
