from tkinter import ttk
from tkinter import *


def inicia():
	app = Tk()
	app.title("Barramento Duplo com Disjuntor a Quatro Chaves")
	app.iconbitmap('img/ufsm-see.ico')


	def finaliza(elem_sel):
		botao1.pack_forget()

		if elem_sel == 'Trocar D3':
			newImage = PhotoImage(file='img/bar5/bar5D3i.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Manobra em Disjuntor D3 finalizada!\n'
								   '------------------------------------------------------------------------')

		elif elem_sel == 'Trocar D4':
			newImage = PhotoImage(file='img/bar5/bar5D4i.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Manobra em Disjuntor D4 finalizada!\n'
								   '------------------------------------------------------------------------')

		elif elem_sel == 'Trocar D5':
			newImage = PhotoImage(file='img/bar5/bar5D5i.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Manobra em Disjuntor D5 finalizada!\n'
								   '------------------------------------------------------------------------')


	def Disj5Passo6():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D5':
			newImage = PhotoImage(file='img/bar5/bar5D5h.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(
				text='------------------------------------------------------------------------\n'
					 'Disjuntor D5 trocado\n\n'
					 'Selecione o próximo passo:\n'
					 '------------------------------------------------------------------------')
			combo.pack_forget()
			
			botao1.configure(text='Finalizar Manobra', command=lambda: finaliza('Trocar D5'))
		else:
			telaInt.configure(
				text='------------------------------------------------------------------------\n'
					 'Seleção inválida!\n'
					 'Selecione o próximo passo:\n'
					 '------------------------------------------------------------------------')
			Disj5Passo6()


	def Disj5Passo5():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D5':
			newImage = PhotoImage(file='img/bar5/bar5D5g.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor D5 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Fechar S19',
									'Fechar S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Abrir S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Ligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo3())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo5()


	def Disj5Passo4():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S19' or 'Abrir S20':
			newImage = PhotoImage(file='img/bar5/bar5D5f.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
            
			if elem_sel == 'Abrir S19':
				telaInt.configure(text='------------------------------------------------------------------------\n'
                                       'Seccionaddora S19 aberta\n\n'
                                       'Selecione o próximo passo:\n'
                                       '------------------------------------------------------------------------')
			elif elem_sel == 'Abrir S20':
				telaInt.configure(text='------------------------------------------------------------------------\n'
                                       'Seccionaddora S20 aberta\n\n'
                                       'Selecione o próximo passo:\n'
                                       '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Fechar S19',
									'Fechar S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Abrir S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo6())
            
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo4()
	
    
	def Disj5Passo3():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S19':
			newImage = PhotoImage(file='img/bar5/bar5D5e1.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddora S19 aberta\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Fechar S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Abrir S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo4())
            
		elif elem_sel == 'Abrir S20':
			newImage = PhotoImage(file='img/bar5/bar5D5e2.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddora S20 aberta\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Fechar S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Abrir S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo4())
            
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo3()

			
	def Disj5Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S22':
			newImage = PhotoImage(file='img/bar5/bar5D5d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddora S22 fechada\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Abrir S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo5())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo2()

			
	def Disj5Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Ligar DT':
			newImage = PhotoImage(file='img/bar5/bar5D5c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor DT ligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo2())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj5Passo1()

			
	def analiseD5():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S9-S10':
			newImage = PhotoImage(file='img/bar5/bar5D5b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddoras S9 e S10 fechadas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Ligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo1())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			analiseD5()


	def Disj4Passo6():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D4':
			newImage = PhotoImage(file='img/bar5/bar5D4h.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(
				text='------------------------------------------------------------------------\n'
					 'Disjuntor D4 trocado\n\n'
					 'Selecione o próximo passo:\n'
					 '------------------------------------------------------------------------')
			combo.pack_forget()
			
			botao1.configure(text='Finalizar Manobra', command=lambda: finaliza('Trocar D4'))
		else:
			telaInt.configure(
				text='------------------------------------------------------------------------\n'
					 'Seleção inválida!\n'
					 'Selecione o próximo passo:\n'
					 '------------------------------------------------------------------------')
			Disj4Passo6()


	def Disj4Passo5():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D4':
			newImage = PhotoImage(file='img/bar5/bar5D4g.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor D4 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Fechar S15',
									'Fechar S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Abrir S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Ligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo3())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo5()


	def Disj4Passo4():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S15' or 'Abrir S16':
			newImage = PhotoImage(file='img/bar5/bar5D4f.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
            
			if elem_sel == 'Abrir S15':
				telaInt.configure(text='------------------------------------------------------------------------\n'
                                       'Seccionaddora S15 aberta\n\n'
                                       'Selecione o próximo passo:\n'
                                       '------------------------------------------------------------------------')
			elif elem_sel == 'Abrir S16':
				telaInt.configure(text='------------------------------------------------------------------------\n'
                                       'Seccionaddora S16 aberta\n\n'
                                       'Selecione o próximo passo:\n'
                                       '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Fechar S15',
									'Fechar S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Abrir S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo6())
            
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo4()
	
    
	def Disj4Passo3():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S15':
			newImage = PhotoImage(file='img/bar5/bar5D4e1.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddora S15 aberta\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Fechar S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Abrir S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo4())
            
		elif elem_sel == 'Abrir S16':
			newImage = PhotoImage(file='img/bar5/bar5D4e2.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddora S16 aberta\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Fechar S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Abrir S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo4())
            
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo3()

			
	def Disj4Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S18':
			newImage = PhotoImage(file='img/bar5/bar5D4d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddora S18 fechada\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Abrir S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo5())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo2()

			
	def Disj4Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Ligar DT':
			newImage = PhotoImage(file='img/bar5/bar5D4c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor DT ligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo2())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj4Passo1()

			
	def analiseD4():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S9-S10':
			newImage = PhotoImage(file='img/bar5/bar5D4b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddoras S9 e S10 fechadas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Ligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo1())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			analiseD4()


	def Disj3Passo6():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D3':
			newImage = PhotoImage(file='img/bar5/bar5D3h.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(
				text='------------------------------------------------------------------------\n'
					 'Disjuntor D3 trocado\n\n'
					 'Selecione o próximo passo:\n'
					 '------------------------------------------------------------------------')
			combo.pack_forget()
			
			botao1.configure(text='Finalizar Manobra', command=lambda: finaliza('Trocar D3'))
		else:
			telaInt.configure(
				text='------------------------------------------------------------------------\n'
					 'Seleção inválida!\n'
					 'Selecione o próximo passo:\n'
					 '------------------------------------------------------------------------')
			Disj3Passo6()


	def Disj3Passo5():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D3':
			newImage = PhotoImage(file='img/bar5/bar5D3g.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor D3 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Abrir S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Ligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo3())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo5()


	def Disj3Passo4():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S11' or 'Abrir S12':
			newImage = PhotoImage(file='img/bar5/bar5D3f.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
            
			if elem_sel == 'Abrir S11':
				telaInt.configure(text='------------------------------------------------------------------------\n'
                                       'Seccionaddora S11 aberta\n\n'
                                       'Selecione o próximo passo:\n'
                                       '------------------------------------------------------------------------')
			elif elem_sel == 'Abrir S12':
				telaInt.configure(text='------------------------------------------------------------------------\n'
                                       'Seccionaddora S12 aberta\n\n'
                                       'Selecione o próximo passo:\n'
                                       '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Fechar S11',
									'Fechar S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Abrir S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo6())
            
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo4()
	
    
	def Disj3Passo3():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S11':
			newImage = PhotoImage(file='img/bar5/bar5D3e1.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddora S11 aberta\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Fechar S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Abrir S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Ligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo4())
            
		elif elem_sel == 'Abrir S12':
			newImage = PhotoImage(file='img/bar5/bar5D3e2.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddora S12 aberta\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Fechar S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Abrir S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Ligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo4())
            
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo3()

			
	def Disj3Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S14':
			newImage = PhotoImage(file='img/bar5/bar5D3d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddora S14 fechada\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Abrir S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo5())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo2()

			
	def Disj3Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Ligar DT':
			newImage = PhotoImage(file='img/bar5/bar5D3c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor DT ligado\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Desligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo2())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			Disj3Passo1()

			
	def analiseD3():
		elem_sel = combo.get()

		if elem_sel == 'Fechar S9-S10':
			newImage = PhotoImage(file='img/bar5/bar5D3b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionaddoras S9 e S10 fechadas\n\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1',
									'Abrir S2',
									'Abrir S5',
									'Abrir S6',
									'Abrir S11',
									'Abrir S12',
									'Abrir S15',
									'Abrir S16',
									'Abrir S19',
									'Abrir S20',
									'Fechar S3',
									'Fechar S4',
									'Fechar S7',
									'Fechar S8',
									'Fechar S13',
									'Fechar S14',
									'Fechar S17',
									'Fechar S18',
									'Fechar S21',
									'Fechar S22',
									'Abrir S9-S10',
									'Ligar DT',
									'Desligar D1',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo1())
		else:
			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			analiseD3()

			
	def selectFalha():
		elem_sel = combo.get()
		elem_falha = elem_sel
		telaInt.configure(text='------------------------------------------------------------------------\n'
							   'Falha no ' + elem_falha + '\n\n'
							   'Selecione o próximo passo:\n'
							   '------------------------------------------------------------------------')
		combo.configure(values=['Abrir S1',
								'Abrir S2',
								'Abrir S5',
								'Abrir S6',
								'Abrir S11',
								'Abrir S12',
								'Abrir S15',
								'Abrir S16',
								'Abrir S19',
								'Abrir S20',
								'Fechar S3',
								'Fechar S4',
								'Fechar S7',
								'Fechar S8',
								'Fechar S13',
								'Fechar S14',
								'Fechar S17',
								'Fechar S18',
								'Fechar S21',
								'Fechar S22',
								'Fechar S9-S10',
								'Ligar DT',
								'Desligar D1',
								'Desligar D2',
								'Desligar D3',
								'Desligar D4',
								'Desligar D5',])
		combo.set('')
		botao1.configure(text='Próximo Passo')
		botao2.configure(text='Sair')

		if elem_sel == 'Disjuntor D3':
			newImage = PhotoImage(file='img/bar5/bar5D3a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			botao1.configure(command=lambda: analiseD3())

		elif elem_sel == 'Disjuntor D4':
			newImage = PhotoImage(file='img/bar5/bar5D4a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			botao1.configure(command=lambda: analiseD4())

		elif elem_sel == 'Disjuntor D5':
			newImage = PhotoImage(file='img/bar5/bar5D5a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			botao1.configure(command=lambda: analiseD5())

			
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
	image = PhotoImage(file='img/bar5/bar5.png')
	diagrama = Label(container1, image=image)
	diagrama.pack(expand=True, fill='both')


	# Criação Tela Interativa
	telaInt = Label(subcontainer1,
					text='------------------------------------------------------------------------\n'
						 'Barramento Duplo com Disjuntor a Quatro Chaves\n\n'
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
					   ]
	combo.pack(fill='x', padx=10, pady=10)


	# Criação Botões
	botao1 = Button(subcontainer3, text='Iniciar Manobra', font=('Times New Roman', '14'), command=lambda: selectFalha())
	botao2 = Button(subcontainer3, text='Sair', font=('Times New Roman', '14'), command=lambda: app.destroy())
	botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
	botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)


	app.mainloop()


inicia()