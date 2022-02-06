from tkinter import *
import PyPDF2

class ComandosParaJanelasAjuda():

    def semComando(self):
        pass

    def janelaSobre(self):
        self.app = Tk()
        self.app.title("Sobre UFSM-CS SEE")
        self.app.geometry('400x250')
        self.app.resizable(width=False, height=False)

        Label(self.app, text="\nSobre UFSM-CS SEE App"
                            "\nVersão 0.1"
                            "\n\nEsta aplicação foi criada com o intuito de auxiliar"
                            "\nna disciplina de Subestações de Energia Elétrica,"
                            "\ndo curso de Engenharia Elétrica, da Universidade"
                            "\nFederal de Santa Maria - Campus Cachoeira do Sul!"
                            "\n\nApenas para uso educacional!", font="Times 12").pack()

        Button(self.app, text='Fechar', command=self.app.destroy).pack(side=BOTTOM)
        self.app.mainloop()

    def janelaManual(self):
        with open("sample.pdf", "rb") as f:
            pdf = PyPDF2.PdfFileReader(f)