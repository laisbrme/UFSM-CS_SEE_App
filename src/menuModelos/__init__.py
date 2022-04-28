from src.menuModelos.manobrasBarras import *
import os

def criaJanBarras(app, titulo, textoImg, caminhoImg, numS, numD, numTC, numTP, numRele):
    #app = Tk()
    app.title(titulo)
    aux1 = os.getcwd() + '/ufsm-see.ico'
    aux = aux1.replace("\\", '/')
    diretorio = aux.replace('/', '//')
    app.iconbitmap(diretorio)

    Label(app, text=textoImg, font='Times 14 bold').pack()

    img = PhotoImage(file=caminhoImg)  # objeto imagem
    Label(app, image=img).pack(expand=YES, fill=BOTH)

    container2 = Elementos()
    Label(app, text='Elementos:', font='Times 12 bold').pack(anchor=NW)
    container2.criaBotoesCheck(app, numS, numD, numTC, numTP, numRele)

    container3 = Frame()
    Button(container3, text='Energizar', command=app.destroy).pack(side=LEFT)
    Button(container3, text='Fechar', command=app.destroy).pack(side=RIGHT)

    #app.mainloop()


class ComandosParaJanelasModelos():

    def semComando(self):
        pass
