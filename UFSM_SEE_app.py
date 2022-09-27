# -*- coding: utf-8 -*-
'''
    Código da interface gráfica da aplicação UFSM SEE
'''

from src.cmdMenus import *

app = Tk()
app.title("UFSM-CS SEE")
app.iconbitmap('src/barras/img/ufsm-see.ico')
app.configure(background="#dde")
app.minsize(width=300, height=200)
app.resizable(False, False)
app.eval('tk::PlaceWindow . center')
MenuJan = barraMenu()
MenuJan.criaBarraMenus(app)

status = ' Janela Principal | Inicie uma nova manobra'
Label(app, text=status, bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)
app.mainloop()
