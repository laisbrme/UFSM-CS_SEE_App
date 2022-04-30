'''
    Código da interface gráfica da aplicação UFSM SEE
'''

import os
from tkinter import *
from src.cmdMenus import *

app = Tk()
app.title("UFSM-CS SEE")
Configura = configJan()
Configura.config(app)
Configura.iconeJan(app)
menus = barraMenu()
menus.criaBarraMenus(app)

status = ' Janela Principal | Inicie uma nova manobra'
Label(app, text=status, bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)
app.mainloop()




