'''
    Barramento Simples - Manobra no Disjuntor
'''

from tkinter import *
from __init__ import *


app = Tk()
app.title("Barramento Simples - Manobra no Disjuntor")
#app.minsize(width=150, height=150)


container1 = Config()
container2 = Elementos()

container1.imagem(app, texto='BARRA SIMPLES', caminho='1.BarraSimples.gif')
#container2.criaBotoesCheck(app, numS=10, numD=5, numTC=5, numTP=2, numRele=1)

Button(app,text='Energizar',command=app.destroy).grid(row=12, column=0, sticky=E)
Button(app,text='Fechar',command=app.destroy).grid(row=12, column=1, sticky=E)
app.mainloop()