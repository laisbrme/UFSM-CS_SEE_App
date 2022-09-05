from tkinter import ttk
from tkinter import *

def inicio():
    app = Tk()
    app.title("Barramento Duplo com Disjuntor e Meio")
    # app.iconbitmap('img/ufsm-see.ico')


    def finaliza(elem_sel):
        if elem_sel == 'Trocar D2':
            newImage = PhotoImage(file='img/bar7/bar7D2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D2 finalizada!\n'
                                   '------------------------------------------------------------------------')


        elif elem_sel == 'Trocar D3':
            newImage = PhotoImage(file='img/bar7/bar7D3.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D3 finalizada!\n'
                                   '------------------------------------------------------------------------')


        elif elem_sel == 'Trocar D4':
            newImage = PhotoImage(file='img/bar7/bar7D4.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D4 finalizada!\n'
                                   '------------------------------------------------------------------------')


        elif elem_sel == 'Trocar D5':
            newImage = PhotoImage(file='img/bar7/bar7D5.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D5 finalizada!\n'
                                   '------------------------------------------------------------------------')


    def Disj5Passo6():
        elem_sel = combo.get()

        if elem_sel == 'Trocar D5':
            newImage = PhotoImage(file='img/bar7/bar7D5h.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Disjuntor D5 trocado\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            combo.pack_forget()
            botao1.configure(text='Finalizar', command=lambda: finaliza(elem_sel))
        else:
            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Seleção inválida!\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            Disj5Passo6()

			
	def	Disj5Passo5():
		elem_sel = combo.get()

        if elem_sel == 'Abrir S9-S10':
			newImage = PhotoImage(file='img/bar7/bar7D5g.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionadoras S9 e S10 abertas\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Fechar S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Ligar D5',
									'Desligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj5Passo6())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj5Passo5()
			
			
	def	Disj5Passo4():
		elem_sel = combo.get()

        if elem_sel == 'Desligar D5':
			newImage = PhotoImage(file='img/bar7/bar7D5f.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor D5 desligado\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Ligar D5',
									'Desligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj5Passo5())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj5Passo4()
			
			
	def	Disj5Passo3():
		elem_sel = combo.get()

        if elem_sel == 'Ligar D6' or 'Ligar D7':
			newImage = PhotoImage(file='img/bar7/bar7D5e.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
			if elem_sel == 'Ligar D6' 
				telaInt.configure(text='------------------------------------------------------------------------\n'
									   'Disjuntor D6 ligado\n'
									   'Selecione o próximo passo:\n'
									   '------------------------------------------------------------------------')
			elif elem_sel == 'Ligar D7':
				telaInt.configure(text='------------------------------------------------------------------------\n'
									   'Disjuntor D7 ligado\n'
									   'Selecione o próximo passo:\n'
									   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D5',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
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

        if elem_sel == 'Fechar S11-S12':
            newImage = PhotoImage(file='img/bar7/bar7D5d1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S11 e S12 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D5',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj5Passo3())

        elif elem_sel == 'Fechar S13-S14':
            newImage = PhotoImage(file='img/bar7/bar7D5d2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S13 e S14 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D5',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj5Passo3())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj5Passo2()

			
    def Disj5Passo1a():
        elem_sel = combo.get()

		if elem_sel == 'Ligar D6':
            newImage = PhotoImage(file='img/bar7/bar7D5c1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D6 ligado\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D5',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Fechar S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj5Passo2())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj5Passo1a()
			
			
    def Disj5Passo1b():
        elem_sel = combo.get()

		if elem_sel == 'Ligar D7':
            newImage = PhotoImage(file='img/bar7/bar7D5c2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D7 ligado\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D5',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj5Passo2())
        
        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj5Passo1b()


    def analiseD5():
        elem_sel = combo.get()

        if elem_sel == 'Fechar S11-S12':
            newImage = PhotoImage(file='img/bar7/bar7D5b1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S11 e S12 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D5',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Fechar S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj5Passo1a())

        elif elem_sel == 'Fechar S13-S14':
            newImage = PhotoImage(file='img/bar7/bar7D5b2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S13 e S14 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D5',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj5Passo1b())

        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            analiseD5()
								   
								   
    def Disj4Passo6():
        elem_sel = combo.get()

        if elem_sel == 'Trocar D4':
            newImage = PhotoImage(file='img/bar7/bar7D4h.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Disjuntor D4 trocado\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            combo.pack_forget()
            botao1.configure(text='Finalizar', command=lambda: finaliza(elem_sel))
        else:
            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Seleção inválida!\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            Disj4Passo6()

			
	def	Disj4Passo5():
		elem_sel = combo.get()

        if elem_sel == 'Abrir S7-S8':
			newImage = PhotoImage(file='img/bar7/bar7D4g.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionadoras S7 e S8 abertas\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Fechar S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Ligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj4Passo6())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj4Passo5()
			
			
	def	Disj4Passo4():
		elem_sel = combo.get()

        if elem_sel == 'Desligar D4':
			newImage = PhotoImage(file='img/bar7/bar7D4f.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor D4 desligado\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Ligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj4Passo5())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj4Passo4()
			
			
	def	Disj4Passo3():
		elem_sel = combo.get()

        if elem_sel == 'Ligar D6' or 'Ligar D7':
			newImage = PhotoImage(file='img/bar7/bar7D4e.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
			if elem_sel == 'Ligar D6' 
				telaInt.configure(text='------------------------------------------------------------------------\n'
									   'Disjuntor D6 ligado\n'
									   'Selecione o próximo passo:\n'
									   '------------------------------------------------------------------------')
			elif elem_sel == 'Ligar D7':
				telaInt.configure(text='------------------------------------------------------------------------\n'
									   'Disjuntor D7 ligado\n'
									   'Selecione o próximo passo:\n'
									   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D4',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
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

        if elem_sel == 'Fechar S11-S12':
            newImage = PhotoImage(file='img/bar7/bar7D4d1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S11 e S12 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D4',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj4Passo3())

        elif elem_sel == 'Fechar S13-S14':
            newImage = PhotoImage(file='img/bar7/bar7D4d2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S13 e S14 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D4',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj4Passo3())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj4Passo2()

			
    def Disj4Passo1a():
        elem_sel = combo.get()

		if elem_sel == 'Ligar D6':
            newImage = PhotoImage(file='img/bar7/bar7D4c1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D6 ligado\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D4',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Fechar S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj4Passo2())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj4Passo1a()
			
			
    def Disj4Passo1b():
        elem_sel = combo.get()

		if elem_sel == 'Ligar D7':
            newImage = PhotoImage(file='img/bar7/bar7D4c2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D7 ligado\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D4',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj4Passo2())
        
        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj4Passo1b()


    def analiseD4():
        elem_sel = combo.get()

        if elem_sel == 'Fechar S11-S12':
            newImage = PhotoImage(file='img/bar7/bar7D4b1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S11 e S12 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D4',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Fechar S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj4Passo1a())

        elif elem_sel == 'Fechar S13-S14':
            newImage = PhotoImage(file='img/bar7/bar7D4b2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S13 e S14 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D4',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj4Passo1b())

        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            analiseD4()
								   
								   
    def Disj3Passo6():
        elem_sel = combo.get()

        if elem_sel == 'Trocar D3':
            newImage = PhotoImage(file='img/bar7/bar7D3h.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Disjuntor D3 trocado\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            combo.pack_forget()
            botao1.configure(text='Finalizar', command=lambda: finaliza(elem_sel))
        else:
            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Seleção inválida!\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            Disj3Passo6()

			
	def	Disj3Passo5():
		elem_sel = combo.get()

        if elem_sel == 'Abrir S5-S6':
			newImage = PhotoImage(file='img/bar7/bar7D3g.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionadoras S5 e S6 abertas\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S3-S4',
									'Fechar S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Ligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo6())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj3Passo5()
			
			
	def	Disj3Passo4():
		elem_sel = combo.get()

        if elem_sel == 'Desligar D3':
			newImage = PhotoImage(file='img/bar7/bar7D3f.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor D3 desligado\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Ligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo5())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj3Passo4()
			
			
	def	Disj3Passo3():
		elem_sel = combo.get()

        if elem_sel == 'Ligar D6' or 'Ligar D7':
			newImage = PhotoImage(file='img/bar7/bar7D3e.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
			if elem_sel == 'Ligar D6' 
				telaInt.configure(text='------------------------------------------------------------------------\n'
									   'Disjuntor D6 ligado\n'
									   'Selecione o próximo passo:\n'
									   '------------------------------------------------------------------------')
			elif elem_sel == 'Ligar D7':
				telaInt.configure(text='------------------------------------------------------------------------\n'
									   'Disjuntor D7 ligado\n'
									   'Selecione o próximo passo:\n'
									   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D3',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
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

        if elem_sel == 'Fechar S11-S12':
            newImage = PhotoImage(file='img/bar7/bar7D3d1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S11 e S12 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D3',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo3())

        elif elem_sel == 'Fechar S13-S14':
            newImage = PhotoImage(file='img/bar7/bar7D3d2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S13 e S14 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D3',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo3())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj3Passo2()

			
    def Disj3Passo1a():
        elem_sel = combo.get()

		if elem_sel == 'Ligar D6':
            newImage = PhotoImage(file='img/bar7/bar7D3c1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D6 ligado\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D3',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Fechar S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo2())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj3Passo1a()
			
			
    def Disj3Passo1b():
        elem_sel = combo.get()

		if elem_sel == 'Ligar D7':
            newImage = PhotoImage(file='img/bar7/bar7D3c2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D7 ligado\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D3',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo2())
        
        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj3Passo1b()


    def analiseD3():
        elem_sel = combo.get()

        if elem_sel == 'Fechar S11-S12':
            newImage = PhotoImage(file='img/bar7/bar7D3b1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S11 e S12 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D3',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Fechar S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo1a())

        elif elem_sel == 'Fechar S13-S14':
            newImage = PhotoImage(file='img/bar7/bar7D3b2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S13 e S14 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D3',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo1b())

        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            analiseD3()


    def Disj2Passo6():
        elem_sel = combo.get()

        if elem_sel == 'Trocar D2':
            newImage = PhotoImage(file='img/bar7/bar7D2h.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Disjuntor D2 trocado\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            combo.pack_forget()
            botao1.configure(text='Finalizar', command=lambda: finaliza(elem_sel))
        else:
            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Seleção inválida!\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            Disj2Passo6()

			
	def	Disj3Passo5():
		elem_sel = combo.get()

        if elem_sel == 'Abrir S3-S4':
			newImage = PhotoImage(file='img/bar7/bar7D2g.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Seccionadoras S3 e S4 abertas\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D2',
									'Fechar S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Ligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo6())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj2Passo5()
			
			
	def	Disj3Passo4():
		elem_sel = combo.get()

        if elem_sel == 'Desligar D2':
			newImage = PhotoImage(file='img/bar7/bar7D2f.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

			telaInt.configure(text='------------------------------------------------------------------------\n'
								   'Disjuntor D2 desligado\n'
								   'Selecione o próximo passo:\n'
								   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D2',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Ligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo5())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj2Passo4()
			
			
	def	Disj3Passo3():
		elem_sel = combo.get()

        if elem_sel == 'Ligar D6' or 'Ligar D7':
			newImage = PhotoImage(file='img/bar7/bar7D2e.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
			if elem_sel == 'Ligar D6' 
				telaInt.configure(text='------------------------------------------------------------------------\n'
									   'Disjuntor D6 ligado\n'
									   'Selecione o próximo passo:\n'
									   '------------------------------------------------------------------------')
			elif elem_sel == 'Ligar D7':
				telaInt.configure(text='------------------------------------------------------------------------\n'
									   'Disjuntor D7 ligado\n'
									   'Selecione o próximo passo:\n'
									   '------------------------------------------------------------------------')
			combo.configure(values=['Trocar D2',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo4())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj2Passo3()
		
		
    def Disj2Passo2():
        elem_sel = combo.get()

        if elem_sel == 'Fechar S11-S12':
            newImage = PhotoImage(file='img/bar7/bar7D2d1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S11 e S12 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D2',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo3())

        elif elem_sel == 'Fechar S13-S14':
            newImage = PhotoImage(file='img/bar7/bar7D2d2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S13 e S14 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D2',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo3())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj2Passo2()

			
    def Disj2Passo1a():
        elem_sel = combo.get()

		if elem_sel == 'Ligar D6':
            newImage = PhotoImage(file='img/bar7/bar7D2c1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D6 ligado\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D2',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Fechar S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Desligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo2())
			
		else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj2Passo1a()
			
			
    def Disj2Passo1b():
        elem_sel = combo.get()

		if elem_sel == 'Ligar D7':
            newImage = PhotoImage(file='img/bar7/bar7D2c2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D7 ligado\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D2',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Desligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo2())
        
        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj2Passo1b()


    def analiseD2():
        elem_sel = combo.get()

        if elem_sel == 'Fechar S11-S12':
            newImage = PhotoImage(file='img/bar7/bar7D2b1.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S11 e S12 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D2',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Abrir S11-S12',
									'Fechar S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo1a())

        elif elem_sel == 'Fechar S13-S14':
            newImage = PhotoImage(file='img/bar7/bar7D2b2.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S13 e S14 fechadas\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D2',
									'Abrir S3-S4',
									'Abrir S5-S6',
									'Abrir S7-S8',
									'Abrir S9-S10',
									'Fechar S11-S12',
									'Abrir S13-S14',
									'Desligar D2',
									'Desligar D3',
									'Desligar D4',
									'Desligar D5',
									'Ligar D6',
									'Ligar D7',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo1b())

        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            analiseD2()


    def selectFalha():
        elem_sel = combo.get()
        elem_falha = elem_sel
        telaInt.configure(text='------------------------------------------------------------------------\n'
                               'Falha no ' + elem_falha + '\n'
                               'Selecione o próximo passo:\n'
                               '------------------------------------------------------------------------')
        combo.configure(values=['Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Fechar S11-S12',
                                'Fechar S13-S14',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Ligar D6',
                                'Ligar D7',])
        combo.set('')
        botao1.configure(text='Próximo Passo')
        botao2.configure(text='Sair')

        if elem_sel == 'Disjuntor D2':
            newImage = PhotoImage(file='img/bar7/bar7D2a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            botao1.configure(command=lambda: analiseD2())

        elif elem_sel == 'Disjuntor D3':
            newImage = PhotoImage(file='img/bar7/bar7D3a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            botao1.configure(command=lambda: analiseD3())

        elif elem_sel == 'Disjuntor D4':
            newImage = PhotoImage(file='img/bar7/bar7D4a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            botao1.configure(command=lambda: analiseD4())

        elif elem_sel == 'Disjuntor D5':
            newImage = PhotoImage(file='img/bar7/bar7D5a.png')
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
    image = PhotoImage(file='img/bar7/bar7.png')
    diagrama = Label(container1, image=image)
    diagrama.pack(expand=True, fill='both')


    # Criação Tela Interativa
    telaInt = Label(subcontainer1,
                    text='------------------------------------------------------------------------\n'
                         'Barramento Duplo com Disjuntor e Meio\n\n'
                         'Defina o elemento com falha!\n'
                         '------------------------------------------------------------------------',
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
                       'Disjuntor D5', ]
    combo.pack(fill='x', padx=10, pady=10)


    # Criação Botões
    botao1 = Button(subcontainer3, text='Iniciar Manobra', font=('Times New Roman', '14'), command=lambda: selectFalha())
    botao2 = Button(subcontainer3, text='Sair', font=('Times New Roman', '14'), command=lambda: app.destroy())
    botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
    botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)

    app.mainloop()


inicio()