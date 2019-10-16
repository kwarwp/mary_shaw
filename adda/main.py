# mary_shaw.adda.main.py
"""
Uma expedição para coletar os tesouros do templo Inca
--Relato:
Entramos em uma tumba, percorremos câmaras que continham tesouros e perigos 
e podiamos escolher entre ficar ou sair.
"""
__autor__ = "Marília Campos Galvão"

from random import randint

class Explorador:
    def __init__(self, templo_inca):
        self.mochila = 0
        self.cabana = 0
        self.templo = templo_inca
        
    def pega(self, quantidade, camara):
        """ guarda um tesouro na machila """
        print(f"Você coloca {quantidade} tesouro na mochila" )
        self.mochila += quantidade
        print(f"Você fica com {self.mochila} tesouros na mochila")
        if input("Continua? (s/N)").lower() == "s":
            camara.entra(self)
        else:
            self.sai()
        
    def sai(self):
        """ sai do templo """
        print("Você sai do templo e guarda os tesouros!")
        self.cabana += self.mochila
        self.mochila = 0
        print(f"Você ficou com {camara.pedras} tesouros na mochila")
        if input("Nova Incursão? (s/N)").lower() == "s":
            self.templo.inicia()
class Camara:
    def __init__(self):
        self.pedras = 3
        
    def entra(self, explorador):
        """ entra em uma câmera"""
        print("O que existe nela")
        if self.pedras:
            self.pedras -= 1
            explorador.pega(randint(1, 4), self)
        else:
            print(f"A rodada acabou para você, leve suas {explorador.cabana} para cabana")
            explorador.sai()

class TemploInca:
    def __init__(self):
        self.explorador = Explorador(templo_inca=self)
        self.camara = Camara(self.explorador)

        
    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros de um templo Inca")
        self.camara.entra(self.explorador)
        
    
            
    
        
        
if __name__ == "__main__":
    TemploInca().inicia()