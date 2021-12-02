'''
 Código da interface gráfica da aplicação UFSM SEE
'''

from tkinter import *


def semComando():
    print(" ")

def janelaSobre():
    exec(open("menuAjuda.py").read())

app = Tk()

app.title("UFSM-CS SEE")
app.geometry("1080x720")
app.configure(background="#dde")

barraMenu = Menu(app)

menu1 = Menu(barraMenu, tearoff = 0)
menu1.add_command(label = "Novo", command = semComando)
menu1.add_separator()
menu1.add_command(label = "Fechar", command = app.quit)
barraMenu.add_cascade(label = "Arquivo", menu = menu1)


manu2 = Menu(barraMenu, tearoff = 0)
manu2.add_command(label ="Modelos", command = semComando)
barraMenu.add_cascade(label = "Modelos", menu = manu2)


menu3   = Menu(barraMenu, tearoff = 0)
menu3.add_command(label = "Manual", command = semComando)
menu3.add_command(label = "Sobre", command = janelaSobre)
barraMenu.add_cascade(label = "Ajuda", menu = menu3)






app.configure(menu = barraMenu)

app.mainloop()