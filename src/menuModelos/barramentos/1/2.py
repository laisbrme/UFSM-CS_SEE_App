'''
    Barramento Simples - Manobra na Barra
'''

from tkinter import *
from __init__ import *

app = Tk()
app.title("Barramento Simples - Manobra no Disjuntor")
#app.minsize(width=150, height=150)

img = PhotoImage(file='1.png')  # objeto imagem
imagem = Label(app, image=img).pack()




app.mainloop()