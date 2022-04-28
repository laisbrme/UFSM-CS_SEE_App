
from tkinter import *

from src.menuArquivos.__init__ import *
from src.menuModelos.__init__ import *
from src.menuAjuda.__init__ import *

CJF = ComandosParaJanelasArquivos()
CJM = ComandosParaJanelasModelos()
CJA = ComandosParaJanelasAjuda()

class barraMenu:
    def criaBarraMenus(self, app):
        menuBar = Menu(app)
        menu1 = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Arquivos", menu=menu1)
        menu1.add_command(label="Novo", command=CJF.semComando)
        menu1.add_command(label="Abrir", command=CJF.semComando)
        menu1.add_command(label="Salvar", command=CJF.semComando)
        menu1.add_command(label="Salvar como...", command=CJF.semComando)
        menu1.add_separator()
        menu1.add_command(label="Fechar", command=app.quit)

        menu2 = Menu(menuBar, tearoff=0)
        submenu1 = Menu(menu2, tearoff=0)
        submenu2 = Menu(menu2, tearoff=0)
        submenu3 = Menu(menu2, tearoff=0)
        submenu4 = Menu(menu2, tearoff=0)
        submenu5 = Menu(menu2, tearoff=0)
        submenu6 = Menu(menu2, tearoff=0)
        submenu7 = Menu(menu2, tearoff=0)
        submenu8 = Menu(menu2, tearoff=0)

        menuBar.add_cascade(label="Modelos", menu=menu2)
        menu2.add_cascade(label="1. Barramento Simples", menu=CJM.semComando)
        menu2.add_cascade(label="2. Barramento Simples com Barra de Transferência", menu=CJM.semComando)
        menu2.add_cascade(label="3. Barramento Simples Com Seccionamento de Barra", menu=CJM.semComando)
        menu2.add_cascade(label="4. Barramento Simples com Geração Auxiliar", menu=CJM.semComando)
        menu2.add_cascade(label="5. Barramento Duplo a Quatro Chaves", menu=CJM.semComando)
        menu2.add_cascade(label="6. Barramento Disjuntor Duplo", menu=CJM.semComando)
        menu2.add_cascade(label="7. Barramento Duplo e Disjuntor e Meio", menu=CJM.semComando)
        menu2.add_cascade(label="8. Barramento em Anel", menu=CJM.semComando)

        menu3 = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Ajuda", menu=menu3)
        menu3.add_command(label="Manual", command=CJA.janelaManual)
        menu3.add_command(label="Sobre", command=CJA.janelaSobre)

        app.configure(menu=menuBar)
