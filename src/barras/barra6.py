from tkinter import ttk
from tkinter import *

def inicio():
    app = Tk()
    app.title("Barramento Duplo com Disjuntor Duplo")
    app.iconbitmap('img/ufsm-see.ico')


    def finaliza(elem_sel):
        if elem_sel == 'Trocar D1':
            newImage = PhotoImage(file='img/bar6/bar6D1h.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D1 finalizada!\n'
                                   '------------------------------------------------------------------------')


        elif elem_sel == 'Trocar D3':
            newImage = PhotoImage(file='img/bar6/bar6D3i.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D3 finalizada!\n'
                                   '------------------------------------------------------------------------')


        elif elem_sel == 'Trocar D5':
            newImage = PhotoImage(file='img/bar6/bar6D5i.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D5 finalizada!\n'
                                   '------------------------------------------------------------------------')


        elif elem_sel == 'Trocar D7':
            newImage = PhotoImage(file='img/bar6/bar6D7i.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage
            telaInt.configure(text='------------------------------------------------------------------------\n'
                                   'Manobra em Disjuntor D7 finalizada!\n'
                                   '------------------------------------------------------------------------')


    def selectFalha():
        elem_sel = combo.get()
        elem_falha = elem_sel
        telaInt.configure(text='------------------------------------------------------------------------\n'
                               'Falha no ' + elem_falha + '\n\n'
                               'Selecione o próximo passo:\n'
                               '------------------------------------------------------------------------')
        combo.configure(values=['Abrir S1-S2',
                                'Abrir S5-S6',
                                'Abrir S9-S10',
                                'Abrir S13-S14',
                                'Fechar S3-S4',
                                'Fechar S7-S8',
                                'Fechar S11-S12',
                                'Fechar S15-S16',
                                'Desligar D1',
                                'Desligar D3',
                                'Desligar D5',
                                'Desligar D7',
                                'Ligar D2',
                                'Ligar D4',
                                'Ligar D6',
                                'Ligar D8', ])
        combo.set('')
        botao1.configure(text='Próximo Passo')
        botao2.configure(text='Sair')

        if elem_sel == 'Disjuntor D1':
            newImage = PhotoImage(file='img/bar6/bar6D1a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            def analiseD1():
                elem_sel = combo.get()

                if elem_sel == 'Desligar D1':
                    newImage = PhotoImage(file='img/bar6/bar6D1b.png')
                    diagrama.configure(image=newImage)
                    diagrama.image = newImage

                    telaInt.configure(text='------------------------------------------------------------------------\n'
                                           'Disjuntor D1 desligado\n\n'
                                           'Selecione o próximo passo:\n'
                                           '------------------------------------------------------------------------')
                    combo.configure(values=['Trocar D1',
                                            'Abrir S1-S2',
                                            'Abrir S5-S6',
                                            'Abrir S9-S10',
                                            'Abrir S13-S14',
                                            'Abrir S3-S4',
                                            'Fechar S7-S8',
                                            'Fechar S11-S12',
                                            'Fechar S15-S16',
                                            'Ligar D1',
                                            'Desligar D3',
                                            'Desligar D5',
                                            'Desligar D7',
                                            'Ligar D2',
                                            'Ligar D4',
                                            'Ligar D6',
                                            'Ligar D8', ])
                    combo.set('')

                    def Disj1Passo1():
                        elem_sel = combo.get()

                        if elem_sel == 'Abrir S1-S2':
                            newImage = PhotoImage(file='img/bar6/bar6D1c.png')
                            diagrama.configure(image=newImage)
                            diagrama.image = newImage

                            telaInt.configure(text='------------------------------------------------------------------------\n'
                                                   'Seccionadoras S1 e S2 abertas\n\n'
                                                   'Selecione o próximo passo:\n'
                                                   '------------------------------------------------------------------------')
                            combo.configure(values=['Trocar D1',
                                                    'Fechar S1-S2',
                                                    'Abrir S5-S6',
                                                    'Abrir S9-S10',
                                                    'Abrir S13-S14',
                                                    'Abrir S3-S4',
                                                    'Fechar S7-S8',
                                                    'Fechar S11-S12',
                                                    'Fechar S15-S16',
                                                    'Ligar D1',
                                                    'Desligar D3',
                                                    'Desligar D5',
                                                    'Desligar D7',
                                                    'Ligar D2',
                                                    'Ligar D4',
                                                    'Ligar D6',
                                                    'Ligar D8', ])
                            combo.set('')

                            def Disj1Passo2():
                                elem_sel = combo.get()

                                if elem_sel == 'Trocar D1':
                                    newImage = PhotoImage(file='img/bar6/bar6D1d.png')
                                    diagrama.configure(image=newImage)
                                    diagrama.image = newImage

                                    telaInt.configure(
                                        text='------------------------------------------------------------------------\n'
                                             'Disjuntor D1 trocado\n\n'
                                             'Selecione o próximo passo:\n'
                                             '------------------------------------------------------------------------')
                                    combo.configure(values=['Trocar D1',
                                                            'Fechar S1-S2',
                                                            'Abrir S5-S6',
                                                            'Abrir S9-S10',
                                                            'Abrir S13-S14',
                                                            'Abrir S3-S4',
                                                            'Fechar S7-S8',
                                                            'Fechar S11-S12',
                                                            'Fechar S15-S16',
                                                            'Ligar D1',
                                                            'Desligar D3',
                                                            'Desligar D5',
                                                            'Desligar D7',
                                                            'Ligar D2',
                                                            'Ligar D4',
                                                            'Ligar D6',
                                                            'Ligar D8', ])
                                    combo.set('')

                                    def Disj1Passo3():
                                        elem_sel = combo.get()

                                        if elem_sel == 'Fechar S1-S2':
                                            newImage = PhotoImage(file='img/bar6/bar6D1e.png')
                                            diagrama.configure(image=newImage)
                                            diagrama.image = newImage

                                            telaInt.configure(
                                                text='------------------------------------------------------------------------\n'
                                                     'Seccionadoras S1 e S2 fechadas\n\n'
                                                     'Selecione o próximo passo:\n'
                                                     '------------------------------------------------------------------------')
                                            combo.configure(values=['Trocar D1',
                                                                    'Abrir S1-S2',
                                                                    'Abrir S5-S6',
                                                                    'Abrir S9-S10',
                                                                    'Abrir S13-S14',
                                                                    'Abrir S3-S4',
                                                                    'Fechar S7-S8',
                                                                    'Fechar S11-S12',
                                                                    'Fechar S15-S16',
                                                                    'Ligar D1',
                                                                    'Desligar D3',
                                                                    'Desligar D5',
                                                                    'Desligar D7',
                                                                    'Ligar D2',
                                                                    'Ligar D4',
                                                                    'Ligar D6',
                                                                    'Ligar D8', ])
                                            combo.set('')

                                            def Disj1Passo4():
                                                elem_sel = combo.get()

                                                if elem_sel == 'Ligar D1':
                                                    newImage = PhotoImage(file='img/bar6/bar6D1f.png')
                                                    diagrama.configure(image=newImage)
                                                    diagrama.image = newImage

                                                    telaInt.configure(
                                                        text='------------------------------------------------------------------------\n'
                                                             'Disjuntor D1 ligado\n\n'
                                                             'Selecione o próximo passo:\n'
                                                             '------------------------------------------------------------------------')
                                                    combo.pack_forget()
                                                    botao1.configure(text='Finalizar',
                                                                     command=lambda: finaliza('Trocar D1'))

                                                else:
                                                    telaInt.configure(
                                                        text='------------------------------------------------------------------------\n'
                                                             'Seleção inválida!\n'
                                                             'Selecione o próximo passo:\n'
                                                             '------------------------------------------------------------------------')
                                                    Disj1Passo4()

                                            botao1.configure(command=lambda: Disj1Passo4())
                                        else:
                                            telaInt.configure(
                                                text='------------------------------------------------------------------------\n'
                                                     'Seleção inválida!\n'
                                                     'Selecione o próximo passo:\n'
                                                     '------------------------------------------------------------------------')
                                            Disj1Passo3()

                                    botao1.configure(command=lambda: Disj1Passo3())
                                else:
                                    telaInt.configure(
                                        text='------------------------------------------------------------------------\n'
                                             'Seleção inválida!\n'
                                             'Selecione o próximo passo:\n'
                                             '------------------------------------------------------------------------')
                                    Disj1Passo2()

                            botao1.configure(command=lambda: Disj1Passo2())
                        else:
                            telaInt.configure(text='------------------------------------------------------------------------\n'
                                                   'Seleção inválida!\n'
                                                   'Selecione o próximo passo:\n'
                                                   '------------------------------------------------------------------------')
                            Disj1Passo1()

                    botao1.configure(command=lambda: Disj1Passo1())
                else:
                    telaInt.configure(text='------------------------------------------------------------------------\n'
                                           'Seleção inválida!\n'
                                           'Selecione o próximo passo:\n'
                                           '------------------------------------------------------------------------')
                    analiseD1()

            botao1.configure(command=lambda: analiseD1())

        elif elem_sel == 'Disjuntor D3':
            newImage = PhotoImage(file='img/bar6/bar6D3a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            def analiseD3():
                elem_sel = combo.get()

                if elem_sel == 'Fechar S3-S4':
                    newImage = PhotoImage(file='img/bar6/bar6D3b.png')
                    diagrama.configure(image=newImage)
                    diagrama.image = newImage

                    telaInt.configure(text='------------------------------------------------------------------------\n'
                                           'Seccionadoras S3 e S4 fechadas\n\n'
                                           'Selecione o próximo passo:\n'
                                           '------------------------------------------------------------------------')
                    combo.configure(values=['Trocar D3',
                                            'Abrir S1-S2',
                                            'Abrir S5-S6',
                                            'Abrir S9-S10',
                                            'Abrir S13-S14',
                                            'Abrir S3-S4',
                                            'Fechar S7-S8',
                                            'Fechar S11-S12',
                                            'Fechar S15-S16',
                                            'Desligar D1',
                                            'Desligar D3',
                                            'Desligar D5',
                                            'Desligar D7',
                                            'Ligar D2',
                                            'Ligar D4',
                                            'Ligar D6',
                                            'Ligar D8', ])
                    combo.set('')

                    def Disj3Passo1():
                        elem_sel = combo.get()

                        if elem_sel == 'Ligar D2':
                            newImage = PhotoImage(file='img/bar6/bar6D3c.png')
                            diagrama.configure(image=newImage)
                            diagrama.image = newImage
                            telaInt.configure(text='------------------------------------------------------------------------\n'
                                                   'Disjuntor de transferência D2 ligado\n\n'
                                                   'Selecione o próximo passo:\n'
                                                   '------------------------------------------------------------------------')
                            combo.configure(values=['Trocar D3',
                                                    'Abrir S1-S2',
                                                    'Abrir S5-S6',
                                                    'Abrir S9-S10',
                                                    'Abrir S13-S14',
                                                    'Abrir S3-S4',
                                                    'Fechar S7-S8',
                                                    'Fechar S11-S12',
                                                    'Fechar S15-S16',
                                                    'Desligar D1',
                                                    'Desligar D3',
                                                    'Desligar D5',
                                                    'Desligar D7',
                                                    'Desligar D2',
                                                    'Ligar D4',
                                                    'Ligar D6',
                                                    'Ligar D8', ])
                            combo.set('')

                            def Disj3Passo2():
                                elem_sel = combo.get()

                                if elem_sel == 'Fechar S7-S8':
                                    newImage = PhotoImage(file='img/bar6/bar6D3d.png')
                                    diagrama.configure(image=newImage)
                                    diagrama.image = newImage
                                    telaInt.configure(
                                        text='------------------------------------------------------------------------\n'
                                             'Seccionadoras S7 e S8 fechadas\n\n'
                                             'Selecione o próximo passo:\n'
                                             '------------------------------------------------------------------------')
                                    combo.configure(values=['Trocar D3',
                                                            'Abrir S1-S2',
                                                            'Abrir S5-S6',
                                                            'Abrir S9-S10',
                                                            'Abrir S13-S14',
                                                            'Abrir S3-S4',
                                                            'Abrir S7-S8',
                                                            'Fechar S11-S12',
                                                            'Fechar S15-S16',
                                                            'Desligar D1',
                                                            'Desligar D3',
                                                            'Desligar D5',
                                                            'Desligar D7',
                                                            'Desligar D2',
                                                            'Ligar D4',
                                                            'Ligar D6',
                                                            'Ligar D8', ])
                                    combo.set('')

                                    def Disj3Passo3():
                                        elem_sel = combo.get()

                                        if elem_sel == 'Ligar D4':
                                            newImage = PhotoImage(file='img/bar6/bar6D3e.png')
                                            diagrama.configure(image=newImage)
                                            diagrama.image = newImage
                                            telaInt.configure(
                                                text='------------------------------------------------------------------------\n'
                                                     'Disjuntor D4 ligado\n\n'
                                                     'Selecione o próximo passo:\n'
                                                     '------------------------------------------------------------------------')
                                            combo.configure(values=['Trocar D3',
                                                                    'Abrir S1-S2',
                                                                    'Abrir S5-S6',
                                                                    'Abrir S9-S10',
                                                                    'Abrir S13-S14',
                                                                    'Abrir S3-S4',
                                                                    'Abrir S7-S8',
                                                                    'Fechar S11-S12',
                                                                    'Fechar S15-S16',
                                                                    'Desligar D1',
                                                                    'Desligar D3',
                                                                    'Desligar D5',
                                                                    'Desligar D7',
                                                                    'Desligar D2',
                                                                    'Desligar D4',
                                                                    'Ligar D6',
                                                                    'Ligar D8', ])
                                            combo.set('')

                                            def Disj3Passo4():
                                                elem_sel = combo.get()

                                                if elem_sel == 'Desligar D3':
                                                    newImage = PhotoImage(file='img/bar6/bar6D3f.png')
                                                    diagrama.configure(image=newImage)
                                                    diagrama.image = newImage
                                                    telaInt.configure(
                                                        text='------------------------------------------------------------------------\n'
                                                             'Disjuntor D3 desligado\n\n'
                                                             'Selecione o próximo passo:\n'
                                                             '------------------------------------------------------------------------')
                                                    combo.configure(values=['Trocar D3',
                                                                            'Abrir S1-S2',
                                                                            'Abrir S5-S6',
                                                                            'Abrir S9-S10',
                                                                            'Abrir S13-S14',
                                                                            'Abrir S3-S4',
                                                                            'Abrir S7-S8',
                                                                            'Fechar S11-S12',
                                                                            'Fechar S15-S16',
                                                                            'Desligar D1',
                                                                            'Ligar D3',
                                                                            'Desligar D5',
                                                                            'Desligar D7',
                                                                            'Desligar D2',
                                                                            'Desligar D4',
                                                                            'Ligar D6',
                                                                            'Ligar D8', ])
                                                    combo.set('')

                                                    def Disj3Passo5():
                                                        elem_sel = combo.get()

                                                        if elem_sel == 'Abrir S5-S6':
                                                            newImage = PhotoImage(file='img/bar6/bar6D3g.png')
                                                            diagrama.configure(image=newImage)
                                                            diagrama.image = newImage
                                                            telaInt.configure(
                                                                text='------------------------------------------------------------------------\n'
                                                                     'Seccionadoras S5 e S6 abertas\n\n'
                                                                     'Selecione o próximo passo:\n'
                                                                     '------------------------------------------------------------------------')
                                                            combo.configure(values=['Trocar D3',
                                                                                    'Abrir S1-S2',
                                                                                    'Fechar S5-S6',
                                                                                    'Abrir S9-S10',
                                                                                    'Abrir S13-S14',
                                                                                    'Abrir S3-S4',
                                                                                    'Abrir S7-S8',
                                                                                    'Fechar S11-S12',
                                                                                    'Fechar S15-S16',
                                                                                    'Desligar D1',
                                                                                    'Ligar D3',
                                                                                    'Desligar D5',
                                                                                    'Desligar D7',
                                                                                    'Desligar D2',
                                                                                    'Desligar D4',
                                                                                    'Ligar D6',
                                                                                    'Ligar D8', ])
                                                            combo.set('')

                                                            def Disj3Passo6():
                                                                elem_sel = combo.get()

                                                                if elem_sel == 'Trocar D3':
                                                                    newImage = PhotoImage(file='img/bar6/bar6D3h.png')
                                                                    diagrama.configure(image=newImage)
                                                                    diagrama.image = newImage
                                                                    telaInt.configure(
                                                                        text='------------------------------------------------------------------------\n'
                                                                             'Disjuntor D3 trocado\n\n'
                                                                             'Selecione o próximo passo:\n'
                                                                             '------------------------------------------------------------------------')
                                                                    combo.pack_forget()
                                                                    botao1.configure(text='Finalizar',
                                                                                     command=lambda: finaliza(elem_sel))
                                                                else:
                                                                    telaInt.configure(
                                                                        text='------------------------------------------------------------------------\n'
                                                                             'Seleção inválida!\n'
                                                                             'Selecione o próximo passo:\n'
                                                                             '------------------------------------------------------------------------')
                                                                    Disj3Passo6()

                                                            botao1.configure(command=lambda: Disj3Passo6())
                                                        else:
                                                            telaInt.configure(
                                                                text='------------------------------------------------------------------------\n'
                                                                     'Seleção inválida!\n'
                                                                     'Selecione o próximo passo:\n'
                                                                     '------------------------------------------------------------------------')
                                                            Disj3Passo5()

                                                    botao1.configure(command=lambda: Disj3Passo5())
                                                else:
                                                    telaInt.configure(
                                                        text='------------------------------------------------------------------------\n'
                                                             'Seleção inválida!\n'
                                                             'Selecione o próximo passo:\n'
                                                             '------------------------------------------------------------------------')
                                                    Disj3Passo4()

                                            botao1.configure(command=lambda: Disj3Passo4())
                                        else:
                                            telaInt.configure(
                                                text='------------------------------------------------------------------------\n'
                                                     'Seleção inválida!\n'
                                                     'Selecione o próximo passo:\n'
                                                     '------------------------------------------------------------------------')
                                            Disj3Passo3()

                                    botao1.configure(command=lambda: Disj3Passo3())
                                else:
                                    telaInt.configure(
                                        text='------------------------------------------------------------------------\n'
                                             'Seleção inválida!\n'
                                             'Selecione o próximo passo:\n'
                                             '------------------------------------------------------------------------')
                                    Disj3Passo2()

                            botao1.configure(command=lambda: Disj3Passo2())
                        else:
                            telaInt.configure(text='------------------------------------------------------------------------\n'
                                                   'Seleção inválida!\n'
                                                   'Selecione o próximo passo:\n'
                                                   '------------------------------------------------------------------------')
                            Disj3Passo1()

                    botao1.configure(command=lambda: Disj3Passo1())
                else:
                    telaInt.configure(text='------------------------------------------------------------------------\n'
                                           'Seleção inválida!\n'
                                           'Selecione o próximo passo:\n'
                                           '------------------------------------------------------------------------')
                    analiseD3()

            botao1.configure(text='Próximo Passo', command=lambda: analiseD3())

        elif elem_sel == 'Disjuntor D5':
            newImage = PhotoImage(file='img/bar6/bar6D5a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            def analiseD5():
                elem_sel = combo.get()

                if elem_sel == 'Fechar S3-S4':
                    newImage = PhotoImage(file='img/bar6/bar6D5b.png')
                    diagrama.configure(image=newImage)
                    diagrama.image = newImage

                    telaInt.configure(text='------------------------------------------------------------------------\n'
                                           'Seccionadoras S3 e S4 fechadas\n\n'
                                           'Selecione o próximo passo:\n'
                                           '------------------------------------------------------------------------')
                    combo.configure(values=['Trocar D5',
                                            'Abrir S1-S2',
                                            'Abrir S5-S6',
                                            'Abrir S9-S10',
                                            'Abrir S13-S14',
                                            'Abrir S3-S4',
                                            'Fechar S7-S8',
                                            'Fechar S11-S12',
                                            'Fechar S15-S16',
                                            'Desligar D1',
                                            'Desligar D3',
                                            'Desligar D5',
                                            'Desligar D7',
                                            'Ligar D2',
                                            'Ligar D4',
                                            'Ligar D6',
                                            'Ligar D8', ])
                    combo.set('')

                    def Disj5Passo1():
                        elem_sel = combo.get()

                        if elem_sel == 'Ligar D2':
                            newImage = PhotoImage(file='img/bar6/bar6D5c.png')
                            diagrama.configure(image=newImage)
                            diagrama.image = newImage
                            telaInt.configure(text='------------------------------------------------------------------------\n'
                                                   'Disjuntor de transferência D2 ligado\n\n'
                                                   'Selecione o próximo passo:\n'
                                                   '------------------------------------------------------------------------')
                            combo.configure(values=['Trocar D5',
                                                    'Abrir S1-S2',
                                                    'Abrir S5-S6',
                                                    'Abrir S9-S10',
                                                    'Abrir S13-S14',
                                                    'Abrir S3-S4',
                                                    'Fechar S7-S8',
                                                    'Fechar S11-S12',
                                                    'Fechar S15-S16',
                                                    'Desligar D1',
                                                    'Desligar D3',
                                                    'Desligar D5',
                                                    'Desligar D7',
                                                    'Desligar D2',
                                                    'Ligar D4',
                                                    'Ligar D6',
                                                    'Ligar D8', ])
                            combo.set('')

                            def Disj5Passo2():
                                elem_sel = combo.get()

                                if elem_sel == 'Fechar S11-S12':
                                    newImage = PhotoImage(file='img/bar6/bar6D5d.png')
                                    diagrama.configure(image=newImage)
                                    diagrama.image = newImage
                                    telaInt.configure(
                                        text='------------------------------------------------------------------------\n'
                                             'Seccionadoras S11 e S12 fechadas\n\n'
                                             'Selecione o próximo passo:\n'
                                             '------------------------------------------------------------------------')
                                    combo.configure(values=['Trocar D5',
                                                            'Abrir S1-S2',
                                                            'Abrir S5-S6',
                                                            'Abrir S9-S10',
                                                            'Abrir S13-S14',
                                                            'Abrir S3-S4',
                                                            'Fechar S7-S8',
                                                            'Abrir S11-S12',
                                                            'Fechar S15-S16',
                                                            'Desligar D1',
                                                            'Desligar D3',
                                                            'Desligar D5',
                                                            'Desligar D7',
                                                            'Desligar D2',
                                                            'Ligar D4',
                                                            'Ligar D6',
                                                            'Ligar D8', ])
                                    combo.set('')

                                    def Disj5Passo3():
                                        elem_sel = combo.get()

                                        if elem_sel == 'Ligar D6':
                                            newImage = PhotoImage(file='img/bar6/bar6D5e.png')
                                            diagrama.configure(image=newImage)
                                            diagrama.image = newImage
                                            telaInt.configure(
                                                text='------------------------------------------------------------------------\n'
                                                     'Disjuntor D6 ligado\n\n'
                                                     'Selecione o próximo passo:\n'
                                                     '------------------------------------------------------------------------')
                                            combo.configure(values=['Trocar D5',
                                                                    'Abrir S1-S2',
                                                                    'Abrir S5-S6',
                                                                    'Abrir S9-S10',
                                                                    'Abrir S13-S14',
                                                                    'Abrir S3-S4',
                                                                    'Fechar S7-S8',
                                                                    'Abrir S11-S12',
                                                                    'Fechar S15-S16',
                                                                    'Desligar D1',
                                                                    'Desligar D3',
                                                                    'Desligar D5',
                                                                    'Desligar D7',
                                                                    'Desligar D2',
                                                                    'Ligar D4',
                                                                    'Desligar D6',
                                                                    'Ligar D8', ])
                                            combo.set('')

                                            def Disj5Passo4():
                                                elem_sel = combo.get()

                                                if elem_sel == 'Desligar D5':
                                                    newImage = PhotoImage(file='img/bar6/bar6D5f.png')
                                                    diagrama.configure(image=newImage)
                                                    diagrama.image = newImage
                                                    telaInt.configure(
                                                        text='------------------------------------------------------------------------\n'
                                                             'Disjuntor D5 desligado\n\n'
                                                             'Selecione o próximo passo:\n'
                                                             '------------------------------------------------------------------------')
                                                    combo.configure(values=['Trocar D5',
                                                                            'Abrir S1-S2',
                                                                            'Abrir S5-S6',
                                                                            'Abrir S9-S10',
                                                                            'Abrir S13-S14',
                                                                            'Abrir S3-S4',
                                                                            'Fechar S7-S8',
                                                                            'Abrir S11-S12',
                                                                            'Fechar S15-S16',
                                                                            'Desligar D1',
                                                                            'Desligar D3',
                                                                            'Ligar D5',
                                                                            'Desligar D7',
                                                                            'Desligar D2',
                                                                            'Ligar D4',
                                                                            'Desligar D6',
                                                                            'Ligar D8', ])
                                                    combo.set('')

                                                    def Disj5Passo5():
                                                        elem_sel = combo.get()

                                                        if elem_sel == 'Abrir S9-S10':
                                                            newImage = PhotoImage(file='img/bar6/bar6D5g.png')
                                                            diagrama.configure(image=newImage)
                                                            diagrama.image = newImage
                                                            telaInt.configure(
                                                                text='------------------------------------------------------------------------\n'
                                                                     'Seccionadoras S9 e S10 abertas\n\n'
                                                                     'Selecione o próximo passo:\n'
                                                                     '------------------------------------------------------------------------')
                                                            combo.configure(values=['Trocar D5',
                                                                                    'Abrir S1-S2',
                                                                                    'Abrir S5-S6',
                                                                                    'Fechar S9-S10',
                                                                                    'Abrir S13-S14',
                                                                                    'Abrir S3-S4',
                                                                                    'Fechar S7-S8',
                                                                                    'Abrir S11-S12',
                                                                                    'Fechar S15-S16',
                                                                                    'Desligar D1',
                                                                                    'Desligar D3',
                                                                                    'Ligar D5',
                                                                                    'Desligar D7',
                                                                                    'Desligar D2',
                                                                                    'Ligar D4',
                                                                                    'Desligar D6',
                                                                                    'Ligar D8', ])
                                                            combo.set('')

                                                            def Disj5Passo6():
                                                                elem_sel = combo.get()

                                                                if elem_sel == 'Trocar D5':
                                                                    newImage = PhotoImage(file='img/bar6/bar6D5h.png')
                                                                    diagrama.configure(image=newImage)
                                                                    diagrama.image = newImage
                                                                    telaInt.configure(
                                                                        text='------------------------------------------------------------------------\n'
                                                                             'Disjuntor D5 trocado\n\n'
                                                                             'Selecione o próximo passo:\n'
                                                                             '------------------------------------------------------------------------')
                                                                    combo.pack_forget()
                                                                    botao1.configure(text='Finalizar',
                                                                                     command=lambda: finaliza(elem_sel))
                                                                else:
                                                                    telaInt.configure(
                                                                        text='------------------------------------------------------------------------\n'
                                                                             'Seleção inválida!\n'
                                                                             'Selecione o próximo passo:\n'
                                                                             '------------------------------------------------------------------------')
                                                                    Disj5Passo6()

                                                            botao1.configure(command=lambda: Disj5Passo6())
                                                        else:
                                                            telaInt.configure(
                                                                text='------------------------------------------------------------------------\n'
                                                                     'Seleção inválida!\n'
                                                                     'Selecione o próximo passo:\n'
                                                                     '------------------------------------------------------------------------')
                                                            Disj5Passo5()

                                                    botao1.configure(command=lambda: Disj5Passo5())
                                                else:
                                                    telaInt.configure(
                                                        text='------------------------------------------------------------------------\n'
                                                             'Seleção inválida!\n'
                                                             'Selecione o próximo passo:\n'
                                                             '------------------------------------------------------------------------')
                                                    Disj5Passo4()

                                            botao1.configure(command=lambda: Disj5Passo4())
                                        else:
                                            telaInt.configure(
                                                text='------------------------------------------------------------------------\n'
                                                     'Seleção inválida!\n'
                                                     'Selecione o próximo passo:\n'
                                                     '------------------------------------------------------------------------')
                                            Disj5Passo3()

                                    botao1.configure(command=lambda: Disj5Passo3())
                                else:
                                    telaInt.configure(
                                        text='------------------------------------------------------------------------\n'
                                             'Seleção inválida!\n'
                                             'Selecione o próximo passo:\n'
                                             '------------------------------------------------------------------------')
                                    Disj5Passo2()

                            botao1.configure(command=lambda: Disj5Passo2())
                        else:
                            telaInt.configure(text='------------------------------------------------------------------------\n'
                                                   'Seleção inválida!\n'
                                                   'Selecione o próximo passo:\n'
                                                   '------------------------------------------------------------------------')
                            Disj5Passo1()

                    botao1.configure(command=lambda: Disj5Passo1())
                else:
                    telaInt.configure(text='------------------------------------------------------------------------\n'
                                           'Seleção inválida!\n'
                                           'Selecione o próximo passo:\n'
                                           '------------------------------------------------------------------------')
                    analiseD5()

            botao1.configure(command=lambda: analiseD5())

        elif elem_sel == 'Disjuntor D7':
            newImage = PhotoImage(file='img/bar6/bar6D7a.png')
            diagrama.configure(image=newImage)
            diagrama.image = newImage

            def analiseD7():
                elem_sel = combo.get()

                if elem_sel == 'Fechar S3-S4':
                    newImage = PhotoImage(file='img/bar6/bar6D7b.png')
                    diagrama.configure(image=newImage)
                    diagrama.image = newImage

                    telaInt.configure(text='------------------------------------------------------------------------\n'
                                           'Seccionadoras S3 e S4 fechadas\n\n'
                                           'Selecione o próximo passo:\n'
                                           '------------------------------------------------------------------------')
                    combo.configure(values=['Trocar D7',
                                            'Abrir S1-S2',
                                            'Abrir S5-S6',
                                            'Abrir S9-S10',
                                            'Abrir S13-S14',
                                            'Abrir S3-S4',
                                            'Fechar S7-S8',
                                            'Fechar S11-S12',
                                            'Fechar S15-S16',
                                            'Desligar D1',
                                            'Desligar D3',
                                            'Desligar D5',
                                            'Desligar D7',
                                            'Ligar D2',
                                            'Ligar D4',
                                            'Ligar D6',
                                            'Ligar D8', ])
                    combo.set('')

                    def Disj7Passo1():
                        elem_sel = combo.get()

                        if elem_sel == 'Ligar D2':
                            newImage = PhotoImage(file='img/bar6/bar6D7c.png')
                            diagrama.configure(image=newImage)
                            diagrama.image = newImage
                            telaInt.configure(text='------------------------------------------------------------------------\n'
                                                   'Disjuntor de transferência D2 ligado\n\n'
                                                   'Selecione o próximo passo:\n'
                                                   '------------------------------------------------------------------------')
                            combo.configure(values=['Trocar D7',
                                                    'Abrir S1-S2',
                                                    'Abrir S5-S6',
                                                    'Abrir S9-S10',
                                                    'Abrir S13-S14',
                                                    'Abrir S3-S4',
                                                    'Fechar S7-S8',
                                                    'Fechar S11-S12',
                                                    'Fechar S15-S16',
                                                    'Desligar D1',
                                                    'Desligar D3',
                                                    'Desligar D5',
                                                    'Desligar D7',
                                                    'Desligar D2',
                                                    'Ligar D4',
                                                    'Ligar D6',
                                                    'Ligar D8', ])
                            combo.set('')

                            def Disj7Passo2():
                                elem_sel = combo.get()

                                if elem_sel == 'Fechar S15-S16':
                                    newImage = PhotoImage(file='img/bar6/bar6D7d.png')
                                    diagrama.configure(image=newImage)
                                    diagrama.image = newImage
                                    telaInt.configure(
                                        text='------------------------------------------------------------------------\n'
                                             'Seccionadoras S15 e S16 fechadas\n\n'
                                             'Selecione o próximo passo:\n'
                                             '------------------------------------------------------------------------')
                                    combo.configure(values=['Trocar D7',
                                                            'Abrir S1-S2',
                                                            'Abrir S5-S6',
                                                            'Abrir S9-S10',
                                                            'Abrir S13-S14',
                                                            'Abrir S3-S4',
                                                            'Fechar S7-S8',
                                                            'Abrir S11-S12',
                                                            'Abrir S15-S16',
                                                            'Desligar D1',
                                                            'Desligar D3',
                                                            'Desligar D5',
                                                            'Desligar D7',
                                                            'Desligar D2',
                                                            'Ligar D4',
                                                            'Ligar D6',
                                                            'Ligar D8', ])
                                    combo.set('')

                                    def Disj7Passo3():
                                        elem_sel = combo.get()

                                        if elem_sel == 'Ligar D8':
                                            newImage = PhotoImage(file='img/bar6/bar6D7e.png')
                                            diagrama.configure(image=newImage)
                                            diagrama.image = newImage
                                            telaInt.configure(
                                                text='------------------------------------------------------------------------\n'
                                                     'Disjuntor D8 ligado\n\n'
                                                     'Selecione o próximo passo:\n'
                                                     '------------------------------------------------------------------------')
                                            combo.configure(values=['Trocar D7',
                                                                    'Abrir S1-S2',
                                                                    'Abrir S5-S6',
                                                                    'Abrir S9-S10',
                                                                    'Abrir S13-S14',
                                                                    'Abrir S3-S4',
                                                                    'Fechar S7-S8',
                                                                    'Abrir S11-S12',
                                                                    'Abrir S15-S16',
                                                                    'Desligar D1',
                                                                    'Desligar D3',
                                                                    'Desligar D5',
                                                                    'Desligar D7',
                                                                    'Desligar D2',
                                                                    'Ligar D4',
                                                                    'Ligar D6',
                                                                    'Desligar D8', ])
                                            combo.set('')

                                            def Disj7Passo4():
                                                elem_sel = combo.get()

                                                if elem_sel == 'Desligar D7':
                                                    newImage = PhotoImage(file='img/bar6/bar6D7f.png')
                                                    diagrama.configure(image=newImage)
                                                    diagrama.image = newImage
                                                    telaInt.configure(
                                                        text='------------------------------------------------------------------------\n'
                                                             'Disjuntor D7 desligado\n\n'
                                                             'Selecione o próximo passo:\n'
                                                             '------------------------------------------------------------------------')
                                                    combo.configure(values=['Trocar D7',
                                                                            'Abrir S1-S2',
                                                                            'Abrir S5-S6',
                                                                            'Abrir S9-S10',
                                                                            'Abrir S13-S14',
                                                                            'Abrir S3-S4',
                                                                            'Fechar S7-S8',
                                                                            'Abrir S11-S12',
                                                                            'Abrir S15-S16',
                                                                            'Desligar D1',
                                                                            'Desligar D3',
                                                                            'Desligar D5',
                                                                            'Ligar D7',
                                                                            'Desligar D2',
                                                                            'Ligar D4',
                                                                            'Ligar D6',
                                                                            'Desligar D8', ])
                                                    combo.set('')

                                                    def Disj7Passo5():
                                                        elem_sel = combo.get()

                                                        if elem_sel == 'Abrir S13-S14':
                                                            newImage = PhotoImage(file='img/bar6/bar6D7g.png')
                                                            diagrama.configure(image=newImage)
                                                            diagrama.image = newImage
                                                            telaInt.configure(
                                                                text='------------------------------------------------------------------------\n'
                                                                     'Seccionadoras S13 e S14 abertas\n\n'
                                                                     'Selecione o próximo passo:\n'
                                                                     '------------------------------------------------------------------------')
                                                            combo.configure(values=['Trocar D7',
                                                                                    'Abrir S1-S2',
                                                                                    'Abrir S5-S6',
                                                                                    'Abrir S9-S10',
                                                                                    'Fechar S13-S14',
                                                                                    'Abrir S3-S4',
                                                                                    'Fechar S7-S8',
                                                                                    'Abrir S11-S12',
                                                                                    'Abrir S15-S16',
                                                                                    'Desligar D1',
                                                                                    'Desligar D3',
                                                                                    'Desligar D5',
                                                                                    'Ligar D7',
                                                                                    'Desligar D2',
                                                                                    'Ligar D4',
                                                                                    'Ligar D6',
                                                                                    'Desligar D8', ])
                                                            combo.set('')

                                                            def Disj7Passo6():
                                                                elem_sel = combo.get()

                                                                if elem_sel == 'Trocar D7':
                                                                    newImage = PhotoImage(file='img/bar6/bar6D7h.png')
                                                                    diagrama.configure(image=newImage)
                                                                    diagrama.image = newImage
                                                                    telaInt.configure(
                                                                        text='------------------------------------------------------------------------\n'
                                                                             'Disjuntor D7 trocado\n\n'
                                                                             'Selecione o próximo passo:\n'
                                                                             '------------------------------------------------------------------------')
                                                                    combo.pack_forget()
                                                                    botao1.configure(text='Finalizar',
                                                                                     command=lambda: finaliza(elem_sel))
                                                                else:
                                                                    telaInt.configure(
                                                                        text='------------------------------------------------------------------------\n'
                                                                             'Seleção inválida!\n'
                                                                             'Selecione o próximo passo:\n'
                                                                             '------------------------------------------------------------------------')
                                                                    Disj7Passo6()

                                                            botao1.configure(command=lambda: Disj7Passo6())
                                                        else:
                                                            telaInt.configure(
                                                                text='------------------------------------------------------------------------\n'
                                                                     'Seleção inválida!\n'
                                                                     'Selecione o próximo passo:\n'
                                                                     '------------------------------------------------------------------------')
                                                            Disj7Passo5()

                                                    botao1.configure(command=lambda: Disj7Passo5())
                                                else:
                                                    telaInt.configure(
                                                        text='------------------------------------------------------------------------\n'
                                                             'Seleção inválida!\n'
                                                             'Selecione o próximo passo:\n'
                                                             '------------------------------------------------------------------------')
                                                    Disj7Passo4()

                                            botao1.configure(command=lambda: Disj7Passo4())
                                        else:
                                            telaInt.configure(
                                                text='------------------------------------------------------------------------\n'
                                                     'Seleção inválida!\n'
                                                     'Selecione o próximo passo:\n'
                                                     '------------------------------------------------------------------------')
                                            Disj7Passo3()

                                    botao1.configure(command=lambda: Disj7Passo3())
                                else:
                                    telaInt.configure(
                                        text='------------------------------------------------------------------------\n'
                                             'Seleção inválida!\n'
                                             'Selecione o próximo passo:\n'
                                             '------------------------------------------------------------------------')
                                    Disj7Passo2()

                            botao1.configure(command=lambda: Disj7Passo2())
                        else:
                            telaInt.configure(text='------------------------------------------------------------------------\n'
                                                   'Seleção inválida!\n'
                                                   'Selecione o próximo passo:\n'
                                                   '------------------------------------------------------------------------')
                            Disj7Passo1()

                    botao1.configure(command=lambda: Disj7Passo1())
                else:
                    telaInt.configure(text='------------------------------------------------------------------------\n'
                                           'Seleção inválida!\n'
                                           'Selecione o próximo passo:\n'
                                           '------------------------------------------------------------------------')
                    analiseD7()

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
    image = PhotoImage(file='img/bar6/bar6.png')
    diagrama = Label(container1, image=image)
    diagrama.pack(expand=True, fill='both')


    # Criação Tela Interativa
    telaInt = Label(subcontainer1,
                    text='------------------------------------------------------------------------\n'
                         'Barramento Duplo com Disjuntor Duplo\n\n'
                         'Defina o elemento com falha!\n'
                         '------------------------------------------------------------------------',
                    font='times 14 bold',
                    justify='center',
                    bg="#dde")
    telaInt.pack(fill='both', expand='yes', padx=10, pady=10)


    # Criação Combobox
    ComboVar = StringVar()
    combo = ttk.Combobox(subcontainer2, textvariable=ComboVar, font=('Times New Roman', '14'), state='readonly')
    combo['values'] = ['Disjuntor D1',
                       'Disjuntor D3',
                       'Disjuntor D5',
                       'Disjuntor D7',
                       ]
    combo.pack(fill='x', padx=10, pady=10)
    

    # Criação Botões
    botao1 = Button(subcontainer3, text='Iniciar Manobra', font=('Times New Roman', '14'), command=lambda: selectFalha())
    botao2 = Button(subcontainer3, text='Sair', font=('Times New Roman', '14'), command=lambda: app.destroy())
    botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
    botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)


    app.mainloop()


inicio()