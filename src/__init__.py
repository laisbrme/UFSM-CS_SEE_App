
from tkinter import *

from src.menuArquivos.__init__ import *
from src.menuModelos.__init__ import *
from src.menuAjuda.__init__ import *

CJF = ComandosParaJanelasArquivos()
CJM = ComandosParaJanelasModelos()
CJA = ComandosParaJanelasAjuda()

class janelas:
    def criaBarraMenus(self, app):
        barraMenu = Menu(app)
        menu1 = Menu(barraMenu, tearoff=0)
        barraMenu.add_cascade(label="Arquivos", menu=menu1)
        menu1.add_command(label="Novo", command=CJF.semComando)
        menu1.add_command(label="Abrir", command=CJF.semComando)
        menu1.add_command(label="Salvar", command=CJF.semComando)
        menu1.add_command(label="Salvar como...", command=CJF.semComando)
        menu1.add_separator()
        menu1.add_command(label="Fechar", command=app.quit)

        menu2 = Menu(barraMenu, tearoff=0)
        submenu1 = Menu(menu2, tearoff=0)
        submenu2 = Menu(menu2, tearoff=0)
        submenu3 = Menu(menu2, tearoff=0)
        submenu4 = Menu(menu2, tearoff=0)
        submenu5 = Menu(menu2, tearoff=0)
        submenu6 = Menu(menu2, tearoff=0)
        submenu7 = Menu(menu2, tearoff=0)
        submenu8 = Menu(menu2, tearoff=0)

        barraMenu.add_cascade(label="Modelos", menu=menu2)
        menu2.add_cascade(label="1. Barramento Simples", menu=submenu1)
        submenu1.add_command(label="1.Manobra no Disjuntor", command=lambda:CJM.menu1sub1(app))
        submenu1.add_command(label="2.Manobra na Barra", command=CJM.menu1sub2)
        submenu1.add_command(label="3.Manobra no Transformador de Potência", command=CJM.menu1sub3)

        menu2.add_cascade(label="2. Barramento Simples com Barra de Transferência", menu=submenu2)
        submenu2.add_command(label="1.tananã", command=CJM.semComando)
        submenu2.add_command(label="2.tananã", command=CJM.semComando)
        submenu2.add_command(label="3.tananã", command=CJM.semComando)

        menu2.add_cascade(label="3. Barramento Simples Com Seccionamento de Barra", menu=submenu3)
        submenu3.add_command(label="1.tananã", command=CJM.semComando)
        submenu3.add_command(label="2.tananã", command=CJM.semComando)
        submenu3.add_command(label="3.tananã", command=CJM.semComando)

        menu2.add_cascade(label="4. Barramento Simples com Geração Auxiliar", menu=submenu4)
        submenu4.add_command(label="1.tananã", command=CJM.semComando)
        submenu4.add_command(label="2.tananã", command=CJM.semComando)
        submenu4.add_command(label="3.tananã", command=CJM.semComando)

        menu2.add_cascade(label="5. Barramento Duplo a Quatro Chaves", menu=submenu5)
        submenu5.add_command(label="1.tananã", command=CJM.semComando)
        submenu5.add_command(label="2.tananã", command=CJM.semComando)
        submenu5.add_command(label="3.tananã", command=CJM.semComando)

        menu2.add_cascade(label="6. Barramento Disjuntor Duplo", menu=submenu6)
        submenu6.add_command(label="1.tananã", command=CJM.semComando)
        submenu6.add_command(label="2.tananã", command=CJM.semComando)
        submenu6.add_command(label="3.tananã", command=CJM.semComando)

        menu2.add_cascade(label="7. Barramento Duplo e Disjuntor e Meio", menu=submenu7)
        submenu7.add_command(label="1.tananã", command=CJM.semComando)
        submenu7.add_command(label="2.tananã", command=CJM.semComando)
        submenu7.add_command(label="3.tananã", command=CJM.semComando)

        menu2.add_cascade(label="8. Barramento em Anel", menu=submenu8)
        submenu8.add_command(label="1.tananã", command=CJM.semComando)
        submenu8.add_command(label="2.tananã", command=CJM.semComando)
        submenu8.add_command(label="3.tananã", command=CJM.semComando)

        menu3 = Menu(barraMenu, tearoff=0)
        barraMenu.add_cascade(label="Ajuda", menu=menu3)
        menu3.add_command(label="Manual", command=CJA.janelaManual)
        menu3.add_command(label="Sobre", command=CJA.janelaSobre)

        app.configure(menu=barraMenu)