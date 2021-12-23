'''
 Código da interface gráfica da aplicação UFSM SEE
'''

from tkinter import *
from src.menuArquivos.ComandosArquivos import ComandosParaJanelasArquivos
from src.menuModelos.ComandosModelos import ComandosParaJanelasModelos
from src.menuAjuda.ComandosAjuda import ComandosParaJanelasAjuda

app = Tk()
CJF  = ComandosParaJanelasArquivos()
CJM  = ComandosParaJanelasModelos()
CJA  = ComandosParaJanelasAjuda()

app.title("UFSM-CS SEE")
app.geometry("1080x720")
app.configure(background="#dde")


barraMenu = Menu(app)
menu1 = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Arquivos", menu = menu1)
menu1.add_command(label = "Novo", command = CJF.semComando)
menu1.add_command(label = "Abrir", command = CJF.semComando)
menu1.add_command(label = "Salvar", command = CJF.semComando)
menu1.add_command(label = "Salvar como...", command = CJF.semComando)
menu1.add_separator()
menu1.add_command(label = "Fechar", command = app.quit)


menu2   = Menu(barraMenu, tearoff = 0)
submenu1 = Menu(menu2, tearoff = 0)
submenu2 = Menu(menu2, tearoff = 0)
barraMenu.add_cascade(label = "Modelos", menu = menu2)
menu2.add_cascade(label = "Barramentos", menu = submenu1)
submenu1.add_command(label = "1. Barramento Simples", command = CJM.semComando)
submenu1.add_command(label = "2. Barramento Simples com Barra de Transferência", command = CJM.semComando)
submenu1.add_command(label = "3. Barramento Simples Com Seccionamento de Barra", command = CJM.semComando)
submenu1.add_command(label = "4. Barramento Simples com Geração Auxiliar", command = CJM.semComando)
submenu1.add_command(label = "5. Barramento Duplo a Quatro Chaves", command = CJM.semComando)
submenu1.add_command(label = "6. Barramento Disjuntor Duplo", command = CJM.semComando)
submenu1.add_command(label = "7. Barramento Duplo e Disjuntor e Meio", command = CJM.semComando)
submenu1.add_command(label = "8. Barramento em Anel", command = CJM.semComando)
menu2.add_cascade(label = "Manobras", menu = submenu2)
submenu2.add_command(label = "1.tananã", command = CJM.semComando)
submenu2.add_command(label = "2.tananã", command = CJM.semComando)
submenu2.add_command(label = "3.tananã", command = CJM.semComando)
submenu2.add_command(label = "4.tananã", command = CJM.semComando)
submenu2.add_command(label = "5.tananã", command = CJM.semComando)
submenu2.add_command(label = "6.tananã", command = CJM.semComando)
submenu2.add_command(label = "7.tananã", command = CJM.semComando)
submenu2.add_command(label = "8.tananã", command = CJM.semComando)
submenu2.add_command(label = "9.tananã", command = CJM.semComando)


menu3 = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Ajuda", menu = menu3)
menu3.add_command(label = "Manual", command = CJA.janelaManual)
menu3.add_command(label = "Sobre", command = CJA.janelaSobre)


app.configure(menu = barraMenu)
app.mainloop()