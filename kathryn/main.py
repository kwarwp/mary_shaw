__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"
__version__ = "19.11.06d"
from random import randint
from collections import defaultdict
#================================================================================================
class Explorador:
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        self.perigos = "aranha cobra mumia desabamento fogo".split()
        # self.camara = camara?
            
    def assusta(self, tipo_perigo, camara):
        perigo = self.perigos[tipo_perigo]
        input(f"Você se assusta com este perigo: {perigo}")
        camara.entra(self)
            
    def pega(self, quantidade, camara):
        self.mochila += quantidade
        input(f"Você coloca {quantidade} pedras na mochila e fica com {self.mochila} tesouros")
        camara.entra(self)
                    
    def sai(self):
        self.cabana, self.mochila = self.mochila, 0
        input(f"Você sai do templo e guarda {self.cabana} tesouros na cabana!")
#================================================================================================
class Camara:
    def __init__(self):
        self.quantidade = 3
        self.decide = defaultdict(lambda: self.desiste)
        self.decide["s"] = self.encara
        #self.decide[1] = self.decide[2] = self.decide[3] = self.continua
        self.decide.update({chave: self.continua
            for chave in range(1, self.quantidade+1)})
        
    def entra(self, explorador):
        o_que_decidiu = input("Você entra em uma câmara com tesouros! Continua?")
        self.decide[o_que_decidiu.lower()](explorador)
        
        
    def encara(self, explorador):
        self.decide[self.quantidade](explorador)
        
    def continua(self, explorador):
        """ desiste da exploração """
        self.quantidade -= 1        
        explorador.pega(randint(1, 4), self)
        
    def desiste(self, explorador):
        """ desiste da exploração """
        explorador.sai()
#================================================================================================
class CamaraPerigosa:
    def __init__(self):
        self.quantidade = 3
        self.decide = defaultdict(lambda: self.desiste)
        self.decide["s"] = self.encara
        #self.decide[1] = self.decide[2] = self.decide[3] = self.continua
        self.decide.update({chave: self.continua
            for chave in range(1, self.quantidade+1)})
        
    def entra(self, explorador):
        o_que_decidiu = input("Você entra em uma câmara com perigos! Continua?")
        self.decide[o_que_decidiu.lower()](explorador)
        
        
    def encara(self, explorador):
        self.decide[self.quantidade](explorador)
        
    def continua(self, explorador):
        """ desiste da exploração """
        self.quantidade -= 1        
        explorador.assusta(randint(0, 4), self)
        
    def desiste(self, explorador):
        """ desiste da exploração """
        explorador.sai()
#================================================================================================
class TemploInca:
    def __init__(self):
        self.explorador = Explorador()
        self.camara = CamaraPerigosa()
        self.decide = defaultdict(lambda: self.desiste)
        self.decide["s"] = self.encara
        print(2)
        
    def inicia(self):
        o_que_decidiu = input("Uma expedição para saquear o Templo Inca. Vai encarar (s/N)?")
        self.decide[o_que_decidiu]()
        print(3)
        
    def encara(self):
        self.camara.entra(self.explorador)
        
    def desiste(self):
        input("Sábia decisão, vamos evitar este templo macabro!")
#================================================================================================
#================================================================================================
#================================================================================================
print(0)
if __name__ == "__main__":
    print(1)
    TemploInca().inicia()
#================================================================================================
