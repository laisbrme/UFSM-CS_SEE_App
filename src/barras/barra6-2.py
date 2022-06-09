from tkinter import ttk
from tkinter import *


app = Tk()
app.title("Barramento Duplo com Disjuntor Duplo")
#app.iconbitmap('img/ufsm-see.ico')


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
diagrama = Canvas(container1, bg='white', height=900, width=620)
diagrama.create_image(0,0, image=image, anchor=NW)
#diagrama = Label(container1, image=image)
diagrama.pack(expand=True, fill='both')


# Criação Tela Interativa
telaInt = Label(subcontainer1,
                     text='--------------------------------------------------------------\n' \
                          'Barramento Duplo com Disjuntor Duplo\n\n' \
                          'Defina o elemento com falha!\n' \
                          '--------------------------------------------------------------',
                     font='times 14 bold',
                     justify='center',
                     bg="#dde")
telaInt.pack(fill='both', expand='yes', padx=10, pady=10)

# Criação Combobox
ComboVar = StringVar()
combo = ttk.Combobox(subcontainer2, textvariable=ComboVar,font=('Times New Roman', '14'), state='readonly')
combo['values'] = ['Disjuntor D1',
                   'Disjuntor D3',
                   'Disjuntor D5',
                   'Disjuntor D7',]
combo.pack(fill='x', padx=10, pady=10)

def ComboGet():
    Var = combo.get()
    print('Entrou na função ComboGet()')
    return Var

def selectFalha():
    print('2. Seleção do Disjuntor com Falha')
    ElemSel = ComboGet()
    ElemFalha = ElemSel
    print('2. Elemento com Falha: ' + ElemFalha + '\n')

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


        def analiseD1():
            pass

        botao1.configure(text='Próximo Passo', command=lambda: analiseD1())
        botao2.configure(text='Finalizar Manobra')

    elif ElemSel == 'Disjuntor D3':

        newImage = PhotoImage(file='img/bar5.png')
        diagrama.create_image(0,0, image=newImage, anchor=NW)
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

        def analiseD3():
            print('3. Inicialização da análise')
            ElemSel = ComboGet()
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

                def D3P1():
                    print('4. Entrou em D3P1')
                    ElemSel = ComboGet()
                    print('4. Elemento Selecionado: ' + ElemSel)
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
                    else:
                        telaInt.configure(text='--------------------------------------------------------------\n' \
                                               'Seleção inválida!\n' \
                                               'Selecione o próximo passo:\n' \
                                               '--------------------------------------------------------------')
                        D3P1()

                botao1.configure(command=D3P1())
            else:
                telaInt.configure(text='--------------------------------------------------------------\n' \
                                       'Seleção inválida!\n' \
                                       'Selecione o próximo passo:\n' \
                                       '--------------------------------------------------------------')
                analiseD3()

        botao1.configure(text='Próximo Passo', command=lambda: analiseD3())
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


# Criação Botões
botao1 = Button(subcontainer3, text='Iniciar Manobra', font='times 14', command=lambda:selectFalha())
botao2 = Button(subcontainer3, text='Sair', font='times 14', command=lambda:app.destroy())
botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)

print('1. Programa iniciado\n')

app.mainloop()