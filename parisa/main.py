# mary_shaw.parisa.main.py
#site: http://supygirls.pythonanywhere.com/

"""
     Jogo do Tesouro Inca
     
     Uma aventura pelas Câmaras do Templo Inca, onde encontramos perigos e tesouros.

"""

__author__ = "Fernanda Prazeres <fprazeres at dcc ufrj br>"


class TemploInca:
    cabana = 0
    mochila = 0
    camara = 3 
    
    def inicia (self):
        """ inicia a aventura """
        print ("Uma aventura para coletar os tesouros do Templo Inca")
        self.entra()
        
    def entra (self):
        """ entra na câmara """
        print ("Você encontrou tesouro!")
        self.pega(1)
        
    def pega(self, quantidade):
        """ Coloca um tesouro na mochila """
        print (f"Sua mochila {quantidade} ficou mais pesada!")
        TemploInca.mochila += quantidade 
        
        
        
if __name__ == "__main__":
      TemploInca().inicia()
        
        