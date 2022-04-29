from tkinter import *

from src.menuModelos.manobrasBarras import *

class JanBar6:
    def tituloMain(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', background='green')
        self.botao.pack()
'''
titulo = "Barramento Dijuntor Duplo"
bar6 = Tk()
bar6.title(titulo)
Configura = configJan()
Configura.config(bar6)
JanBar6(bar6)
bar6.mainloop()
'''