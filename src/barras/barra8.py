from tkinter import ttk
from tkinter import *


app = Tk()
app.title("Barramento Duplo com Disjuntor e Um Terço")
# app.iconbitmap('img/ufsm-see.ico')


def finaliza(elem_sel):
    if elem_sel == 'Trocar D2':
        newImage = PhotoImage(file='img/bar8/bar8D2i.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D2 finalizada!\n'
                               '--------------------------------------------------------------')


    elif elem_sel == 'Trocar D3':
        newImage = PhotoImage(file='img/bar8/bar8D3i.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D3 finalizada!\n'
                               '--------------------------------------------------------------')


    elif elem_sel == 'Trocar D4':
        newImage = PhotoImage(file='img/bar8/bar8D4i.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D4 finalizada!\n'
                               '--------------------------------------------------------------')

    elif elem_sel == 'Trocar D5':
        newImage = PhotoImage(file='img/bar8/bar8D5i.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D5 finalizada!\n'
                               '--------------------------------------------------------------')


    elif elem_sel == 'Trocar D6':
        newImage = PhotoImage(file='img/bar8/bar8D6i.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D6 finalizada!\n'
                               '--------------------------------------------------------------')

    elif elem_sel == 'Trocar D7':
        newImage = PhotoImage(file='img/bar8/bar8D7i.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Manobra em Disjuntor D7 finalizada!\n'
                               '--------------------------------------------------------------')


def Disj7Passo6():
    elem_sel = combo.get()

    if elem_sel == 'Trocar D7':
        newImage = PhotoImage(file='img/bar8/bar8D7h.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D7 trocado\n'
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
        Disj7Passo6()


def Disj7Passo5():
    elem_sel = combo.get()

    if elem_sel == 'Abrir S13-S14':
        newImage = PhotoImage(file='img/bar8/bar8D7g.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seccionadoras S13 e S14 abertas\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D7'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Fechar S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Ligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj7Passo6())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj7Passo5()


def Disj7Passo4():
    elem_sel = combo.get()

    if elem_sel == 'Desligar D7':
        newImage = PhotoImage(file='img/bar8/bar8D7f.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D6 desligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D7'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Ligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj7Passo5())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj7Passo4()


def Disj7Passo3():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8' or elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D7e.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 elem_sel + ' ligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D7'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj7Passo4())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj7Passo3()


def Disj7Passo2a():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D7d2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S17 e S18 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D7'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj7Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj7Passo2a()


def Disj7Passo2b():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D7d1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S15 e S16 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D7'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9'])
        combo.set('')

        botao1.configure(command=lambda: Disj7Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj7Passo2b()

		
def Disj7Passo1a():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8':
        newImage = PhotoImage(file='img/bar8/bar8D7c2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D8 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D7'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9', ])
        combo.set('')

        botao1.configure(command=lambda: Disj7Passo2a())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj7Passo1a()


def Disj7Passo1b():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D7c1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D9 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D7'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9' ])
        combo.set('')

        botao1.configure(command=lambda: Disj7Passo2())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj7Passo1b()


def analiseD7():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D7b2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S15 e S16 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D7'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj7Passo1a())

    elif elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D7b1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S17 e S18 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D7'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj7Passo1b())

    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        analiseD7()


def Disj6Passo6():
    elem_sel = combo.get()

    if elem_sel == 'Trocar D6':
        newImage = PhotoImage(file='img/bar8/bar8D6h.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D6 trocado\n'
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
        Disj6Passo6()


def Disj6Passo5():
    elem_sel = combo.get()

    if elem_sel == 'Abrir S11-S12':
        newImage = PhotoImage(file='img/bar8/bar8D6g.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seccionadoras S11 e S12 abertas\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D6'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Fechar S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Ligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj6Passo6())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj6Passo5()


def Disj6Passo4():
    elem_sel = combo.get()

    if elem_sel == 'Desligar D6':
        newImage = PhotoImage(file='img/bar8/bar8D6f.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D6 desligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D6'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Ligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj6Passo5())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj6Passo4()


def Disj6Passo3():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8' or elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D6e.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 elem_sel + ' ligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D6'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj6Passo4())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj6Passo3()


def Disj6Passo2a():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D6d2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S17 e S18 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D6'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj6Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj6Passo2a()


def Disj6Passo2b():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D6d1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S15 e S16 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D6'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9'])
        combo.set('')

        botao1.configure(command=lambda: Disj6Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj6Passo2b()

		
def Disj6Passo1a():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8':
        newImage = PhotoImage(file='img/bar8/bar8D6c2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D8 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D6'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9', ])
        combo.set('')

        botao1.configure(command=lambda: Disj6Passo2a())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj6Passo1a()


def Disj6Passo1b():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D6c1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D9 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D6'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9' ])
        combo.set('')

        botao1.configure(command=lambda: Disj6Passo2())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj6Passo1b()


