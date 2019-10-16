# mary_shaw.morgan.main.py
# http://supygirls.python.pythonanywhere.com/
#from _spy.vitollino.main import Cena
#IMAGEM_DO_TEMPLO = "https://i.imgur.com/rY28mtM.jpg"

"""
Nossa aventura em busca do tesouro inca consiste no descobrimento do tesouro inca 
"""

__author__ = "Rafael Ris-Ala (rafaelrisala@ufrj.br)"

from random import randint


class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        print(f"Você coloca {quantidade} tesouro na mochila ")
        self.mochila += quantidade
        print(f"Você fica com {self.mochila} tesouros na mochila ")
        camara.entra()
            
    def sai(self):
        """ sai do templo """
        print("Você sai do templo e guarda os tesouros!")
        self.cabana, self.mochila = self.mochila, 0
        print(f"Você ficou com {self.cabana} tesouros na cabana!")


class Camara:
    def __init__(self, explorador):
        self.camara = 3
        self.explorador = explorador
        #self.quantos_tesouros = tesouros
        
    def entra(self):
        """ entra em uma câmara"""
        print("Você entra em uma câmara com tesouros!")
        if self.camara:
            self.camara -= 1        
            self.explorador.pega(randint(1, 4), self)
        else:
            print("Não havia mais tesouros!")
            self.explorador.sai()


class TemploInca:
    camara = 3
    def __init__(self):
        # self.camara = Camara()
        self.explorador = Explorador()  # (self) (self.camara)
        self.camara = Camara(self.explorador)

    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros do Templo Inca")
        self.camara.entra()
        
    def __entra(self):
        """ entra em uma câmara"""
        print("Você entra em uma câmara com tesouros!")
        if TemploInca.camara:
            TemploInca.camara -= 1        
            self.explorador.pega(1, self)
        else:
            print("Não havia mais tesouros!")
            self.explorador.sai()


if __name__ == "__main__":
    TemploInca().inicia()


