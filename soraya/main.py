# mary_shaw.roxanne.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca

Descrição: Uma excursão em busca do tesouro, entrando
em tumbas e abrindo câmaras para pegar tesouros ou 
enfrentar riscos, arriscando os prêmios a cada incursão.
O único local seguro é a cabana fora do templo.
"""

from random import randint

__author__ = "Sávyo V Morais <savyo morais at labnet nce ufrj br>"

class Explorador:
    """ explora o templo """    
    def __init__(self):
        self.mochila = 0
        self.cabana = 0
            
    def sai(self):
        """ Sai do templo e volta para a cabana """
        print("Você saiu!")
        self.cabana += self.mochila
        self.mochila = 0
        print(f"Agora você tem {self.cabana} tesouros na sua cabana")
        
    def pega(self, qtd, camara):
        """ coloca o tesouro encontrado na mochila """
        print(f"Você coloca {qtd} tesouros na mochila")
        self.mochila += qtd
        print(f"Agora você tem {self.mochila} tesouros na mochila")
        camara.entra()

class Camara:
    """ camara a ser explorada """
    
    def __init__(self, explorador):
        self.camara = 3
        self.explorador = explorador
        
    
    def entra(self):
        """ entra em uma câmara """
        if self.camara:
            self.camara -= 1
            print("Você entrou em uma câmara com tesouros!")
            self.explorador.pega(randint(1,4), self)
        else:
            print("Você já entrou em todas as câmaras!")
            self.explorador.sai()

class TemploInca:
    camara = 3
    
    def __init__(self):
        self.explorador = Explorador()
        self.camara = Camara(self.explorador)
    
    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros o Templo Inca")
        self.camara.entra()
        
        
if __name__ == "__main__":
    TemploInca().inicia()