def analiseD6():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D6b2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S15 e S16 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D6'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj6Passo1a())

    elif elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D6b1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S17 e S18 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D6'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj6Passo1b())

    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        analiseD6()


def Disj5Passo6():
    elem_sel = combo.get()

    if elem_sel == 'Trocar D5':
        newImage = PhotoImage(file='img/bar8/bar8D5h.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D5 trocado\n'
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
        Disj5Passo6()


def Disj5Passo5():
    elem_sel = combo.get()

    if elem_sel == 'Abrir S9-S10':
        newImage = PhotoImage(file='img/bar8/bar8D5g.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seccionadoras S9 e S10 abertas\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D5'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Fechar S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Ligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj5Passo6())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj5Passo5()


def Disj5Passo4():
    elem_sel = combo.get()

    if elem_sel == 'Desligar D5':
        newImage = PhotoImage(file='img/bar8/bar8D5f.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D5 desligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D5'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Ligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj5Passo5())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj5Passo4()


def Disj5Passo3():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8' or elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D5e.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 elem_sel + ' ligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D5'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj5Passo4())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj5Passo3()


def Disj5Passo2a():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D5d2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S17 e S18 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D5'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj5Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj5Passo2a()


def Disj5Passo2b():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D5d1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S15 e S16 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D5'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9'])
        combo.set('')

        botao1.configure(command=lambda: Disj5Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj5Passo2b()

		
def Disj5Passo1a():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8':
        newImage = PhotoImage(file='img/bar8/bar8D5c2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D8 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D5'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9', ])
        combo.set('')

        botao1.configure(command=lambda: Disj5Passo2a())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj5Passo1a()


def Disj5Passo1b():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D5c1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D9 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D5'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9' ])
        combo.set('')

        botao1.configure(command=lambda: Disj5Passo2())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj5Passo1b()


def analiseD5():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D5b2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S15 e S16 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D5'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj5Passo1a())

    elif elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D5b1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S17 e S18 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D5'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj5Passo1b())

    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        analiseD5()


def Disj4Passo6():
    elem_sel = combo.get()

    if elem_sel == 'Trocar D4':
        newImage = PhotoImage(file='img/bar8/bar8D4h.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D4 trocado\n'
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
        Disj4Passo6()


def Disj4Passo5():
    elem_sel = combo.get()

    if elem_sel == 'Abrir S7-S8':
        newImage = PhotoImage(file='img/bar8/bar8D4g.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seccionadoras S7 e S8 abertas\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D4'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Fechar S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Ligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj4Passo6())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj4Passo5()


def Disj4Passo4():
    elem_sel = combo.get()

    if elem_sel == 'Desligar D4':
        newImage = PhotoImage(file='img/bar8/bar8D4f.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D4 desligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D4'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Ligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj4Passo5())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj4Passo4()


def Disj4Passo3():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8' or elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D4e.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 elem_sel + ' ligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D4'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj4Passo4())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj4Passo3()


def Disj4Passo2a():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D4d2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S17 e S18 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D4'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj4Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj4Passo2a()


def Disj4Passo2b():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D4d1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S15 e S16 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D4'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9'])
        combo.set('')

        botao1.configure(command=lambda: Disj4Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj4Passo2b()

		
def Disj4Passo1a():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8':
        newImage = PhotoImage(file='img/bar8/bar8D4c2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D8 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D4'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9', ])
        combo.set('')

        botao1.configure(command=lambda: Disj4Passo2a())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj4Passo1a()


def Disj4Passo1b():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D4c1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D9 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D4'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9' ])
        combo.set('')

        botao1.configure(command=lambda: Disj4Passo2())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj4Passo1b()


