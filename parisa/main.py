# mary_shaw.parisa.main.py
#site: http://supygirls.pythonanywhere.com/

#Módulos em python: from roxanne.main import JogoTesouroInca as JogoCarlo

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
        
        
        
if __name__ == "__main__":
      TemploInca().inicia()
        
        