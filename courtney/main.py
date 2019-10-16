# mary_shaw.danae.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
"""
__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"
from random import randint

class Util:
    """ Contém funcionalidades auxiliadores às demais classes do sistema """
    def equivalencia(pedras):
    """ Simplificar a lista de pedras em uma equivalente """    
    
    TURQUEZA  = 1
    OBSIDIANA = 5
    OURO      = 10
    
    soma = pedras.sum() 
    nova = []
    qtdOuro = int(soma/OURO)    
    resto   = soma%OURO  
    for i in range(qtdOuro):
        nova.append(OURO)
    if resto >= OBSIDIANA:
        qtdObsidiana = int(resto/OBSIDIANA)
        for i in range(qtdObsidiana):
            nova.append(OBSIDIANA)    
    qtdTurqueza = soma - sum(nova)       
    for i in range(qtdTurqueza):
        nova.append(TURQUEZA)
    nova.sort() #ordenar
    return np.array(nova)

class Explorador:
    """ explora o templo inca"""
    def __init__(self, templo_inca):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        self.templo = templo_inca
        # self.camara = camara
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        print(f"Você coloca {quantidade} tesouro na mochila ")
        self.mochila += quantidade
        print(f"Você fica com {self.mochila} tesouros na mochila ")
        if input("Continua? (s/N)").lower() == "s":
            camara.entra()
        else:
            self.sai()
            
    def sai(self):
        """ sai do templo """
        print("Você sai do templo e guarda os tesouros!")
        self.cabana += self.mochila
        self.mochila = 0
        print(f"Você ficou com {self.cabana} tesouros na cabana!")
        if input("Inicia nova Incursão? (s/N)").lower() == "s":
            self.templo.inicia()


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
        self.explorador = Explorador(templo_inca=self)  # (self) (self.camara)
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


