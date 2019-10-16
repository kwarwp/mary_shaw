"""
     Jogo do Tesouro Inca
     
     Uma aventura pelas Câmaras do Templo Inca, onde encontramos perigos e tesouros.

"""

__author__ = "Fernanda Prazeres <fprazeres at dcc ufrj br>"

from random import randint

#class Mochila:
 #   """ contém os tesouros coletados nas camaras"""
  #  def __init__(self):
   #     self.explorador = Explorador ()
    #    self.camara = Camara()
     #   self.cabana = Cabana()
        
        
#class Cabana:
 #   """ Contém os tesouros salvos """
  #  def __init__(self):
   #     self.explorador = Explorador ()
    #    self.camara = Camara()
     #   self.cabana = Cabana()
        
        
        

class Explorador:
    """ explora o templo inca """
    
    def __init__(self):
        self.mochila = 0
        self.cabana = 0
                        
    def pega(self, quantidade, camara):
        """ Coloca um tesouro na mochila """
        print (f"Você coloca {quantidade} tesouro na mochila.")
        self.mochila += quantidade 
        print (f"Você fica com {self.mochila} tesouros na mochila.")
        if input (" Você continua ? (sim/nao)").lower() == "sim":
            camara.entra()
        else: 
            self.sai()
        
    def sai(self):
        """ Sai do Templo """
        print (f"Você saiu do Templo e voltou para sua Cabana")
        self.cabana += self.mochila
        self.mochila = 0
        print (f"Você ficou com {self.cabana} tesouros na sua Cabana.")
    
class Camara:
    """ contém tesouros,artefatos e perigos """
    def __init__(self):
        self.explorador = Explorador()
        self.camara = 5
        
    def entra (self):
        """ entra na câmara """
        print ("Você encontrou tesouro!")
        if self.camara:
            self.camara -= 1
            self.explorador.pega(randint(1, 17), self)
        else:
            print ("Não há mais tesouros!")
            self.explorador.sai()  



class TemploInca:
        
    def __init__(self):
        self.explorador = Explorador()
        self.cabana = Explorador()
        self.camara = Camara()
    
    def inicia (self):
        """ inicia a aventura """
        print ("Uma aventura para coletar os tesouros do Templo Inca")
        self.camara.entra()
          
            
if __name__ == "__main__":
      TemploInca().inicia()
        
        