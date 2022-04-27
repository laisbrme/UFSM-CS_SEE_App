from src.menuModelos.manobrasBarras import *

titulo = "Barramento Simples"

app = Tk()
app.title(titulo)
diretorio = 'C:/Users/laisb/Documents/GitHub/UFSM-CS_SEE_App/ufsm-see.ico'
app.iconbitmap(diretorio)

Label(app, text=titulo, font='Times 14 bold').pack()

img = PhotoImage(file='img/bar1.png')  # objeto imagem
Label(app, image=img).pack(expand=YES, fill=BOTH)

Label(app, text='Elementos:', font='Times 12 bold').pack(anchor=NW)
container2 = Elementos()
container2.criaBotoesCheck(app, numS=10, numD=5, numTC=4, numTP=1, numRele=1)

container3 = Frame(app)
container3.pack(side=BOTTOM)
Button(container3, text='Energizar', command=app.destroy).pack(side=LEFT)
Button(container3, text='Fechar', command=app.destroy).pack(side=RIGHT)

app.mainloop()