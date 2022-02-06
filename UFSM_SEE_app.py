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

Jan = janelas()
Jan.criaBarraMenus(app)



Scrollbar(app).pack(side="right", fill="y")

info = 'Inicie uma nova manobra'
statusbar = Label(app, text=info, bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)
app.mainloop()
