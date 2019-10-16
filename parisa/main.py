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
        if TemploInca.camara:
            TemploInca.camara -= 1
            self.pega(1)
        else:
            print ("Não há mais tesouros!")
            self.sai()    
        
    def pega(self, quantidade):
        """ Coloca um tesouro na mochila """
        print (f"Você coloca {quantidade} tesouro na mochila.")
        TemploInca.mochila += quantidade 
        print (f"Você fica com {TemploInca.mochila} tesouros na mochila.")
        self.entra()
        
    def sai(self):
        """ Sai do Templo """
        print (f"Você saiu do Templo e voltou para sua Cabana")
        TemploInca.cabana, TemploInca.mochila = TemploInca.mochila, 0
        print ("Você ficou com {TemploInca.cabana} tesouros na sua Cabana.")
    
        
if __name__ == "__main__":
      TemploInca().inicia()
        
        