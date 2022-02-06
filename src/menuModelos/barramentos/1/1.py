'''
    Barramento Simples - Manobra no Disjuntor
'''

from tkinter import *
from __init__ import *

app = Tk()
app.title("Barramento Simples - Manobra no Disjuntor")
titulo1 = Label(app, text='BARRAMENTO SIMPLES', font='Times 14 bold').pack()

sb = Scrollbar(app)

container1 = Config()
container2 = Elementos()
manobra    = Manobras()

container1.imagem(app, caminho='1.png')
titulo2 = Label(app, text='Elementos:', font='Times 12 bold').pack(anchor=NW)
container2.criaBotoesCheck(app, numS=10, numD=5, numTC=4, numTP=1, numRele=1)

Button(app, text='Energizar', command=manobra.avisoSemComando()).pack(side=LEFT)
Button(app, text='Fechar', command=app.destroy).pack(side=RIGHT)

app.mainloop()