def analiseD4():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D4b2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S15 e S16 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D4'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj4Passo1a())

    elif elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D4b1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S17 e S18 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D4'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj4Passo1b())

    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        analiseD4()


def Disj3Passo6():
    elem_sel = combo.get()

    if elem_sel == 'Trocar D3':
        newImage = PhotoImage(file='img/bar8/bar8D3h.png')
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
        Disj3Passo6()


def Disj3Passo5():
    elem_sel = combo.get()

    if elem_sel == 'Abrir S5-S6':
        newImage = PhotoImage(file='img/bar8/bar8D3g.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seccionadoras S5 e S6 abertas\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3'
                                'Abrir S3-S4',
                                'Fechar S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Ligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj3Passo6())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj3Passo5()


def Disj3Passo4():
    elem_sel = combo.get()

    if elem_sel == 'Desligar D3':
        newImage = PhotoImage(file='img/bar8/bar8D3f.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D3 desligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Ligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj3Passo5())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj3Passo4()


def Disj3Passo3():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8' or elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D3e.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 elem_sel + ' ligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj3Passo4())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj3Passo3()


def Disj3Passo2a():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D3d2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S17 e S18 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D3'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj3Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj3Passo2a()


def Disj3Passo2b():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D3d1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S15 e S16 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D3'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9'])
        combo.set('')

        botao1.configure(command=lambda: Disj3Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj3Passo2b()

		
def Disj3Passo1a():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8':
        newImage = PhotoImage(file='img/bar8/bar8D3c2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D8 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9', ])
        combo.set('')

        botao1.configure(command=lambda: Disj3Passo2a())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj3Passo1a()


def Disj3Passo1b():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D3c1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D9 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9' ])
        combo.set('')

        botao1.configure(command=lambda: Disj3Passo2())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj3Passo1b()


def analiseD3():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D3b2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S15 e S16 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj3Passo1a())

    elif elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D3b1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S17 e S18 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D3'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj3Passo1b())

    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        analiseD3()


