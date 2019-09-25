# mary_shaw.kathryn.main.py
# from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"

__author__ = "Pablo LV"


class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena"""
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        
    def inicia(self):
        """ Inicia a construção do Jogo """
        pass
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    
    
