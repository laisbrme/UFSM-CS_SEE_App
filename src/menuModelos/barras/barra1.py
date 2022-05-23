from tkinter import *

app = Tk()
app.title("Barramento Simples")
app.iconbitmap('img/ufsm-see.ico')

def cliclouStart():
    container1 = Frame(app, bg="black", bd=4, relief=GROOVE)
    container2 = Frame(app, bg="black", bd=4, relief=GROOVE)
    subcontainer1 = Frame(container2, bg="#dde", bd=4, relief=RAISED)
    subcontainer2 = Frame(container2, bd=4)
    subcontainer3 = Frame(container2, bd=4)
    container1.pack(side='left')
    container2.pack(side='left', fill='y')
    subcontainer1.pack(fill='both', expand='yes')
    subcontainer2.pack(fill='both', expand='yes')
    subcontainer3.pack(fill='both', expand='yes')

    # Objeto imagem:
    dir = 'img/bar6.png'
    img = PhotoImage(file=dir)
    diagrama = Label(container1, image=img)
    diagrama.pack(fill='both')

    # Criação Tela Interativa
    alerta = '--------------------------------------------------------------\n' \
             'Barramento Duplo com Disjuntor Duplo\n\n' \
             'Defina o elemento com falha!\n' \
             '--------------------------------------------------------------'
    telaInt = Label(subcontainer1,
                    text=alerta,
                    font='times 12 bold',
                    justify='center',
                    bg="#dde")
    telaInt.pack(fill='both', expand='yes')

    # Criação Combobox
    opcoes = ['Disjuntor D1',
              'Disjuntor D2',
              'Disjuntor D3',
              'Disjuntor D4',
              'Disjuntor D5',
              'Disjuntor D6',
              'Disjuntor D7',
              'Disjuntor D8', ]

    clicada = StringVar()
    Label(subcontainer2, text="Elemento: ").pack(fill='both', side='left', padx=5, pady=5)
    combo = OptionMenu(subcontainer2, clicada, *opcoes)
    combo.pack(fill='x', side='left', padx=5, pady=5)

    # Criação Botões
    botao1 = Button(subcontainer3, text='Próximo Passo', command='1')
    botao1.pack(side='left', fill='x', expand='yes')
    botao2 = Button(subcontainer3, text='Finalizar Manobra')
    botao2.pack(side='left', fill='x', expand='yes')

    if combo.get() == 'Disjuntor D3' and botao1.get() == '1':
        # Objeto imagem:
        dir = 'img/bar5.png'
        img = PhotoImage(file=dir)
        diagrama = Label(container1, image=img)
        diagrama.pack(fill='both')

        # Criação Tela Interativa
        alerta = '--------------------------------------------------------------\n' \
                 'Barramento Duplo com Disjuntor Duplo\n\n' \
                 'Falha em D3!\n' \
                 '--------------------------------------------------------------'
        telaInt = Label(subcontainer1,
                        text=alerta,
                        font='times 12 bold',
                        justify='center',
                        bg="#dde")
        telaInt.pack(fill='both', expand='yes')

        # Criação Combobox
        opcoes = ['Abrir S1-2',
                  'Abrir S5-6',
                  'Abrir S9-10',
                  'Abrir S13-14',
                  'Fechar S3-4',
                  'Fechar S7-8',
                  'Fechar S11-12',
                  'Fechar S15-16',
                  'Desligar D1',
                  'Desligar D3',
                  'Desligar D5',
                  'Desligar D7',
                  'Ligar D2',
                  'Ligar D4',
                  'Ligar D6',
                  'Ligar D8',]

        clicada = StringVar()
        Label(subcontainer2, text="Elemento: ").pack(fill='both', side='left', padx=5, pady=5)
        combo = OptionMenu(subcontainer2, clicada, *opcoes)
        combo.pack(fill='x', side='left', padx=5, pady=5)

        # Criação Botões
        botao1 = Button(subcontainer3, text='Próximo Passo')
        botao1.pack(side='left', fill='x', expand='yes')
        botao2 = Button(subcontainer3, text='Finalizar Manobra')
        botao2.pack(side='left', fill='x', expand='yes')




botaoStart = Button(app, text='Iniciar Manobra', command=cliclouStart).pack(side='left', fill='x', expand='yes')

app.mainloop()