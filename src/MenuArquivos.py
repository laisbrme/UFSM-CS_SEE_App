'''
    Comandos ...
'''
import os

class ComandosParaJanelasArquivos:
    def semComando(self):
        pass

    def openLOG(self):
        self.path_dir = os.getcwd() + '\\src\\barras\\LOGs'
        os.startfile(self.path_dir)

'''
teste = ComandosParaJanelas()
teste.janelaSobre()
'''
