from tkinter import ttk
from tkinter import *


app = Tk()
app.title("Barramento Duplo com Disjuntor Duplo")
#app.iconbitmap('img/ufsm-see.ico')


def finaliza(elem_sel):
    if elem_sel == 'Trocar D1':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D1 finalizada!\n'
                               '--------------------------------------------------------------')


    elif elem_sel == 'Trocar D3':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D3 finalizada!\n'
                               '--------------------------------------------------------------')


    elif elem_sel == 'Trocar D5':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D5 finalizada!\n'
                               '--------------------------------------------------------------')


    elif elem_sel == 'Trocar D7':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D7 finalizada!\n'
                               '--------------------------------------------------------------')


def Disj3Passo6():
    print('9. Entrou em Disj3Passo2')
    elem_sel = combo.get()
    print('9.Elemento Selecionado: ' + elem_sel)

    if elem_sel == 'Trocar D3':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor D3 trocado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.pack_forget()
        print('9. Dentro do IF \n')
        print(elem_sel)
        botao1.configure(text='Finalizar', command=lambda: finaliza(elem_sel))
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj3Passo6()


def Disj3Passo5():
    print('8. Entrou em Disj3Passo2')
    elem_sel = combo.get()
    print('8.Elemento Selecionado: ' + elem_sel)

    if elem_sel == 'Abrir S5-6':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S5 e S6 abertas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3',
                                'Abrir S1-2',
                                'Fechar S5-6',
                                'Abrir S9-10',
                                'Abrir S13-14',
                                'Abrir S3-4',
                                'Abrir S7-8',
                                'Fechar S11-12',
                                'Fechar S15-16',
                                'Desligar D1',
                                'Ligar D3',
                                'Desligar D5',
                                'Desligar D7',
                                'Desligar D2',
                                'Desligar D4',
                                'Ligar D6',
                                'Ligar D8', ])
        print('8. Dentro do IF \n')
        botao1.configure(command=lambda: Disj3Passo6())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj3Passo5()


def Disj3Passo4():
    print('7. Entrou em Disj3Passo2')
    elem_sel = combo.get()
    print('7.Elemento Selecionado: ' + elem_sel)

    if elem_sel == 'Desligar D3':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor D3 desligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3',
                                'Abrir S1-2',
                                'Abrir S5-6',
                                'Abrir S9-10',
                                'Abrir S13-14',
                                'Abrir S3-4',
                                'Abrir S7-8',
                                'Fechar S11-12',
                                'Fechar S15-16',
                                'Desligar D1',
                                'Ligar D3',
                                'Desligar D5',
                                'Desligar D7',
                                'Desligar D2',
                                'Desligar D4',
                                'Ligar D6',
                                'Ligar D8', ])
        print('7. Dentro do IF \n')
        botao1.configure(command=lambda: Disj3Passo5())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj3Passo4()


def Disj3Passo3():
    print('6. Entrou em Disj3Passo2')
    elem_sel = combo.get()
    print('6.Elemento Selecionado: ' + elem_sel)

    if elem_sel == 'Ligar D4':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor D4 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3',
                                'Abrir S1-2',
                                'Abrir S5-6',
                                'Abrir S9-10',
                                'Abrir S13-14',
                                'Abrir S3-4',
                                'Abrir S7-8',
                                'Fechar S11-12',
                                'Fechar S15-16',
                                'Desligar D1',
                                'Desligar D3',
                                'Desligar D5',
                                'Desligar D7',
                                'Desligar D2',
                                'Desligar D4',
                                'Ligar D6',
                                'Ligar D8', ])
        print('6. Dentro do IF \n')
        botao1.configure(command=lambda: Disj3Passo4())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj3Passo3()


def Disj3Passo2():
    print('5. Entrou em Disj3Passo2')
    elem_sel = combo.get()
    print('5.Elemento Selecionado: ' + elem_sel)

    if elem_sel == 'Fechar S7-8':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S7 e S8 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3',
                                'Abrir S1-2',
                                'Abrir S5-6',
                                'Abrir S9-10',
                                'Abrir S13-14',
                                'Abrir S3-4',
                                'Abrir S7-8',
                                'Fechar S11-12',
                                'Fechar S15-16',
                                'Desligar D1',
                                'Desligar D3',
                                'Desligar D5',
                                'Desligar D7',
                                'Desligar D2',
                                'Ligar D4',
                                'Ligar D6',
                                'Ligar D8', ])
        combo.set('')
        print('5. Dentro do IF \n')
        botao1.configure(command=lambda: Disj3Passo3())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj3Passo2()


