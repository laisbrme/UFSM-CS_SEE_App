'''
    Classes para:
        - Configurar janela principal
        - Barra de menus
'''

import os
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
        #toplevel.wm_state('zoomed')
        toplevel.configure(background="#dde")
        toplevel.minsize(width=300, height=200)

class barraMenu:
    def criaBarraMenus(self, toplevel):
        menuBar = Menu(toplevel)
        menu1 = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Arquivos", menu=menu1)
        menu1.add_command(label="Novo", command=CJF.semComando)
        menu1.add_command(label="Abrir", command=CJF.semComando)
        menu1.add_command(label="Salvar", command=CJF.semComando)
        menu1.add_separator()
        menu1.add_command(label="Fechar", command=toplevel.destroy)

        menu2 = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Modelos", menu=menu2)
        menu2.add_cascade(label="1. Barramento Simples", command=CJM.AbrirBar1)
        menu2.add_cascade(label="2. Barramento Principal com Barra de Transferência", command=CJM.AbrirBar2)
        menu2.add_cascade(label="3. Barramento Principal com Seccionamento de Barra", command=CJM.AbrirBar3)
        menu2.add_cascade(label="4. Duplo Barramento Simples com Geração Auxiliar", command=CJM.AbrirBar4)
        menu2.add_cascade(label="5. Barramento Duplo com Disjuntor a Quatro Chaves", command=CJM.AbrirBar5)
        menu2.add_cascade(label="6. Barramento Duplo com Disjuntor Duplo", command=CJM.AbrirBar6(toplevel))
        menu2.add_cascade(label="7. Barramento Duplo com Disjuntor e Meio", command=CJM.AbrirBar7)
        menu2.add_cascade(label="8. Barramento em Anel", command=CJM.AbrirBar8)

        menu3 = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Ajuda", menu=menu3)
        menu3.add_command(label="Manual", command=CJA.janelaManual)
        menu3.add_command(label="Sobre", command=CJA.janelaSobre)

        toplevel.configure(menu=menuBar)

