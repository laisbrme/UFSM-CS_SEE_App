'''
    Código da interface gráfica da aplicação UFSM SEE
'''

from tkinter import *
from src.__init__ import *


app = Tk()
app.title("UFSM-CS SEE")
app.iconbitmap("ufsm-see.ico")
#app.wm_state('zoomed')
app.configure(background="#dde")
app.minsize(width=300, height=200)

menus = barraMenu()
menus.criaBarraMenus(app)

status = 'Inicie uma nova manobra'
Label(app, text=status, bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)
app.mainloop()
