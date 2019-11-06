"""
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
 
 19.11.06f - troca aleatoriamente entre perigos e tesouros
 19.11.06e - introduz camara com perigos que espantam o explorador
 19.11.06d - introduz camara com perigos
 19.11.06c - usa defaultdict na Camara no caso de if quantidade: também
 19.11.06b - usa defaultdict na Camara também
 19.11.06a - usa defaultdict como uma forma de switch
 19.11.06 - troca print por input
"""

__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"
__version__ = "19.11.06f"
from random import randint
from collections import defaultdict


class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        self.perigos = "aranha cobra mumia desabamento fogo".split()
        # self.camara = camara?
            
    def espanta(self, tipo_perigo, camara):
        """ se espanta com um perigo e foge do templo """
        perigo = self.perigos[tipo_perigo]
        input(f"Você se espanta por ver de novo o perigo: {perigo}")
        self.sai()
            
    def assusta(self, tipo_perigo, camara):
        """ se assusta com um perigo """
        perigo = self.perigos[tipo_perigo]
        input(f"Você se assusta com este perigo: {perigo}")
        camara.entra(self)
            
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
        self.quantidade = 8
        self.decide = defaultdict(lambda: self.desiste)
        self.decide["s"] = self.encara
        #self.decide[1] = self.decide[2] = self.decide[3] = self.continua
        self.decide.update({chave: self.continua
            for chave in range(1, self.quantidade+1)})
        self.outra_camara = None
        
    def adentra(self, camara_outra):
        """ entra em uma câmara, com a opção de entrar na outra"""
        self.outra_camara = camara_outra
        if not camara_outra.outra_camara:
            camara_outra.adentra(self)
        return self
        
    def entra(self, explorador):
        """ entra em uma câmara"""
        o_que_decidiu = input("Você entra em uma câmara com tesouros! Continua?")
        self.decide[o_que_decidiu.lower()](explorador)
        
        
    def encara(self, explorador):
        """ decide continuar a exploração """
        self.decide[self.quantidade](explorador)
        
    def continua(self, explorador):
        """ desiste da exploração """
        self.quantidade -= 1        
        explorador.pega(randint(1, 4), self)
        
    def desiste(self, explorador):
        """ desiste da exploração """
        explorador.sai()


class CamaraPerigosa(Camara):
    """ Uma câmara do templo.
    o explorador usa o método entra para ter acesso aos tesouros
    """
    def __init__(self):
        super().__init__()
        self.perigos = {perigo: 0 for perigo in range(5)}
        pass
        
    def entra(self, explorador):
        """ entra em uma câmara"""
        
        o_que_decidiu = input("Você entra em uma câmara com perigos! Continua?")
        self.decide[o_que_decidiu.lower()](explorador)
        
    def continua(self, explorador):
        """ desiste da exploração """
        self.quantidade -= 1
        tipo_perigo = randint(0, 4)
        perigos = self.perigos[tipo_perigo] = self.perigos[tipo_perigo] + 1
        if perigos > 1:
            explorador.espanta(tipo_perigo, self)
        else:
            explorador.assusta(tipo_perigo, self)


class TemploInca:
    """ O jogo do Tesouro Inca
    
    o jogo inicia quando se chama o método inicia
    """
    def __init__(self):
        self.explorador = Explorador()
        self.camara = CamaraPerigosa().adentra(Camara())
        self.decide = defaultdict(lambda: self.desiste)
        self.decide["s"] = self.encara
        
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
    #import mary_shaw.samantha.main as mn
    #print(help(mn))

