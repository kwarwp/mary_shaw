# mary_shaw.parisa.main.py
#site: http://supygirls.pythonanywhere.com/

"""
     Jogo do Tesouro Inca
     
     Uma aventura pelas Câmaras do Templo Inca, onde encontramos perigos e tesouros.

"""

__author__ = "Fernanda Prazeres <fprazeres at dcc ufrj br>"

class Explorador:
    """ explora o templo inca """
    def __init__(self):
        self.mochila = 0
        self.cabana = 0
        camara = TemploInca ()
                
        def pega(self, quantidade, camara):
        """ Coloca um tesouro na mochila """
        print (f"Você coloca {quantidade} tesouro na mochila.")
        self.mochila += quantidade 
        print (f"Você fica com {TemploInca.mochila} tesouros na mochila.")
        camara.entra()
        
        def sai(self):
        """ Sai do Templo """
        print (f"Você saiu do Templo e voltou para sua Cabana")
        self.cabana, self.mochila = self.mochila, 0
        print (f"Você ficou com {TemploInca.cabana} tesouros na sua Cabana.")
    


class TemploInca:
    camara = 3
    
    def __init__(self):
        self.explorador = Explorador()
        self.cabana = Explorador()
    
    def inicia (self):
        """ inicia a aventura """
        print ("Uma aventura para coletar os tesouros do Templo Inca")
        self.entra()
                  
    def entra (self):
        """ entra na câmara """
        print ("Você encontrou tesouro!")
        if TemploInca.camara:
            TemploInca.camara -= 1
            self.explorador.pega(1, self)
        else:
            print ("Não há mais tesouros!")
            self.explorador.sai()    
            
if __name__ == "__main__":
      TemploInca().inicia()
        
        