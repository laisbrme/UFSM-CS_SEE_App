'''
 Código da interface gráfica da aplicação UFSM SEE
'''

from tkinter import *
from src.ComandosJanelas import ComandosParaJanelas

app = Tk()
CJ  = ComandosParaJanelas()

app.title("UFSM-CS SEE")
app.geometry("1080x720")
app.configure(background="#dde")

barraMenu = Menu(app)

menu1 = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Arquivo", menu = menu1)
menu1.add_command(label = "Novo", command = CJ.semComando)
menu1.add_command(label = "Abrir", command = CJ.semComando)
menu1.add_command(label = "Salvar", command = CJ.semComando)
menu1.add_command(label = "Salvar como...", command = CJ.semComando)
menu1.add_separator()
menu1.add_command(label = "Fechar", command = app.quit)


menu2   = Menu(barraMenu, tearoff = 0)
submenu1 = Menu(menu2, tearoff = 0)
submenu2 = Menu(menu2, tearoff = 0)
barraMenu.add_cascade(label = "Modelos", menu = menu2)
menu2.add_cascade(label = "Barramentos", menu = submenu1)
submenu1.add_command(label = "1. Barramento Simples", command = CJ.semComando)
submenu1.add_command(label = "2. Barramento Simples com Barra de Transferência", command = CJ.semComando)
submenu1.add_command(label = "3. Barramento Simples Com Seccionamento de Barra", command = CJ.semComando)
submenu1.add_command(label = "4. Barramento Simples com Geração Auxiliar", command = CJ.semComando)
submenu1.add_command(label = "5. Barramento Duplo a Quatro Chaves", command = CJ.semComando)
submenu1.add_command(label = "6. Barramento Disjuntor Duplo", command = CJ.semComando)
submenu1.add_command(label = "7. Barramento Duplo e Disjuntor e Meio", command = CJ.semComando)
submenu1.add_command(label = "8. Barramento em Anel", command = CJ.semComando)
menu2.add_cascade(label = "Manobras", menu = submenu2)
submenu2.add_command(label = "1.tananã", command = CJ.semComando)
submenu2.add_command(label = "2.tananã", command = CJ.semComando)
submenu2.add_command(label = "3.tananã", command = CJ.semComando)
submenu2.add_command(label = "4.tananã", command = CJ.semComando)
submenu2.add_command(label = "5.tananã", command = CJ.semComando)
submenu2.add_command(label = "6.tananã", command = CJ.semComando)
submenu2.add_command(label = "7.tananã", command = CJ.semComando)
submenu2.add_command(label = "8.tananã", command = CJ.semComando)
submenu2.add_command(label = "9.tananã", command = CJ.semComando)


menu3 = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Ajuda", menu = menu3)
menu3.add_command(label = "Manual", command = CJ.semComando)
menu3.add_command(label = "Sobre", command = CJ.janelaSobre)

app.configure(menu = barraMenu)

app.mainloop()