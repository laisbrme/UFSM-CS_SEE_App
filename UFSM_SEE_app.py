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
menu1.add_command(label = "Novo", command = CJ.semComando)
menu1.add_command(label = "Abrir", command = CJ.semComando)
menu1.add_command(label = "Salvar", command = CJ.semComando)
menu1.add_command(label = "Salvar como...", command = CJ.semComando)
menu1.add_separator()
menu1.add_command(label = "Fechar", command = app.quit)
barraMenu.add_cascade(label = "Arquivo", menu = menu1)


manu2 = Menu(barraMenu, tearoff = 0)
manu2.add_command(label ="Barramentos", command = CJ.semComando)
manu2.add_command(label ="Manobras", command = CJ.semComando)
barraMenu.add_cascade(label = "Modelos", menu = manu2)


menu3 = Menu(barraMenu, tearoff = 0)
menu3.add_command(label = "Manual", command = CJ.semComando)
menu3.add_command(label = "Sobre", command = CJ.janelaSobre)
barraMenu.add_cascade(label = "Ajuda", menu = menu3)






app.configure(menu = barraMenu)

app.mainloop()