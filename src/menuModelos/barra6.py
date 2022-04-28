from src.menuModelos.manobrasBarras import *
from tkinter import *

class Janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', background='green')
        self.botao.pack()

titulo = "Barramento Dijuntor Duplo"

bar6 = Tk()
bar6.title(titulo)
diretorio = 'C:/Users/laisb/Documents/GitHub/UFSM-CS_SEE_App/ufsm-see.ico'
bar6.iconbitmap(diretorio)
Janela(bar6)
bar6.mainloop()