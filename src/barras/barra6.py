from tkinter import ttk
from tkinter import *


app = Tk()
app.title("Barramento Duplo com Disjuntor Duplo")
#app.iconbitmap('img/ufsm-see.ico')

def clicouB1():
    ElemSel = combo.get()
    return ElemSel

def finaliza(diagrama, telaInt, combo, botao1, ElemFalha):
    ElemFalha = ElemSel
    if ElemFalha == 'Disjuntor D1':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D1 finalizada!\n'
                               '--------------------------------------------------------------')
        botao1.destroy()

    elif ElemSel == 'Disjuntor D3':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D3 finalizada!\n'
                               '--------------------------------------------------------------')
        botao1.destroy()

    elif ElemSel == 'Disjuntor D5':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D5 finalizada!\n'
                               '--------------------------------------------------------------')
        botao1.destroy()

    elif ElemSel == 'Disjuntor D7':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D7 finalizada!\n'
                               '--------------------------------------------------------------')
        botao1.destroy()

def analiseD1(diagrama, telaInt, combo, botao1, ElemFalha):
    pass

def D3P6(diagrama, telaInt, combo, botao1, ElemFalha):
    if ElemSel == 'Trocar D3':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Seccionadoras S5 e S6 abertas\n' \
                               'Selecione o próximo passo:\n' \
                               '--------------------------------------------------------------')
        combo.configure(values=['Abrir S1-2',
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
        ElemSel = combo.get()
        botao1.configure(command=finaliza(diagrama, telaInt, combo, botao1, ElemFalha))
    else:
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Seleção inválida!\n' \
                               'Selecione o próximo passo:\n' \
                               '--------------------------------------------------------------')
        D3P6(diagrama, telaInt, combo, botao1, ElemFalha)

def D3P5(diagrama, telaInt, combo, botao1, ElemFalha):
    if ElemSel == 'Abrir S5-6':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Seccionadoras S5 e S6 abertas\n' \
                               'Selecione o próximo passo:\n' \
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
        ElemSel = combo.get()
        botao1.configure(command=D3P6(diagrama, telaInt, combo, botao1, ElemFalha))
    else:
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Seleção inválida!\n' \
                               'Selecione o próximo passo:\n' \
                               '--------------------------------------------------------------')
        D3P5(diagrama, telaInt, combo, botao1, ElemFalha)

def D3P4(diagrama, telaInt, combo, botao1, ElemFalha):
    if ElemSel == 'Desligar D3':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Disjuntor D3 desligado\n' \
                               'Selecione o próximo passo:\n' \
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
        ElemSel = combo.get()
        botao1.configure(command=D3P5(diagrama, telaInt, combo, botao1, ElemFalha))
    else:
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Seleção inválida!\n' \
                               'Selecione o próximo passo:\n' \
                               '--------------------------------------------------------------')
        D3P4(diagrama, telaInt, combo, botao1, ElemFalha)

def D3P3(diagrama, telaInt, combo, botao1, ElemFalha):
    if ElemSel == 'Ligar D4':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Disjuntor D4 ligado\n' \
                               'Selecione o próximo passo:\n' \
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
        ElemSel = combo.get()
        botao1.configure(command=D3P4(diagrama, telaInt, combo, botao1, ElemFalha))
    else:
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Seleção inválida!\n' \
                               'Selecione o próximo passo:\n' \
                               '--------------------------------------------------------------')
        D3P3(diagrama, telaInt, combo, botao1, ElemFalha)

def D3P2(diagrama, telaInt, combo, botao1, ElemFalha):
    print('8. Entrou em D3P2')
    ElemSel = combo.get()
    print('Elemento Selecionado: ' + ElemSel)
    print('Elemento com falha: ' + ElemFalha)
    if ElemSel == 'Fechar S7-8':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Seccionadoras S7 e S8 fechadas\n' \
                               'Selecione o próximo passo:\n' \
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
        ElemSel = combo.get()
        botao1.configure(command=D3P3(diagrama, telaInt, combo, botao1, ElemFalha))
        print('9. Saindo de D3P2')
    else:
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Seleção inválida!\n' \
                               'Selecione o próximo passo:\n' \
                               '--------------------------------------------------------------')
        D3P2(diagrama, telaInt, combo, botao1, ElemFalha)

def D3P1(diagrama, telaInt, combo, botao1, ElemFalha):
    print('6. Entrou em D3P1')
    ElemSel = combo.get()
    print('Elemento Selecionado: ' + ElemSel)
    print('Elemento com falha: ' + ElemFalha)
    if ElemSel == 'Ligar D2':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Disjuntor de transferência D2 ligado\n' \
                               'Selecione o próximo passo:\n' \
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
        ElemSel = combo.get()
        print('Elemento selecionado dentro do if é ' + ElemSel)
        botao1.configure(command=D3P2(diagrama, telaInt, combo, botao1, ElemFalha))
        print('7. Saindo de D3P1')
    else:
        telaInt.configure(text='--------------------------------------------------------------\n' \
                               'Seleção inválida!\n' \
                               'Selecione o próximo passo:\n' \
                               '--------------------------------------------------------------')
        D3P1(diagrama, telaInt, combo, botao1, ElemFalha)

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
diagrama = Label(container1, image=image)

# Criação Tela Interativa
telaInt = Label(subcontainer1,
                     text='--------------------------------------------------------------\n' \
                          'Barramento Duplo com Disjuntor Duplo\n\n' \
                          'Defina o elemento com falha!\n' \
                          '--------------------------------------------------------------',
                     font='times 14 bold',
                     justify='center',
                     bg="#dde")

# Criação Combobox
combo = ttk.Combobox(subcontainer2, font=('Times New Roman', '14'), state='readonly')
combo['values'] = ['Disjuntor D1',
                   'Disjuntor D3',
                   'Disjuntor D5',
                   'Disjuntor D7',]

def selectFalha():
    print('2. Seleção do Disjuntor com Falha')
    ElemSel = combo.get()
    ElemFalha = ElemSel
    print('2. Elemento com Falha: ' + ElemFalha + '\n')
    combo.delete(0, END)

    if ElemSel == 'Disjuntor D1':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Falha no Disjuntor D1\n'
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
        ElemSel = combo.get()

        def analiseD1(diagrama, telaInt, combo, botao1, ElemFalha):
            pass

        botao1.configure(text='Próximo Passo', command=lambda: analiseD1(diagrama, telaInt, combo, botao1, ElemFalha))
        botao2.configure(text='Finalizar Manobra')

    elif ElemSel == 'Disjuntor D3':

        #newImage = PhotoImage(file='img/bar6.png')
        #diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Falha no Disjuntor D3\n'
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

        print('3. Primeiro Passo: ' + ElemSel)

        combo.delete(0, END)
        def analiseD3(diagrama, telaInt, combo, botao1):
            print('3. Inicialização da análise')
            ElemSel = combo.get()
            print('3. Elemento Selecionado: ' + ElemSel)
            if ElemSel == 'Fechar S3-4':
                # newImage = PhotoImage(file='img/bar6.png')
                # diagrama.configure(image=newImage)
                telaInt.configure(text='--------------------------------------------------------------\n' \
                                       'Seccionadoras S3 e S4 fechadas\n' \
                                       'Selecione o próximo passo:\n' \
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
                print('3. Dentro do ELSE: ' + ElemSel)
                botao1.configure(command=D3P1(diagrama, telaInt, combo, botao1, ElemFalha))
                print('3. Primeiro Passo Selecionado')
            else:
                telaInt.configure(text='--------------------------------------------------------------\n' \
                                       'Seleção inválida!\n' \
                                       'Selecione o próximo passo:\n' \
                                       '--------------------------------------------------------------')
                analiseD3(diagrama, telaInt, combo, botao1, ElemFalha)

            combo.delete(0, END)

        combo.delete(0, END)

        botao1.configure(text='Próximo Passo', command=lambda: analiseD3(diagrama, telaInt, combo, botao1, ElemFalha))
        botao2.configure(text='Finalizar Manobra')

    elif ElemSel == 'Disjuntor D5':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Falha no Disjuntor D5\n'
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

        def analiseD5(diagrama, telaInt, combo, botao1, ElemFalha):
            pass

        botao1.configure(text='Próximo Passo', command=lambda: analiseD5(diagrama, telaInt, combo, botao1, ElemFalha))
        botao2.configure(text='Finalizar Manobra')

    elif ElemSel == 'Disjuntor D7':
        # newImage = PhotoImage(file='img/bar6.png')
        # diagrama.configure(image=newImage)
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Falha no Disjuntor D7\n'
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

        def analiseD7(diagrama, telaInt, combo, botao1, ElemFalha):
            pass

        botao1.configure(text='Próximo Passo', command=lambda: analiseD7(diagrama, telaInt, combo, botao1, ElemFalha))
        botao2.configure(text='Finalizar Manobra')

    combo.delete(0, END)

# Criação Botões
botao1 = Button(subcontainer3, text='Iniciar Manobra', font='times 14', command= lambda:selectFalha())
botao2 = Button(subcontainer3, text='Sair', font='times 14', command=lambda:app.destroy())

# Exibição
diagrama.pack(fill='both')
telaInt.pack(fill='both', expand='yes', padx=10, pady=10)
combo.pack(fill='x', padx=10, pady=10)
botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)

print('1. Programa iniciado\n')

#combo.bind('<<ComboboxSelected>>', clicouB1)
#botao1.bind('<Button-1>', True)
#botao2.bind('<Button-1>', app.destroy())


app.mainloop()