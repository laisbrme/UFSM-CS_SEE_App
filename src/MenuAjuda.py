'''
    Comandos para abertura de janelas:
        - Sobre
        - Manual
'''

from tkinter import *
import os


class ComandosParaJanelasAjuda:

    def semComando(self):
        pass

    def janelaSobre(self):
        self.app = Tk()
        self.app.title("Sobre UFSM-CS SEE")
        self.app.overrideredirect(True)
        self.app.geometry('450x300')
        self.app.resizable(width=False, height=False)
        self.app.eval('tk::PlaceWindow . center')

        Label(self.app,
              text="\n\nSobre UFSM-CS SEE App"
                   "\nVersão 1.0"
                   "\n\nEsta aplicação foi criada com o intuito de auxiliar"
                   "\nna disciplina de Subestações de Energia Elétrica,"
                   "\ndo curso de Engenharia Elétrica, da Universidade"
                   "\nFederal de Santa Maria - Campus Cachoeira do Sul!"
                   "\n\nApenas para uso educacional!",
              font="Times 14").pack()

        Button(self.app, text='Fechar', command=self.app.destroy).pack(side=BOTTOM)
        self.app.mainloop()

    def janelaManual(self):
        self.path = os.getcwd() + '\\src\\manual.pdf'
        os.system(self.path)
