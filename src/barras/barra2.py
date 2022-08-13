from tkinter import ttk
from tkinter import *


app = Tk()
app.title("Barramento Principal com Barra de Transferência")
#app.iconbitmap('img/ufsm-see.ico')

def finaliza(elem_sel):
    if elem_sel == 'Trocar D3':
        newImage = PhotoImage(file='img/bar2/bar2D3.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D3 finalizada!\n'
                               '--------------------------------------------------------------')


    elif elem_sel == 'Trocar D4':
        newImage = PhotoImage(file='img/bar2/bar2D4.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D4 finalizada!\n'
                               '--------------------------------------------------------------')

    elif elem_sel == 'Trocar D5':
        newImage = PhotoImage(file='img/bar2/bar2D5.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D5 finalizada!\n'
                               '--------------------------------------------------------------')

    elif elem_sel == 'Trocar D6':
        newImage = PhotoImage(file='img/bar2/bar2D6.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D6 finalizada!\n'
                               '--------------------------------------------------------------')

def Disj3Passo1():
	elem_sel = combo.get()

	if elem_sel == 'Ligar DT':
		newImage = PhotoImage(file='img/bar2/bar2D3c.png')
		diagrama.configure(image=newImage)
		diagrama.image = newImage

		telaInt.configure(text='--------------------------------------------------------------\n'
							   'Disjuntor DT ligado\n'
							   'Selecione o próximo passo:\n'
							   '--------------------------------------------------------------')
		combo.configure(values=['Abrir S7-S8',
								'Abrir S9-S10',
								'Abrir S11-S12',
								'Abrir S13-S14',
								'Abrir S15-S16',
								'Fechar S17',
								'Fechar S18',
								'Fechar S19',
								'Fechar S20',
								'Desligar DT',
								'Desligar D3',
								'Desligar D4',
								'Desligar D5',
								'Desligar D6',])
		combo.set('')

		botao1.configure(command=lambda: Disj3Passo2())
	else:
		telaInt.configure(text='--------------------------------------------------------------\n'
							   'Seleção inválida!\n'
							   'Selecione o próximo passo:\n'
							   '--------------------------------------------------------------')
		Disj3Passo1()
							   
def analiseD3():
	elem_sel = combo.get()

	if elem_sel == 'Fechar S15-S16':
		newImage = PhotoImage(file='img/bar2/bar2D3b.png')
		diagrama.configure(image=newImage)
		diagrama.image = newImage

		telaInt.configure(text='--------------------------------------------------------------\n'
							   'Seccionadoras S15 e S16 fechadas\n'
							   'Selecione o próximo passo:\n'
							   '--------------------------------------------------------------')
		combo.configure(values=['Abrir S7-S8',
								'Abrir S9-S10',
								'Abrir S11-S12',
								'Abrir S13-S14',
								'Abrir S15-S16',
								'Fechar S17',
								'Fechar S18',
								'Fechar S19',
								'Fechar S20',
								'Ligar DT',
								'Desligar D3',
								'Desligar D4',
								'Desligar D5',
								'Desligar D6',])
		combo.set('')

		botao1.configure(command=lambda: Disj3Passo1())
	else:
		telaInt.configure(text='--------------------------------------------------------------\n'
							   'Seleção inválida!\n'
							   'Selecione o próximo passo:\n'
							   '--------------------------------------------------------------')
		analiseD3()

def selectFalha():
    elem_sel = combo.get()
    elem_falha = elem_sel
    telaInt.configure(text='--------------------------------------------------------------\n'
                           'Falha no ' + elem_falha + '\n'
                           'Selecione o próximo passo:\n'
                           '--------------------------------------------------------------')
    combo.configure(values=['Abrir S7-S8',
							'Abrir S9-S10',
							'Abrir S11-S12',
							'Abrir S13-S14',
							'Fechar S15-S16',
							'Fechar S17',
							'Fechar S18',
							'Fechar S19',
							'Fechar S20',
							'Ligar DT',
                            'Desligar D3',
                            'Desligar D4',
							'Desligar D5',
							'Desligar D6',])
    combo.set('')
    botao1.configure(text='Próximo Passo')
    botao2.configure(text='Sair')

    if elem_sel == 'Disjuntor D3':
        newImage = PhotoImage(file='img/bar2/bar2D3a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        botao1.configure(command=lambda: analiseD3())

    elif elem_sel == 'Disjuntor D4':
        newImage = PhotoImage(file='img/bar2/bar2D4a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        botao1.configure(command=lambda: analiseD4())

    elif elem_sel == 'Disjuntor D5':
        newImage = PhotoImage(file='img/bar2/bar2D5a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        botao1.configure(command=lambda: analiseD5())

    elif elem_sel == 'Disjuntor D6':
        newImage = PhotoImage(file='img/bar2/bar2D6a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        botao1.configure(command=lambda: analiseD6())

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
image = PhotoImage(file='img/bar2/bar2.png')
diagrama = Label(container1, image=image)
diagrama.pack(expand=True, fill='both')


# Criação Tela Interativa
telaInt = Label(subcontainer1,
                text='--------------------------------------------------------------\n'
                     'Barramento Principal com Barra de Transferência\n\n'
                     'Defina o elemento com falha!\n'
                     '--------------------------------------------------------------',
                font='times 14 bold',
                justify='center',
                bg="#dde")
telaInt.pack(fill='both', expand='yes', padx=10, pady=10)


# Criação Combobox
ComboVar = StringVar()
combo = ttk.Combobox(subcontainer2, textvariable=ComboVar, font=('Times New Roman', '14'), state='readonly')
combo['values'] = ['Disjuntor D3',
                   'Disjuntor D4',
				   'Disjuntor D5',
				   'Disjuntor D6',
                   ]
combo.pack(fill='x', padx=10, pady=10)


# Criação Botões
botao1 = Button(subcontainer3, text='Iniciar Manobra', font=('Times New Roman', '14'), command=lambda: selectFalha())
botao2 = Button(subcontainer3, text='Sair', font=('Times New Roman', '14'), command=lambda: app.destroy())
botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)


app.mainloop()