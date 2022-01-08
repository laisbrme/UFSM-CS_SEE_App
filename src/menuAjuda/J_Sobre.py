'''
    Janela Sobre do menu Ajuda
'''

from tkinter import *

app = Tk()
app.title("Sobre UFSM-CS SEE")
app.resizable(width=False, height=False)
caminho = 'image/sobre.gif'


foto = PhotoImage(file=caminho) # objeto imageM
can=Canvas(app)
can.pack(side=TOP) # ajeitar a disposição
can.create_image(5, 5, image=foto, anchor=NW)  # do desenho

'''
texto_orientacao = Label(app,
                         text="Sobre UFSM-CS SEE App"
                                   "\nVersão 0.1"
                                   "\n\nEsta aplicação foi criada com o intuito de auxiliar "
                                   "\nna disciplina de Subestações de Energia Elétrica, "
                                   "\ndo curso de Engenharia Elétrica, da Universidade "
                                   "\nFederal de Santa Maria - Campus Cachoeira do Sul!"
                                   "\n\nApenas para uso educacional!",
                         font="Times 12",
                         )
texto_orientacao.grid(column=0, row=0, padx=50, pady=50)
'''

Button(app, text='Fechar', command=quit).pack(side=BOTTOM, padx=0, pady=0)
barraMenu = Menu(app)
app.mainloop()