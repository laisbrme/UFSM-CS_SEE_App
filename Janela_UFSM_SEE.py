% Código da interface gráfica da aplicação
% UFSM SEE

from tkinter import *

janela = Tk()

    janela.title("UFSM SEE")
    janela.geometry("720x480")
    
    texto_orientacao = Label(janela, text = "Esta aplicação foi criada com o intuito de auxiliar na disciplina de Subestações de Energia Elétrica, do curso de Engenharia Elétrica, da Universidade Federal de Santa Maria - Campus Cachoeira do Sul!")
    texto_orientacao.grid(column = 0, row = 0, padx = 10, pady = 10)

janela.mainloop()