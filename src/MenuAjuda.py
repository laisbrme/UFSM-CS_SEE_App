'''
    Comandos para abertura de janelas:
        - Sobre
        - Manual
'''

from tkinter import *
import os
import subprocess as sp
import webbrowser as wb

class ComandosParaJanelasAjuda():

    def semComando(self):
        pass

    def janelaSobre(self):
        self.app = Tk()
        self.app.title("Sobre UFSM-CS SEE")
        self.aux1 = os.getcwd() + '/ufsm-see.ico'
        self.aux = self.aux1.replace("\\", '/')
        self.diretorio = self.aux.replace('/', '//')
        self.app.iconbitmap(self.diretorio)
        self.app.geometry('400x250')
        self.app.resizable(width=False, height=False)

        Label(self.app, text="\nSobre UFSM-CS SEE App"
                            "\nVersão 1.0"
                            "\n\nEsta aplicação foi criada com o intuito de auxiliar"
                            "\nna disciplina de Subestações de Energia Elétrica,"
                            "\ndo curso de Engenharia Elétrica, da Universidade"
                            "\nFederal de Santa Maria - Campus Cachoeira do Sul!"
                            "\n\nApenas para uso educacional!", font="Times 12").pack()

        Button(self.app, text='Fechar', command=self.app.destroy).pack(side=BOTTOM)
        self.app.mainloop()

    def janelaManual(self):
        self.path = os.getcwd() + '\manual.pdf'
        #os.system(self.path)
        #sp.Popen([self.path], shell=True)
        #wb.open_new(r'manual.pdf')
