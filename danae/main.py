# mary_shaw.danae.main.py
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
    def __init__(self):
        self.qualquercoisa = None


class TemploInca:
    camara = 3
    def __init__(self):
        # self.camara = Camara()
        self.explorador = Explorador()  # (self) (self.camara)

    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros do Templo Inca")
        self.entra()
        
        
    def entra(self):
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


