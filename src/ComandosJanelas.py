class ComandosParaJanelas():

    def semComando(self):
        pass

    def janelaSobre(self):
        exec(open("menuAjuda.py", "r").read())



teste = ComandosParaJanelas()
teste.janelaSobre()