def Disj2Passo6():
    elem_sel = combo.get()

    if elem_sel == 'Trocar D2':
        newImage = PhotoImage(file='img/bar8/bar8D2h.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D2 trocado\n'
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


def Disj2Passo5():
    elem_sel = combo.get()

    if elem_sel == 'Abrir S3-S4':
        newImage = PhotoImage(file='img/bar8/bar8D2g.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seccionadoras S3 e S4 abertas\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2'
                                'Fechar S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Ligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj2Passo6())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo5()


def Disj2Passo4():
    elem_sel = combo.get()

    if elem_sel == 'Desligar D2':
        newImage = PhotoImage(file='img/bar8/bar8D2f.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Disjuntor D2 desligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Ligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj2Passo5())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo4()


def Disj2Passo3():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8' or elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D2e.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 elem_sel + ' ligado\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Desligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj2Passo4())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo3()


def Disj2Passo2a():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D2d2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S17 e S18 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D2'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj2Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo2a()


def Disj2Passo2b():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D2d1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text=	'--------------------------------------------------------------\n'
								'Seccionadoras S15 e S16 fechadas\n'
								'Selecione o próximo passo:\n'
								'--------------------------------------------------------------')
        combo.configure(values=['Trocar D2'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9'])
        combo.set('')

        botao1.configure(command=lambda: Disj2Passo3())
    else:
        telaInt.configure(
            text='--------------------------------------------------------------\n'
                 'Seleção inválida!\n'
                 'Selecione o próximo passo:\n'
                 '--------------------------------------------------------------')
        Disj2Passo2b()

		
def Disj2Passo1a():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D8':
        newImage = PhotoImage(file='img/bar8/bar8D2c2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D8 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Desligar D8',
                                'Ligar D9', ])
        combo.set('')

        botao1.configure(command=lambda: Disj2Passo2a())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj2Passo1a()


def Disj2Passo1b():
    elem_sel = combo.get()

    if elem_sel == 'Ligar D9':
        newImage = PhotoImage(file='img/bar8/bar8D2c1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Disjuntor de transferência D9 ligado\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Desligar D9' ])
        combo.set('')

        botao1.configure(command=lambda: Disj2Passo2())
    else:
        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seleção inválida!\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        Disj2Passo1b()


def analiseD2():
    elem_sel = combo.get()

    if elem_sel == 'Fechar S15-S16':
        newImage = PhotoImage(file='img/bar8/bar8D3b2.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S15 e S16 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Abrir S15-S16',
                                'Fechar S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj2Passo1a())

    elif elem_sel == 'Fechar S17-S18':
        newImage = PhotoImage(file='img/bar8/bar8D3b1.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        telaInt.configure(text='--------------------------------------------------------------\n'
                               'Seccionadoras S17 e S18 fechadas\n'
                               'Selecione o próximo passo:\n'
                               '--------------------------------------------------------------')
        combo.configure(values=['Trocar D2'
                                'Abrir S3-S4',
                                'Abrir S5-S6',
                                'Abrir S7-S8',
                                'Abrir S9-S10',
                                'Abrir S11-S12',
                                'Abrir S13-S14',
                                'Fechar S15-S16',
                                'Abrir S17-S18',
                                'Desligar D2',
                                'Desligar D3',
                                'Desligar D4',
                                'Desligar D5',
                                'Desligar D6',
                                'Desligar D7',
                                'Ligar D8',
                                'Ligar D9',])
        combo.set('')

        botao1.configure(command=lambda: Disj2Passo1b())

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
                           'Falha no ' + elem_falha + '\n'
                           'Selecione o próximo passo:\n'
                           '--------------------------------------------------------------')
    combo.configure(values=['Abrir S3-S4',
                            'Abrir S5-S6',
                            'Abrir S7-S8',
                            'Abrir S9-S10',
                            'Abrir S11-S12',
                            'Abrir S13-S14',
                            'Fechar S15-S16',
                            'Fechar S17-S18',
                            'Desligar D2',
                            'Desligar D3',
                            'Desligar D4',
                            'Desligar D5',
                            'Desligar D6',
                            'Desligar D7',
                            'Ligar D8',
                            'Ligar D9', ])
    combo.set('')
    botao1.configure(text='Próximo Passo')
    botao2.configure(text='Sair')

    if elem_sel == 'Disjuntor D2':
        newImage = PhotoImage(file='img/bar8/bar8D2a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        botao1.configure(command=lambda: analiseD2())

    elif elem_sel == 'Disjuntor D3':
        newImage = PhotoImage(file='img/bar8/bar8D3a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        def analiseD3():
            pass

        botao1.configure(command=lambda: analiseD3())

    elif elem_sel == 'Disjuntor D4':
        newImage = PhotoImage(file='img/bar8/bar8D4a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        def analiseD4():
            pass

        botao1.configure(command=lambda: analiseD4())

    elif elem_sel == 'Disjuntor D5':
        newImage = PhotoImage(file='img/bar8/bar8D5a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        def analiseD5():
            pass

        botao1.configure(command=lambda: analiseD5())

    elif elem_sel == 'Disjuntor D6':
        newImage = PhotoImage(file='img/bar8/bar8D6a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        def analiseD6():
            pass

        botao1.configure(command=lambda: analiseD6())

    elif elem_sel == 'Disjuntor D7':
        newImage = PhotoImage(file='img/bar8/bar8D7a.png')
        diagrama.configure(image=newImage)
        diagrama.image = newImage

        def analiseD7():
            pass

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
image = PhotoImage(file='img/bar8/bar8.png')
diagrama = Label(container1, image=image)
diagrama.pack(expand=True, fill='both')


# Criação Tela Interativa
telaInt = Label(subcontainer1,
                text='--------------------------------------------------------------\n'
                     'Barramento Duplo com Disjuntor e Um Terço\n\n'
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
                   'Disjuntor D7', ]
combo.pack(fill='x', padx=10, pady=10)


# Criação Botões
botao1 = Button(subcontainer3, text='Iniciar Manobra', font=('Times New Roman', '14'), command=lambda: selectFalha())
botao2 = Button(subcontainer3, text='Sair', font=('Times New Roman', '14'), command=lambda: app.destroy())
botao1.pack(side='left', fill='x', expand='yes', padx=10, pady=10)
botao2.pack(side='left', fill='x', expand='yes', padx=10, pady=10)

app.mainloop()
