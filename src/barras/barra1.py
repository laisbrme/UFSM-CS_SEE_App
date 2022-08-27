from tkinter import ttk
from tkinter import *



def inicio():
    app = Tk()
    app.title("Barramento Simples")
    #app.iconbitmap('img/ufsm-see.ico')
    
    
    def finaliza(elem_sel):
        #botao1.configure(text='Reiniciar', command=lambda: NONE)
        botao1.pack_forget()
        
        if elem_sel == 'Trocar D2':
            newImage = PhotoImage(file='img/bar1/bar1D2e.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D2 finalizada!\n'
                                   '------------------------------------------------------------------------')


        elif elem_sel == 'Trocar D3':
            newImage = PhotoImage(file='img/bar1/bar1D3e.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D3 finalizada!\n'
                                   '------------------------------------------------------------------------')


        elif elem_sel == 'Trocar D4':
            newImage = PhotoImage(file='img/bar1/bar1D4e.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D4 finalizada!\n'
                                   '------------------------------------------------------------------------')

    def Disj2Passo2():
        elem_sel = combo.get()

        if elem_sel == 'Trocar D2':
            newImage = PhotoImage(file='img/bar1/bar1D2d.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Disjuntor D2 trocado\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            combo.pack_forget()
            botao1.configure(text='Finalizar Manobra', command=lambda: finaliza('Trocar D2'))
        else:
            telaInt.configure(
                text='------------------------------------------------------------------------\n'
                     'Seleção inválida!\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            Disj2Passo2()

    def Disj2Passo1():
        elem_sel = combo.get()

        if elem_sel == 'Abrir S3-S4':
            newImage = PhotoImage(file='img/bar1/bar1D2c.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S3 e S4 abertas\n\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D2',
                                    'Fechar S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Ligar D2',
                                    'Desligar D3',
                                    'Desligar D4',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo2())
        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj2Passo1()
                                   
    def analiseD2():
        elem_sel = combo.get()

        if elem_sel == 'Desligar D2':
            newImage = PhotoImage(file='img/bar1/bar1D2b.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D2 desligado\n\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D2',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Ligar D2',
                                    'Desligar D3',
                                    'Desligar D4',])
            combo.set('')

            botao1.configure(command=lambda: Disj2Passo1())
        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            analiseD2()

    def Disj3Passo2():
        elem_sel = combo.get()

        if elem_sel == 'Trocar D3':
            newImage = PhotoImage(file='img/bar1/bar1D3d.png')
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
                     'Seleção inválida!\n\n'
                     'Selecione o próximo passo:\n'
                     '------------------------------------------------------------------------')
            Disj3Passo2()
            
    def Disj3Passo1():
        elem_sel = combo.get()

        if elem_sel == 'Abrir S5-S6':
            newImage = PhotoImage(file='img/bar1/bar1D3c.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S5 e S6 abertas\n\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D3',
                                    'Abrir S3-S4',
                                    'Fechar S5-S6',
                                    'Abrir S7-S8',
                                    'Desligar D2',
                                    'Ligar D3',
                                    'Desligar D4',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo2())
        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            Disj3Passo1()
            
    def analiseD3():
        elem_sel = combo.get()

        if elem_sel == 'Desligar D3':
            newImage = PhotoImage(file='img/bar1/bar1D3b.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D3 desligado\n\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D3',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Desligar D2',
                                    'Ligar D3',
                                    'Desligar D4',])
            combo.set('')

            botao1.configure(command=lambda: Disj3Passo1())
        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            analiseD3()

    def Disj4Passo2():
        elem_sel = combo.get()

        if elem_sel == 'Trocar D4':
            newImage = PhotoImage(file='img/bar1/bar1D4d.png')
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
            Disj4Passo2()
            
    def Disj4Passo1():
        elem_sel = combo.get()

        if elem_sel == 'Abrir S7-S8':
            newImage = PhotoImage(file='img/bar1/bar1D4c.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seccionadoras S7 e S8 abertas\n\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D4',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Fechar S7-S8',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Ligar D4',])
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

        if elem_sel == 'Desligar D4':
            newImage = PhotoImage(file='img/bar1/bar1D4b.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Disjuntor D4 desligado\n\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            combo.configure(values=['Trocar D4',
                                    'Abrir S3-S4',
                                    'Abrir S5-S6',
                                    'Abrir S7-S8',
                                    'Desligar D2',
                                    'Desligar D3',
                                    'Ligar D4',])
            combo.set('')

            botao1.configure(command=lambda: Disj4Passo1())
        else:
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Seleção inválida!\n'
                                   'Selecione o próximo passo:\n'
                                   '------------------------------------------------------------------------')
            analiseD4()

    def selectFalha():
        elem_sel = combo.get()
        elem_falha = elem_sel
        telaInt.configure(text='------------------------------------------------------------------------\n'
                               'Falha no ' + elem_falha + '\n\n'
                               'Selecione o próximo passo:\n'
                               '------------------------------------------------------------------------')
        combo.configure(values=['Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',])
        combo.set('')
        botao1.configure(text='Próximo Passo')
        botao2.configure(text='Sair')

        if elem_sel == 'Disjuntor D2':
            newImage = PhotoImage(file='img/bar1/bar1D2a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            botao1.configure(command=lambda: analiseD2())

        elif elem_sel == 'Disjuntor D3':
            newImage = PhotoImage(file='img/bar1/bar1D3a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            botao1.configure(command=lambda: analiseD3())

        elif elem_sel == 'Disjuntor D4':
            newImage = PhotoImage(file='img/bar1/bar1D4a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            botao1.configure(command=lambda: analiseD4())



    

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
    image = PhotoImage(file='img/bar1/bar1.png')
    diagrama = Label(container1, image=image)
    diagrama.pack(expand=True, fill='both')


    # Criação Tela Interativa
    telaInt = Label(subcontainer1,
                    text='------------------------------------------------------------------------\n'
                         'Barramento Simples\n\n'
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
                       ]
    combo.pack(fill='x', padx=10, pady=10)


    # Criação Botões
    botao1 = Button(subcontainer3, text='Iniciar Manobra', font=('Times New Roman', '14'), command=lambda: selectFalha())
    botao2 = Button(subcontainer3, text='Sair', font=('Times New Roman', '14'), command=lambda: app.destroy())
    botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
    botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)


    app.mainloop()
    
inicio()