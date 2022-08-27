from tkinter import ttk
from tkinter import *

def inicio():
	app = Tk()
	app.title("Barramento Principal com Barra de Transferência")
	#app.iconbitmap('img/ufsm-see.ico')

	def finaliza(elem_sel):
		if elem_sel == 'Trocar D3':
			newImage = PhotoImage(file='img/bar2/bar2D3h.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Manobra em Disjuntor D3 finalizada!\n'
								   '------------------------------------------------------------------------')


		elif elem_sel == 'Trocar D4':
			newImage = PhotoImage(file='img/bar2/bar2D4h.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Manobra em Disjuntor D4 finalizada!\n'
								   '------------------------------------------------------------------------')

		elif elem_sel == 'Trocar D5':
			newImage = PhotoImage(file='img/bar2/bar2D5h.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Manobra em Disjuntor D5 finalizada!\n'
								   '------------------------------------------------------------------------')

		elif elem_sel == 'Trocar D6':
			newImage = PhotoImage(file='img/bar2/bar2D6h.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Manobra em Disjuntor D6 finalizada!\n'
								   '------------------------------------------------------------------------')


	def Disj6Passo5():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D6':
			newImage = PhotoImage(file='img/bar2/bar2D6g.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor D6 trocado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.pack_forget()

			botao1.configure(command=lambda: finaliza('Trocar D6'))
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj6Passo5()


	def Disj6Passo4():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S13-S14':
			newImage = PhotoImage(file='img/bar2/bar2D6f.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadoras S13 e S14 abertas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Fechar S13-S14',
									'Abrir S15-S16',
									'Fechar S17',
									'Fechar S18',
									'Fechar S19',
									'Abrir S20',
									'Desligar DT',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj6Passo5())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj6Passo4()


	def Disj6Passo3():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D6':
			newImage = PhotoImage(file='img/bar2/bar2D6e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor D6 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Fechar S17',
									'Fechar S18',
									'Fechar S19',
									'Abrir S20',
									'Desligar DT',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj6Passo4())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj6Passo3()


	def Disj6Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S20':
			newImage = PhotoImage(file='img/bar2/bar2D6d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadora S20 fechada\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Fechar S17',
									'Fechar S18',
									'Fechar S19',
									'Abrir S20',
									'Desligar DT',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj6Passo3())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj6Passo2()


	def Disj6Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Ligar DT':
			newImage = PhotoImage(file='img/bar2/bar2D6c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor DT ligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S7-S8',
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

			botao1.configure(command=lambda: Disj6Passo2())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj6Passo1()


	def analiseD6():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S15-S16':
			newImage = PhotoImage(file='img/bar2/bar2D6b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadoras S15 e S16 fechadas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S7-S8',
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

			botao1.configure(command=lambda: Disj6Passo1())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			analiseD5()


	def Disj5Passo5():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D5':
			newImage = PhotoImage(file='img/bar2/bar2D5g.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor D5 trocado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.pack_forget()

			botao1.configure(command=lambda: finaliza('Trocar D5'))
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo5()


	def Disj5Passo4():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S11-S12':
			newImage = PhotoImage(file='img/bar2/bar2D5f.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadoras S11 e S12 abertas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Fechar S17',
									'Fechar S18',
									'Abrir S19',
									'Fechar S20',
									'Desligar DT',
									'Desligar D3',
									'Desligar D4',
									'Ligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo5())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo4()


	def Disj5Passo3():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D5':
			newImage = PhotoImage(file='img/bar2/bar2D5e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor D5 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Fechar S17',
									'Fechar S18',
									'Abrir S19',
									'Fechar S20',
									'Desligar DT',
									'Desligar D3',
									'Desligar D4',
									'Ligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo4())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo3()


	def Disj5Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S19':
			newImage = PhotoImage(file='img/bar2/bar2D5d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadora S19 fechada\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Fechar S17',
									'Fechar S18',
									'Abrir S19',
									'Fechar S20',
									'Desligar DT',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo3())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo2()


	def Disj5Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Ligar DT':
			newImage = PhotoImage(file='img/bar2/bar2D5c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor DT ligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S7-S8',
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

			botao1.configure(command=lambda: Disj5Passo2())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo1()


	def analiseD5():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S15-S16':
			newImage = PhotoImage(file='img/bar2/bar2D5b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadoras S15 e S16 fechadas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S7-S8',
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

			botao1.configure(command=lambda: Disj5Passo1())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			analiseD5()


	def Disj4Passo5():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D4':
			newImage = PhotoImage(file='img/bar2/bar2D4g.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor D4 trocado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.pack_forget()

			botao1.configure(command=lambda: finaliza('Trocar D4'))
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo5()


	def Disj4Passo4():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S9-S10':
			newImage = PhotoImage(file='img/bar2/bar2D4f.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadoras S9 e S10 abertas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S7-S8',
									'Fechar S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Fechar S17',
									'Abrir S18',
									'Fechar S19',
									'Fechar S20',
									'Desligar DT',
									'Desligar D3',
									'Ligar D4',
									'Desligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo5())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo4()


	def Disj4Passo3():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D4':
			newImage = PhotoImage(file='img/bar2/bar2D4e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor D4 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Fechar S17',
									'Abrir S18',
									'Fechar S19',
									'Fechar S20',
									'Desligar DT',
									'Desligar D3',
									'Ligar D4',
									'Desligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo4())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo3()


	def Disj4Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S18':
			newImage = PhotoImage(file='img/bar2/bar2D4d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadora S18 fechada\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Fechar S17',
									'Abrir S18',
									'Fechar S19',
									'Fechar S20',
									'Desligar DT',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo3())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo2()


	def Disj4Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Ligar DT':
			newImage = PhotoImage(file='img/bar2/bar2D4c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor DT ligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S7-S8',
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

			botao1.configure(command=lambda: Disj4Passo2())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo1()


	def analiseD4():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S15-S16':
			newImage = PhotoImage(file='img/bar2/bar2D4b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadoras S15 e S16 fechadas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S7-S8',
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

			botao1.configure(command=lambda: Disj4Passo1())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			analiseD4()



	def Disj3Passo5():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D3':
			newImage = PhotoImage(file='img/bar2/bar2D3g.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor D3 trocado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.pack_forget()

			botao1.configure(command=lambda: finaliza('Trocar D3'))
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo5()


	def Disj3Passo4():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S7-S8':
			newImage = PhotoImage(file='img/bar2/bar2D3f.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadoras S7 e S8 abertas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Fechar S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Abrir S17',
									'Fechar S18',
									'Fechar S19',
									'Fechar S20',
									'Desligar DT',
									'Ligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo5())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo4()


	def Disj3Passo3():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D3':
			newImage = PhotoImage(file='img/bar2/bar2D3e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor D3 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Abrir S17',
									'Fechar S18',
									'Fechar S19',
									'Fechar S20',
									'Desligar DT',
									'Ligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo4())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo3()


	def Disj3Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S17':
			newImage = PhotoImage(file='img/bar2/bar2D3d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadora S17 fechada\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Abrir S15-S16',
									'Abrir S17',
									'Fechar S18',
									'Fechar S19',
									'Fechar S20',
									'Desligar DT',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo3())
		else:
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo2()


	def Disj3Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Ligar DT':
			newImage = PhotoImage(file='img/bar2/bar2D3c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Disjuntor DT ligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S7-S8',
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
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo1()


	def analiseD3():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S15-S16':
			newImage = PhotoImage(file='img/bar2/bar2D3b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seccionadoras S15 e S16 fechadas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S7-S8',
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
			telaInt.configure(text='----------------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			analiseD3()


	def selectFalha():
		elem_sel = combo.get()
		elem_falha = elem_sel
		telaInt.configure(text='----------------------------------------------------------------------------------\n'
							   'Falha no ' + elem_falha + '\n\n'
							   'Selecione o próximo passo:\n'
							   '------------------------------------------------------------------------')
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
					text='------------------------------------------------------------------------\n'
						 'Barramento Principal com Barra de Transferência\n\n'
						 'Defina o elemento com falha!\n'
						 '------------------------------------------------------------------------',
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

inicio()