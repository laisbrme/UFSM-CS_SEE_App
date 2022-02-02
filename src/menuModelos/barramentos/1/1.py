'''
    Barramento Simples - Manobra no Disjuntor
'''

from tkinter import *
from __init__ import *


app = Tk()
app.title("Barramento Simples - Manobra no Disjuntor")

container1 = Config()
container2 = Elementos()

container1.imagem(app, caminho='1.png')
container2.criaBotoesCheck(app, numS=10, numD=5, numTC=4, numTP=1, numRele=1)

app.mainloop()