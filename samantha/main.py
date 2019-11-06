# mary_shaw.samantha.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
 
 19.11.06 - troca print por input
"""

__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"
__version__ = "19.11.06"
from random import randint


class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara?
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        input(f"Você coloca {quantidade} tesouro na mochila ")
        self.mochila += quantidade
        input(f"Você fica com {self.mochila} tesouros na mochila ")
        camara.entra(self)
                    
    def sai(self):
        """ sai do templo """
        input("Você sai do templo e guarda os tesouros!")
        self.cabana, self.mochila = self.mochila, 0
        input(f"Você ficou com {self.cabana} tesouros na cabana!")


class Camara:
    def __init__(self):
        self.quantidade = 3
        #self.explorador = explorador
        
    def entra(self, explorador):
        """ entra em uma câmara"""
        input("Você entra em uma câmara com tesouros!")
        if input("Continua?").lower() == "s":
            if self.quantidade:
                self.quantidade -= 1        
                explorador.pega(randint(1, 4), self)
            else:
                input("Não havia mais tesouros!")
                explorador.sai()
        else:
            return
        


class TemploInca:
    def __init__(self):
        self.explorador = Explorador()
        self.camara = Camara()
        
    def inicia(self):
        """ inicia a exploração """
        input("Uma expedição para coletar os tesouros do Templo Inca")
        self.camara.entra(self.explorador)
        
        
    


if __name__ == "__main__":
    TemploInca().inicia()

