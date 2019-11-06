# mary_shaw.samantha.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
 
 19.11.06b - usa defaultdict na Camara também
 19.11.06a - usa defaultdict como uma forma de switch
 19.11.06 - troca print por input
"""

__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"
__version__ = "19.11.06b"
from random import randint
from collections import defaultdict


class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara?
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        self.mochila += quantidade
        input(f"Você coloca {quantidade} pedras na mochila e fica com {self.mochila} tesouros")
        camara.entra(self)
                    
    def sai(self):
        """ sai do templo """
        self.cabana, self.mochila = self.mochila, 0
        input(f"Você sai do templo e guarda {self.cabana} tesouros na cabana!")


class Camara:
    """ Uma câmara do templo.
    o explorador usa o método entra para ter acesso aos tesouros
    """
    def __init__(self):
        self.quantidade = 3
        #self.explorador = explorador
        
    def entra(self, explorador):
        """ entra em uma câmara"""
        #input("Você entra em uma câmara com tesouros!")
        decisao = input("Você entra em uma câmara com tesouros! Continua (s/N)?")
        self.decide[decisao]()
         if self.quantidade:
                self.quantidade -= 1        
                explorador.pega(randint(1, 4), self)
            else:
                input("Não havia mais tesouros!")
                explorador.sai()
        '''
        if input("Você entra em uma câmara com tesouros! Continua?").lower() == "s":
            if self.quantidade:
                self.quantidade -= 1        
                explorador.pega(randint(1, 4), self)
            else:
                input("Não havia mais tesouros!")
                explorador.sai()
        else:
            explorador.sai()
        '''


class TemploInca:
    """ O jogo do Tesouro Inca
    
    o jogo inicia quando se chama o método inicia
    """
    def __init__(self):
        self.explorador = Explorador()
        self.camara = Camara()
        self.decide = defaultdict(lambda: self.desiste)
        self.decide["s"] = self.encara
        '''
        self.decide = defaultdict(lambda: input("Sábia mimimi.. macabro!"))
        self.decide["s"] = lambda: self.camara.entra(self.explorador)
        '''
        
    def inicia(self):
        """ inicia a exploração """
        o_que_decidiu = input("Uma expedição para saquear o Templo Inca. Vai encarar (s/N)?")
        self.decide[o_que_decidiu]()
        
    def encara(self):
        """ decide iniciar a exploração """
        self.camara.entra(self.explorador)
        
    def desiste(self):
        """ desiste da exploração """
        input("Sábia decisão, vamos evitar este templo macabro!")
        
        
    


if __name__ == "__main__":
    TemploInca().inicia()

