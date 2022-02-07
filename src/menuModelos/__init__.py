from src.menuModelos.barramentos.manobras1Barra import *
import os

def criaJanBarras(titulo, textoImg, caminhoImg, numS, numD, numTC, numTP, numRele):
    app = Tk()
    app.title(titulo)
    aux1 = os.getcwd() + '/ufsm-see.ico'
    aux = aux1.replace("\\", '/')
    diretorio = aux.replace('/', '//')
    app.iconbitmap(diretorio)

    Label(app, text=textoImg, font='Times 14 bold').pack()

    Scrollbar(app).pack()

    container1 = Config()
    container2 = Elementos()

    container1.imagem(app, caminho=caminhoImg)
    Label(app, text='Elementos:', font='Times 12 bold').pack(anchor=NW)
    container2.criaBotoesCheck(app, numS, numD, numTC, numTP, numRele)

    container3 = Frame()
    Button(container3, text='Energizar', command=app.destroy).pack(side=LEFT)
    Button(container3, text='Fechar', command=app.destroy).pack(side=RIGHT)

    app.mainloop()


class ComandosParaJanelasModelos():

    def semComando(self):
        pass


    def menu1sub1(self):
        '''
           Barramento Simples - Manobra no Disjuntor
        '''
        self.titulo = "Barramento Simples - Manobra no Disjuntor"
        self.textoImg = 'BARRAMENTO SIMPLES'
        self.aux1 = os.getcwd() + '/src/menuModelos/img/1.png'
        self.caminhoImg = self.aux1.replace("/", '\\')
        #self.caminhoImg = self.aux.replace('/', '//')
        criaJanBarras(self.titulo, self.textoImg, self.caminhoImg, numS=10, numD=5, numTC=4, numTP=1, numRele=1)

    def menu1sub2(self):
        '''
           Barramento Simples - Manobra na Barra
        '''
        self.titulo = "Barramento Simples - Manobra na Barra"
        self.textoImg = 'BARRAMENTO SIMPLES'
        self.caminhoImg = os.getcwd() + '/img/1.png'
        criaJanBarras(self.titulo, self.textoImg, self.caminhoImg, numS=10, numD=5, numTC=4, numTP=1, numRele=1)

    def menu1sub3(self):
        '''
           Barramento Simples - Manobra no Transformador de Potência
        '''
        self.titulo = "Barramento Simples - Manobra no Transformador de Potência"
        self.textoImg = 'BARRAMENTO SIMPLES'
        self.caminhoImg = os.getcwd() + '/img/1.png'
        criaJanBarras(self.titulo, self.textoImg, self.caminhoImg, numS=10, numD=5, numTC=4, numTP=1, numRele=1)