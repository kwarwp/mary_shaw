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
        self.templo = TemploInca() 
        self.explorador = Explorador()
                        
    def pega(self, quantidade, camara):
        """ Coloca um tesouro na mochila """
        print (f"Você coloca {quantidade} tesouro na mochila.")
        self.mochila += quantidade 
        print (f"Você fica com {self.mochila} tesouros na mochila.")
        if input (" Você continua ? (sim/nao)").lower() == "si":
            camara.entra()
        else: 
            self.sai()
        
    def sai(self):
        """ Sai do Templo """
        print (f"Você saiu do Templo e voltou para sua Cabana")
        self.cabana += self.mochila
        self.mochila = 0
        print (f"Você ficou com {self.cabana} tesouros na sua Cabana.")
        if input ("Nova Incursão a vista! Quer participar? (sim/nao)").lower() == "si":
            self.templo.inicia()
        
    
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
        if input("Você entra em uma câmara com tesouros! Continua?").lower() == "s":
            if self.quantidade:
                self.quantidade -= 1        
                explorador.pega(randint(1, 4), self)
            else:
                input("Não havia mais tesouros!")
                explorador.sai()
        else:
            explorador.sai()



class TemploInca:
        
    def __init__(self):
        self.explorador = Explorador()
        self.camara = Camara()
    
    def inicia (self):
        """ inicia a aventura """
        input ("Uma aventura para coletar os tesouros do Templo Inca, vai encarar? (si/no)")
        if encara == "si":
            self.camara.entra(self.explorador)
        else:
            input("Então, volte para a sua cabana.")
                      
            
if __name__ == "__main__":
      TemploInca().inicia()
        
        