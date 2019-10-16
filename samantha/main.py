# mary_shaw.samantha.main.py
from random import randint
"""
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
"""

__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"


class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara?
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        print(f"Você coloca {quantidade} tesouro na mochila ")
        self.mochila += quantidade
        print(f"Você fica com {self.mochila} tesouros na mochila ")
        if input("Continua?").lower() == "s":
            camara.entra(self)
        else:
            self.sai()
        
            
    def sai(self):
        """ sai do templo """
        print("Você sai do templo e guarda os tesouros!")
        self.cabana, self.mochila = self.mochila, 0
        print(f"Você ficou com {self.cabana} tesouros na cabana!")


class Camara:
    def __init__(self):
        self.quantidade = 3
        #self.explorador = explorador
        
    def entra(self, explorador):
        """ entra em uma câmara"""
        print("Você entra em uma câmara com tesouros!")
        if self.quantidade:
            self.quantidade -= 1        
            explorador.pega(1, self)
        else:
            print("Não havia mais tesouros!")
            explorador.sai()


class TemploInca:
    def __init__(self):
        self.explorador = Explorador()
        self.camara = Camara()
        
    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros do Templo Inca")
        self.camara.entra(self.explorador)
        
        
    


if __name__ == "__main__":
    TemploInca().inicia()

