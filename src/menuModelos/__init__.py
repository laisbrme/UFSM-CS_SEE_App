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


    def menu1sub1(self, app):
        '''
           Barramento Simples - Manobra no Disjuntor
        '''
        self.titulo = "Barramento Simples - Manobra no Disjuntor"
        self.textoImg = 'BARRAMENTO SIMPLES'
        self.aux1 = os.getcwd() + '/src/menuModelos/img/bar1.png'
        self.aux = self.aux1.replace("\\", '/')
        self.caminhoImg = self.aux.replace('/', '//')
        print(self.caminhoImg)
        #self.caminhoImg = 'C:/Users/laisb/Documents/GitHub/UFSM-CS_SEE_App/src/menuModelos/img/bar1.png'
        criaJanBarras(app, self.titulo, self.textoImg, self.caminhoImg, numS=10, numD=5, numTC=4, numTP=1, numRele=1)

    def menu1sub2(self):
        '''
           Barramento Simples - Manobra na Barra
        '''
        self.titulo = "Barramento Simples - Manobra na Barra"
        self.textoImg = 'BARRAMENTO SIMPLES'
        self.caminhoImg = os.getcwd() + '/img/bar1.png'
        criaJanBarras(self.titulo, self.textoImg, self.caminhoImg, numS=10, numD=5, numTC=4, numTP=1, numRele=1)

    def menu1sub3(self):
        '''
           Barramento Simples - Manobra no Transformador de Potência
        '''
        self.titulo = "Barramento Simples - Manobra no Transformador de Potência"
        self.textoImg = 'BARRAMENTO SIMPLES'
        self.caminhoImg = os.getcwd() + '/img/bar1.png'
        criaJanBarras(self.titulo, self.textoImg, self.caminhoImg, numS=10, numD=5, numTC=4, numTP=1, numRele=1)