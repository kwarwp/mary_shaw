# mary_shaw.anastasia.main.py

"""
    Uma expedição para coletar os tesouros do Templo Inca
    --Relato:
    Fomos explorar um tempo Inca onde havia câmaras com tesouros. Acampamos perto do templo onde fomos 
    guardando os tesouros. Fizemos diversas incursões mas tivemos que enfrentar diversos perigos. Voltei com meu tesouro
    mas nem todos tiveram a mesma sorte.
"""

__author__ = "Claudia L R Motta <claudiam at nce.ufrj.br>"


class Explorador:
    """ Explora o templo  """
    def __init__(self): #(self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara
        
    def pega(self, quantidade, camara):
        """ Coloca um tesouro na mochila """ 
        print(f"Você coloca {quantidade} tesouro na mochila")
        self.mochila += quantidade
        print(f"Você fica com {self.mochila} tesouros na mochila")
        camara.entra()       
        
    def sai(self):
        """" Sai do Templo """
        print( "Você sai do templo e guarda os tesouros na cabana!")
        self.mochila , self.mochila  = self.mochila, 0
        print(f"Você ficou com {self.cabana} tesouros na cabana!")
        
        
class Camara:
    def __init__ (self):
        self.qualquercoisa = None

class TemploInca:
    camara = 3
    def __inicia__(self):
        # self.camara = camara()
        self.explorador - Explorador() # (self) (self.camara)
        
    
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
        