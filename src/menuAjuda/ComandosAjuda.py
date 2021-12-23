class ComandosParaJanelasAjuda():

    def semComando(self):
        pass

    def janelaSobre(self):
        exec(open("src\menuAjuda\J_Sobre.py").read())

    def janelaManual(self):
        exec(open("src\menuAjuda\Manual.pdf").read())


'''
teste = ComandosParaJanelas()
teste.janelaSobre()
'''