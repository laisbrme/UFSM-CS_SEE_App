def Disj2Passo2():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S7-S8':
        newImage = PhotoImage(file='img/bar8/bar8D2d.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seccionadoras S7 e S8 fechadas\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2',
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

        botao1.configure(command=lambda: Disj2Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo2()


def Disj2Passo3():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D4':
        newImage = PhotoImage(file='img/bar8/bar8D2e.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D4 ligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2',
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

        botao1.configure(command=lambda: Disj2Passo4())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo3()


def Disj2Passo4():
    elem_sel = combo.get()

    if elem_sel == 'Desligar D3':
        newImage = PhotoImage(file='img/bar8/bar8D2f.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D3 desligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2',
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

        botao1.configure(command=lambda: Disj2Passo5())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo4()


def Disj2Passo5():
    elem_sel = combo.get()

    if elem_sel == 'Abrir S5-S6':
        newImage = PhotoImage(file='img/bar8/bar8D2g.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seccionadoras S5 e S6 abertas\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2',
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

        botao1.configure(command=lambda: Disj2Passo6())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo5()


def Disj2Passo6():
    elem_sel = combo.get()

    if elem_sel == 'Trocar D2':
        newImage = PhotoImage(file='img/bar8/bar8D2h.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D3 trocado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.pack_forget()
        botao1.configure(text='Finalizar',
                         command=lambda: finaliza(elem_sel))
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo6()