from src.menuModelos.manobrasBarras import *

class JanBar6:
    def tituloMain(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', background='green')
        self.botao.pack()
