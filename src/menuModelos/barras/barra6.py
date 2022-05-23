import os
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


app = Tk()
app.title("Barramento Duplo com Disjuntor Duplo")
app.iconbitmap('img/ufsm-see.ico')


def analiseD1(diagrama, telaInt, combo, botao1):
    pass

def analiseD3(diagrama, telaInt, combo, botao1):
    #newImage = PhotoImage(file='img/bar5.png')
    #diagrama.configure(image=newImage)
    telaInt.configure(text='Falha no Disjuntor D3\nSelecione o próximo passo:')
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
    botao1.configure(text='Próximo Passo', command= lambda:analiseD3(diagrama, telaInt, combo, botao1))
    botao2.configure(text='Finalizar Manobra')
    while combo.get() != 'Fechar S3-4' and botao1.bind() == True:
        print('entrou no while')
        telaInt.configure(text='Seleção inválida!\nSelecione o próximo passo:')
    else:
        print('não entrou no while')


def analiseD5(diagrama, telaInt, combo, botao1):
    pass

def analiseD7(diagrama, telaInt, combo, botao1):
    pass

def cliclouB1(diagrama, telaInt, combo, botao1):
    print('Entrou na função clicou botão 1')
    ElemSel = combo.get()
    if ElemSel == 'Disjuntor D1':
        print(ElemSel)
        analiseD1(diagrama, telaInt, combo, botao1)

    elif ElemSel == 'Disjuntor D3':
        print(ElemSel)
        analiseD3(diagrama, telaInt, combo, botao1)

    elif ElemSel == 'Disjuntor D5':
        print(ElemSel)
        analiseD5(diagrama, telaInt, combo, botao1)

    elif ElemSel == 'Disjuntor D7':
        print(ElemSel)
        analiseD7(diagrama, telaInt, combo, botao1)


container1 = Frame(app, bd=4, relief=GROOVE)
container2 = Frame(app, bd=4, relief=GROOVE)
subcontainer1 = LabelFrame(container2, bg="#dde", bd=4, relief=GROOVE)
subcontainer2 = LabelFrame(container2, text='Elemento(s)', bd=4)
subcontainer3 = LabelFrame(container2, bd=4)
container1.pack(side='left', padx=10, pady=10)
container2.pack(side='left', fill='y', padx=10, pady=10)
subcontainer1.pack(fill='both', expand='yes', padx=10, pady=10)
subcontainer2.pack(fill='both', expand='yes', padx=10, pady=10)
subcontainer3.pack(fill='both', expand='yes', padx=10, pady=10)


# Objeto imagem:
img = PhotoImage(file='img/bar6.png')
diagrama = Label(container1, image=img)

# Criação Tela Interativa
telaInt = Label(subcontainer1,
                     text='--------------------------------------------------------------\n' \
                          'Barramento Duplo com Disjuntor Duplo\n\n' \
                          'Defina o elemento com falha!\n' \
                          '--------------------------------------------------------------',
                     font='times 12 bold',
                     justify='center',
                     bg="#dde")

# Criação Combobox
clicada = StringVar()
combo = ttk.Combobox(subcontainer2, textvariable=clicada, state='readonly')
combo['values'] = ['Disjuntor D1',
                   'Disjuntor D3',
                   'Disjuntor D5',
                   'Disjuntor D7',]

# Criação Botões
botao1 = Button(subcontainer3, text='Iniciar Manobra', command= lambda:cliclouB1(diagrama, telaInt, combo, botao1))
botao2 = Button(subcontainer3, text='Sair', command=lambda:app.destroy())

# Exibição
diagrama.pack(fill='both')
telaInt.pack(fill='both', expand='yes', padx=10, pady=10)
combo.pack(fill='x', side='left', padx=10, pady=10)
botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)


#combo.bind('<<ComboboxSelected>>', analise)
#botao1.bind('<Button-1>', True)
#botao2.bind('<Button-1>', app.destroy())


app.mainloop()