def DisjD3Passo1():
    print('4. Entrou em Disj3Passo1')
    elem_sel = combo.get()
    print('4.Elemento Selecionado: ' + elem_sel)

    if elem_sel == 'Ligar D2':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D2 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3',
                                'Abrir S1-2',
                                'Abrir S5-6',
                                'Abrir S9-10',
                                'Abrir S13-14',
                                'Abrir S3-4',
                                'Fechar S7-8',
                                'Fechar S11-12',
                                'Fechar S15-16',
                                'Desligar D1',
                                'Desligar D3',
                                'Desligar D5',
                                'Desligar D7',
                                'Desligar D2',
                                'Ligar D4',
                                'Ligar D6',
                                'Ligar D8', ])
        combo.set('')
        print('4. Dentro do IF \n')
        botao1.configure(command=lambda: Disj3Passo2())
    else:
        print('4. Dentro do ELSE \n')
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        DisjD3Passo1()


def analiseD3():
    print('3. Inicialização da análise')
    elem_sel = combo.get()
    print('3. Elemento Selecionado: ' + elem_sel)

    if elem_sel == 'Fechar S3-4':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S3 e S4 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3',
                                'Abrir S1-2',
                                'Abrir S5-6',
                                'Abrir S9-10',
                                'Abrir S13-14',
                                'Abrir S3-4',
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
                                'Ligar D8', ])
        combo.set('')
        print('3. Dentro do IF \n')
        botao1.configure(command=lambda: DisjD3Passo1())
    else:
        print('3. Dentro do ELSE \n')
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        analiseD3()


def selectFalha():
    print('2. Seleção do Disjuntor com Falha')
    elem_sel = combo.get()
    elem_falha = elem_sel
    print('2. Elemento com Falha: ' + elem_falha)
    telaInt.configure(text='--------------------------------------------------------------\n'
                           'Falha no ' + elem_falha + '\n'
                           'Selecione o próximo passo:\n'
                           '--------------------------------------------------------------')
    combo.configure(values=['Abrir S1-2',
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
                            'Ligar D8', ])
    combo.set('')
    botao1.configure(text='Próximo Passo')
    botao2.configure(text='Sair')

    if elem_sel == 'Disjuntor D1':
        newImage = PhotoImage(file='img/bar6D3a.png')
        diagrama.configure(image=newImage)

        def analiseD1():
            pass

        botao1.configure(command=lambda: analiseD1())

    elif elem_sel == 'Disjuntor D3':
        newImage = PhotoImage(file='img/bar6D3a.png')
        diagrama.create_image(0, 0, image=newImage, anchor=NW)

        print('2. Dentro do IF \n')

        botao1.configure(text='Próximo Passo', command=lambda: analiseD3())

    elif elem_sel == 'Disjuntor D5':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)

        def analiseD5():
            pass

        botao1.configure(command=lambda: analiseD5())

    elif elem_sel == 'Disjuntor D7':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)

        def analiseD7():
            pass

        botao1.configure(command=lambda: analiseD7())


container1 = Frame(app, bd=4, relief=GROOVE)
container2 = Frame(app, bd=4, relief=GROOVE)
subcontainer1 = LabelFrame(container2, bg="#dde", bd=4, relief=GROOVE)
subcontainer2 = LabelFrame(container2, text='ELEMENTO(S)', font='times 12 bold', bd=4)
subcontainer3 = LabelFrame(container2, bd=4)
container1.pack(side='left', padx=10, pady=10)
container2.pack(side='left', fill='y', padx=10, pady=10)
subcontainer1.pack(fill='both', expand='yes', padx=10, pady=10)
subcontainer2.pack(fill='both', expand='yes', padx=10, pady=10)
subcontainer3.pack(fill='both', expand='yes', padx=10, pady=10)


# Objeto imagem:
image = PhotoImage(file='img/bar6.png')
diagrama = Canvas(container1, bg='white', height=1000, width=700)
diagrama.create_image(0, 0, image=image, anchor=NW)
#diagrama = Label(container1, image=image)
diagrama.pack(expand=True, fill='both')


# Criação Tela Interativa
telaInt = Label(subcontainer1,
                text='--------------------------------------------------------------\n'
                     'Barramento Duplo com Disjuntor Duplo\n\n'
                     'Defina o elemento com falha!\n'
                     '--------------------------------------------------------------',
                font='times 14 bold',
                justify='center',
                bg="#dde")
telaInt.pack(fill='both', expand='yes', padx=10, pady=10)


# Criação Combobox
ComboVar = StringVar()
combo = ttk.Combobox(subcontainer2, textvariable=ComboVar, font=('Times New Roman', '14'), state='readonly')
combo['values'] = ['Disjuntor D1',
                   'Disjuntor D3',
                   'Disjuntor D5',
                   'Disjuntor D7',
                   ]
combo.pack(fill='x', padx=10, pady=10)


# Criação Botões
botao1 = Button(subcontainer3, text='Iniciar Manobra', font=('Times New Roman', '14'), command=lambda: selectFalha())
botao2 = Button(subcontainer3, text='Sair', font=('Times New Roman', '14'), command=lambda: app.destroy())
botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)

print('1. Programa iniciado\n')


app.mainloop()
