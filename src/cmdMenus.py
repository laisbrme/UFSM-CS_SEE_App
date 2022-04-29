'''
    Classes para:
        - Configurar janela principal
        - Barra de menus
'''

from tkinter import *
from src.menuArquivos.cmdArquivos import *
from src.menuModelos.cmdModelos import *
from src.menuAjuda.cmdAjuda import *

CJF = ComandosParaJanelasArquivos()
CJM = ComandosParaJanelasModelos()
CJA = ComandosParaJanelasAjuda()

class configJan:

    def iconeJan(self, toplevel):
        aux1 = os.getcwd() + '/ufsm-see.ico'
        aux = aux1.replace("\\", '/')
        diretorio = aux.replace('/', '//')
        toplevel.iconbitmap(diretorio)

    def config(self, toplevel):
        toplevel.wm_state('zoomed')
        toplevel.configure(background="#dde")
        toplevel.minsize(width=300, height=200)


class barraMenu:
    def criaBarraMenus(self, app):
        menuBar = Menu(app)
        menu1 = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Arquivos", menu=menu1)
        menu1.add_command(label="Novo", command=CJF.semComando)
        menu1.add_command(label="Abrir", command=CJF.semComando)
        menu1.add_command(label="Salvar", command=CJF.semComando)
        menu1.add_separator()
        menu1.add_command(label="Fechar", command=app.quit)

        menu2 = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Modelos", menu=menu2)
        menu2.add_cascade(label="1. Barramento Simples", menu=CJM.AbrirBar1())
        menu2.add_cascade(label="2. Barramento Simples com Barra de Transferência", menu=CJM.AbrirBar2)
        menu2.add_cascade(label="3. Barramento Simples Com Seccionamento de Barra", menu=CJM.AbrirBar3)
        menu2.add_cascade(label="4. Barramento Simples com Geração Auxiliar", menu=CJM.AbrirBar4)
        menu2.add_cascade(label="5. Barramento Duplo a Quatro Chaves", menu=CJM.AbrirBar5)
        menu2.add_cascade(label="6. Barramento Disjuntor Duplo", menu=CJM.AbrirBar6)
        menu2.add_cascade(label="7. Barramento Duplo e Disjuntor e Meio", menu=CJM.AbrirBar7)
        menu2.add_cascade(label="8. Barramento em Anel", menu=CJM.AbrirBar8)

        menu3 = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Ajuda", menu=menu3)
        menu3.add_command(label="Manual", command=CJA.janelaManual)
        menu3.add_command(label="Sobre", command=CJA.janelaSobre)

        app.configure(menu=menuBar)
