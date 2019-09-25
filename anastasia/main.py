# mary_shaw.anastasia.main.py

"""
    Jogo do Tesouro Inca
     
"""     
from _spy.vitollino.main import Cena
IMAGEM_DO_TEMPLO = "https://i.imgur.com/VGAHhzQ.jpg"  

__author__ = "Claudia L R Motta (claudiam@nce.ufrj.br)"



class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """Constroi a cena"""
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        
    def inicia(self):
        """Inicia a construção do Jogo"""
        self.cena_do_templo.vai()       
        
if __name__ == "__main__": 
    jogo = JogoTesouroInca()
    jogo.inicia()
    

    