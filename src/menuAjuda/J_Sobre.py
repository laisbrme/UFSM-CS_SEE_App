'''
 Janela Sobre do menu Ajuda
'''

from tkinter import *
from PIL import ImageTk, Image

app = Tk()

app.title("Sobre UFSM-CS SEE")
app.geometry("450x300")

img = ImageTk.PhotoImage(Image.open("src\image\sobre.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

texto_orientacao = Label(app,
                         text="Sobre UFSM-CS SEE App"
                                   "\nVersão 0.1"
                                   "\n\nEsta aplicação foi criada com o intuito de auxiliar "
                                   "\nna disciplina de Subestações de Energia Elétrica, "
                                   "\ndo curso de Engenharia Elétrica, da Universidade "
                                   "\nFederal de Santa Maria - Campus Cachoeira do Sul!"
                                   "\n\nApenas para uso educacional!",
                         font="Times 12",
                         )
texto_orientacao.grid(column=0, row=0, padx=50, pady=50)

barraMenu = Menu(app)

app.mainloop()