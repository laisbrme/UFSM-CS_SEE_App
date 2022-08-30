from tkinter import ttk
from tkinter import *


def inicia():
	app = Tk()
	app.title("Barramento em Anel")
	#app.iconbitmap('img/ufsm-see.ico')


	def finaliza(elem_sel):
		if elem_sel == 'Trocar D3':
			newImage = PhotoImage(file='img/bar9/bar9D3g.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Manobra em Disjuntor D3 finalizada!\n'
								   '--------------------------------------------------------------')

		elif elem_sel == 'Trocar D6':
			newImage = PhotoImage(file='img/bar9/bar9D6g.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Manobra em Disjuntor D6 finalizada!\n'
								   '--------------------------------------------------------------')


	def Disj6Passo4():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D6':
			newImage = PhotoImage(file='img/bar9/bar9D6f.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(
				text='--------------------------------------------------------------\n'
					 'Disjuntor D6 trocado\n\n'
					 'Selecione o próximo passo:\n'
					 '--------------------------------------------------------------')
			combo.pack_forget()
			
			botao1.configure(command=lambda: finaliza())
		else:
			telaInt.configure(
				text='--------------------------------------------------------------\n'
					 'Seleção inválida!\n'
					 'Selecione o próximo passo:\n'
					 '--------------------------------------------------------------')
			Disj6Passo4()


	def Disj6Passo3():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S13-S14':
			newImage = PhotoImage(file='img/bar9/bar9D6e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionadoras S13 e S14 abertas\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S1-S2',
									'Abrir S4-S5',
									'Abrir S7-S8',
									'Fechar S13-S14',
									'Fechar S3',
									'Fechar S6',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Ligar D6',
									'Desligar D4',
									'Ligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj6Passo4())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			Disj6Passo3()
			
			
	def Disj6Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D6':
			newImage = PhotoImage(file='img/bar9/bar9D6d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D6 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S1-S2',
									'Abrir S4-S5',
									'Abrir S7-S8',
									'Abrir S13-S14',
									'Fechar S3',
									'Fechar S6',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Ligar D6',
									'Desligar D4',
									'Ligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj6Passo3())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			Disj6Passo2()

			
	def Disj6Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Ligar D4':
			newImage = PhotoImage(file='img/bar9/bar9D6c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D4 ligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S1-S2',
									'Abrir S4-S5',
									'Abrir S7-S8',
									'Abrir S13-S14',
									'Fechar S3',
									'Fechar S6',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D6',
									'Desligar D4',
									'Ligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj6Passo2())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			Disj6Passo1()

			
	def analiseD6():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S9-S10':
			newImage = PhotoImage(file='img/bar9/bar9D6b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionaddoras S9 e S10 fechadas\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S1-S2',
									'Abrir S4-S5',
									'Abrir S7-S8',
									'Abrir S13-S14',
									'Fechar S3',
									'Fechar S6',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D6',
									'Ligar D4',
									'Ligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj6Passo1())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			analiseD6()

			
	def Disj3Passo4():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D3':
			newImage = PhotoImage(file='img/bar9/bar9D3f.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(
				text='--------------------------------------------------------------\n'
					 'Disjuntor D3 trocado\n\n'
					 'Selecione o próximo passo:\n'
					 '--------------------------------------------------------------')
			combo.pack_forget()
			
			botao1.configure(command=lambda: finaliza())
		else:
			telaInt.configure(
				text='--------------------------------------------------------------\n'
					 'Seleção inválida!\n'
					 'Selecione o próximo passo:\n'
					 '--------------------------------------------------------------')
			Disj3Passo4()


	def Disj3Passo3():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S7-S8':
			newImage = PhotoImage(file='img/bar9/bar9D3e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionadoras S7 e S8 abertas\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1-S2',
									'Abrir S4-S5',
									'Fechar S7-S8',
									'Abrir S13-S14',
									'Fechar S3',
									'Fechar S6',
									'Fechar S9-S10',
									'Abrir S11-S12',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D6',
									'Ligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo4())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			Disj3Passo3()
			
			
	def Disj3Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D3':
			newImage = PhotoImage(file='img/bar9/bar9D3d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D3 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1-S2',
									'Abrir S4-S5',
									'Abrir S7-S8',
									'Abrir S13-S14',
									'Fechar S3',
									'Fechar S6',
									'Fechar S9-S10',
									'Abrir S11-S12',
									'Desligar D1',
									'Desligar D2',
									'Ligar D3',
									'Desligar D6',
									'Ligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo3())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			Disj3Passo2()

			
	def Disj3Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Ligar D5':
			newImage = PhotoImage(file='img/bar9/bar9D3c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D5 ligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1-S2',
									'Abrir S4-S5',
									'Abrir S7-S8',
									'Abrir S13-S14',
									'Fechar S3',
									'Fechar S6',
									'Fechar S9-S10',
									'Abrir S11-S12',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D6',
									'Ligar D4',
									'Desligar D5',])
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

		if elem_sel == 'Fechar S11-S12':
			newImage = PhotoImage(file='img/bar9/bar9D3b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionaddoras S11 e S12 fechadas\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1-S2',
									'Abrir S4-S5',
									'Abrir S7-S8',
									'Abrir S13-S14',
									'Fechar S3',
									'Fechar S6',
									'Fechar S9-S10',
									'Abrir S11-S12',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D6',
									'Ligar D4',
									'Ligar D5',])
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
							   'Falha no ' + elem_falha + '\n\n'
							   'Selecione o próximo passo:\n'
							   '--------------------------------------------------------------')
		combo.configure(values=['Abrir S1-S2',
								'Abrir S4-S5',
								'Abrir S7-S8',
								'Abrir S13-S14',
								'Fechar S3',
								'Fechar S6',
								'Fechar S9-S10',
								'Fechar S11-S12',
								'Desligar D1',
								'Desligar D2',
								'Desligar D3',
								'Desligar D6',
								'Ligar D4',
								'Ligar D5',])
		combo.set('')
		botao1.configure(text='Próximo Passo')
		botao2.configure(text='Sair')

		if elem_sel == 'Disjuntor D3':
			newImage = PhotoImage(file='img/bar9/bar9D3a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			botao1.configure(command=lambda: analiseD3())

		elif elem_sel == 'Disjuntor D6':
			newImage = PhotoImage(file='img/bar9/bar9D6a.png')
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
	image = PhotoImage(file='img/bar9/bar9.png')
	diagrama = Label(container1, image=image)
	diagrama.pack(expand=True, fill='both')


	# Criação Tela Interativa
	telaInt = Label(subcontainer1,
					text='--------------------------------------------------------------\n'
						 'Barramento em Anel\n\n'
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
					   'Disjuntor D6',
					   ]
	combo.pack(fill='x', padx=10, pady=10)


	# Criação Botões
	botao1 = Button(subcontainer3, text='Iniciar Manobra', font=('Times New Roman', '14'), command=lambda: selectFalha())
	botao2 = Button(subcontainer3, text='Sair', font=('Times New Roman', '14'), command=lambda: app.destroy())
	botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
	botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)


	app.mainloop()


inicia()