from tkinter import ttk
from tkinter import *


def inicia():
	app = Tk()
	app.title("Duplo Barramento Simples com Geração Auxiliar")
	#app.iconbitmap('img/ufsm-see.ico')


	def finaliza(elem_sel):
		if elem_sel == 'Trocar D2':
			newImage = PhotoImage(file='img/bar4/bar4D2e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Manobra em Disjuntor D2 finalizada!\n'
								   '--------------------------------------------------------------')

		elif elem_sel == 'Trocar D3':
			newImage = PhotoImage(file='img/bar4/bar4D3e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Manobra em Disjuntor D3 finalizada!\n'
								   '--------------------------------------------------------------')

        elif elem_sel == 'Trocar D4':
			newImage = PhotoImage(file='img/bar4/bar4D4e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Manobra em Disjuntor D4 finalizada!\n'
								   '--------------------------------------------------------------')

		elif elem_sel == 'Trocar D5':
			newImage = PhotoImage(file='img/bar4/bar4D5e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Manobra em Disjuntor D5 finalizada!\n'
								   '--------------------------------------------------------------')

		elif elem_sel == 'Trocar D6':
			newImage = PhotoImage(file='img/bar4/bar4D6e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Manobra em Disjuntor D6 finalizada!\n'
								   '--------------------------------------------------------------')
								   
		elif elem_sel == 'Trocar D7':
			newImage = PhotoImage(file='img/bar4/bar4D7e.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Manobra em Disjuntor D7 finalizada!\n'
								   '--------------------------------------------------------------')

	def Disj7Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D7':
			newImage = PhotoImage(file='img/bar4/bar4D7d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(
				text='--------------------------------------------------------------\n'
					 'Disjuntor D7 trocado\n\n'
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
			Disj7Passo2()

			
	def Disj7Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S15-S16':
			newImage = PhotoImage(file='img/bar4/bar4D7c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionadoras S15 e S16 abertas\n'
								   'Selecione o próximo passo:\n\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D7',
									'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Fechar S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Desligar D5',
                                    'Desligar D6',
                                    'Ligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj7Passo2())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			Disj7Passo1()

			
	def analiseD7():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D7':
			newImage = PhotoImage(file='img/bar4/bar4D7b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D7 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D7',
									'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Desligar D5',
                                    'Desligar D6',
                                    'Ligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj7Passo1())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			analiseD7()

			
	def Disj6Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D6':
			newImage = PhotoImage(file='img/bar4/bar4D6d.png')
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
			Disj6Passo2()

			
	def Disj6Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S13-S14':
			newImage = PhotoImage(file='img/bar4/bar4D6c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionadoras S13 e S14 abertas\n'
								   'Selecione o próximo passo:\n\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Fechar S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Desligar D5',
                                    'Ligar D6',
                                    'Desligar D7',])
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

		if elem_sel == 'Desligar D6':
			newImage = PhotoImage(file='img/bar4/bar4D6b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D6 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D6',
									'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Desligar D5',
                                    'Ligar D6',
                                    'Desligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj6Passo1())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			analiseD6()

			
	def Disj5Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D5':
			newImage = PhotoImage(file='img/bar4/bar4D5d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(
				text='--------------------------------------------------------------\n'
					 'Disjuntor D5 trocado\n\n'
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
			Disj5Passo2()

			
	def Disj5Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S11-S12':
			newImage = PhotoImage(file='img/bar4/bar4D5c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionadoras S11 e S12 abertas\n'
								   'Selecione o próximo passo:\n\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
                                    'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Fechar S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Ligar D5',
                                    'Desligar D6',
                                    'Desligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo2())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			Disj5Passo1()

			
	def analiseD5():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D5':
			newImage = PhotoImage(file='img/bar4/bar4D5b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D5 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
                                    'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Ligar D5',
                                    'Desligar D6',
                                    'Desligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj5Passo1())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			analiseD5()
			
			
	def Disj4Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D4':
			newImage = PhotoImage(file='img/bar4/bar4D4d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(
				text='--------------------------------------------------------------\n'
					 'Disjuntor D4 trocado\n\n'
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
			Disj4Passo2()

			
	def Disj4Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S7-S8':
			newImage = PhotoImage(file='img/bar4/bar4D4c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionadoras S7 e S8 abertas\n'
								   'Selecione o próximo passo:\n\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
                                    'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Fechar S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Ligar D4',
                                    'Desligar D5',
                                    'Desligar D6',
                                    'Desligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo2())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			Disj4Passo1()

			
	def analiseD4():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D4':
			newImage = PhotoImage(file='img/bar4/bar4D4b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D4 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
                                    'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Ligar D4',
                                    'Desligar D5',
                                    'Desligar D6',
                                    'Desligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj4Passo1())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			analiseD4()

			
	def Disj3Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D3':
			newImage = PhotoImage(file='img/bar4/bar4D3d.png')
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
			Disj3Passo2()

			
	def Disj3Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S5-S6':
			newImage = PhotoImage(file='img/bar4/bar4D3c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionadoras S5 e S6 abertas\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Fechar S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Desligar D5',
                                    'Desligar D6',
                                    'Desligar D7',])
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

		if elem_sel == 'Desligar D3':
			newImage = PhotoImage(file='img/bar4/bar4D3b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D3 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D2',
									'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Desligar D5',
                                    'Desligar D6',
                                    'Desligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj3Passo1())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			analiseD3()


	def Disj2Passo2():
		elem_sel = combo.get()

		if elem_sel == 'Trocar D2':
			newImage = PhotoImage(file='img/bar4/bar4D2d.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(
				text='--------------------------------------------------------------\n'
					 'Disjuntor D2 trocado\n\n'
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
			Disj2Passo2()

			
	def Disj2Passo1():
		elem_sel = combo.get()

		if elem_sel == 'Abrir S3-S4':
			newImage = PhotoImage(file='img/bar4/bar4D2c.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seccionadoras S3 e S4 abertas\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D2',
                                    'Abrir S1-S2',
                                    'Fechar S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Ligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Desligar D5',
                                    'Desligar D6',
                                    'Desligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj2Passo2())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			Disj2Passo1()

			
	def analiseD2():
		elem_sel = combo.get()

		if elem_sel == 'Desligar D2':
			newImage = PhotoImage(file='img/bar4/bar4D2b.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Disjuntor D2 desligado\n\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			combo.configure(values=['Trocar D2',
                                    'Abrir S1-S2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Abrir S11-S12',
                                    'Abrir S13-S14',
                                    'Abrir S15-S16',
                                    'Fechar S9-S10',
                                    'Ligar DG',
                                    'Desligar D1',
                                    'Ligar D2',
                                    'Desligar D3',
                                    'Desligar D4',
                                    'Desligar D5',
                                    'Desligar D6',
                                    'Desligar D7',])
			combo.set('')

			botao1.configure(command=lambda: Disj2Passo1())
		else:
			telaInt.configure(text='--------------------------------------------------------------\n'
								   'Seleção inválida!\n'
								   'Selecione o próximo passo:\n'
								   '--------------------------------------------------------------')
			analiseD2()

			
	def selectFalha():
		elem_sel = combo.get()
		elem_falha = elem_sel
		telaInt.configure(text='--------------------------------------------------------------\n'
							   'Falha no ' + elem_falha + '\n\n'
							   'Selecione o próximo passo:\n'
							   '--------------------------------------------------------------')
		combo.configure(values=['Abrir S1-S2',
								'Abrir S3-S4',
                                'Abrir S5-S6',
								'Abrir S7-S8',
								'Abrir S11-S12',
								'Abrir S13-S14',
								'Abrir S15-S16',
								'Fechar S9-S10',
								'Ligar DG',
								'Desligar D1',
								'Desligar D2',
								'Desligar D3',
								'Desligar D4',
								'Desligar D5',
								'Desligar D6',
								'Desligar D7',])
		combo.set('')
		botao1.configure(text='Próximo Passo')
		botao2.configure(text='Sair')

		if elem_sel == 'Disjuntor D2':
			newImage = PhotoImage(file='img/bar4/bar4D2a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			botao1.configure(command=lambda: analiseD2())

		elif elem_sel == 'Disjuntor D3':
			newImage = PhotoImage(file='img/bar4/bar4D3a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			botao1.configure(command=lambda: analiseD3())
            
        elif elem_sel == 'Disjuntor D4':
			newImage = PhotoImage(file='img/bar4/bar4D4a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			botao1.configure(command=lambda: analiseD4())

		elif elem_sel == 'Disjuntor D5':
			newImage = PhotoImage(file='img/bar4/bar4D5a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			botao1.configure(command=lambda: analiseD5())

		elif elem_sel == 'Disjuntor D6':
			newImage = PhotoImage(file='img/bar4/bar4D6a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

			botao1.configure(command=lambda: analiseD6())
		
		elif elem_sel == 'Disjuntor D7':
			newImage = PhotoImage(file='img/bar4/bar4D7a.png')
			diagrama.configure(image=newImage)
			diagrama.image = newImage

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
	image = PhotoImage(file='img/bar4/bar4.png')
	diagrama = Label(container1, image=image)
	diagrama.pack(expand=True, fill='both')


	# Criação Tela Interativa
	telaInt = Label(subcontainer1,
					text='--------------------------------------------------------------\n'
						 'Duplo Barramento Simples com Geração Auxiliar\n\n'
						 'Defina o elemento com falha!\n'
						 '--------------------------------------------------------------',
					font='times 14 bold',
					justify='center',
					bg="#dde")
	telaInt.pack(fill='both', expand='yes', padx=10, pady=10)


	# Criação Combobox
	ComboVar = StringVar()
	combo = ttk.Combobox(subcontainer2, textvariable=ComboVar, font=('Times New Roman', '14'), state='readonly')
	combo['values'] = ['Disjuntor D2',
                       'Disjuntor D3',
					   'Disjuntor D4',
					   'Disjuntor D5',
					   'Disjuntor D6',
					   'Disjuntor D7',
					   ]
	combo.pack(fill='x', padx=10, pady=10)


	# Criação Botões
	botao1 = Button(subcontainer3, text='Iniciar Manobra', font=('Times New Roman', '14'), command=lambda: selectFalha())
	botao2 = Button(subcontainer3, text='Sair', font=('Times New Roman', '14'), command=lambda: app.destroy())
	botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
	botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)


	app.mainloop()


inicia()