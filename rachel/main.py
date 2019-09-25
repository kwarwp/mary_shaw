# mary_shaw.rachel.main.py

"""
    Jogo do Tesouro Inca
     
"""

#from adda.main import JogoTesouroInca as JogoMarilia
from _spy.vitollino.main import Cena
IMAGEM_DO_TEMPLO = "https://i.imgur.com/TyH3QTV.jpg"

__author__ = "Andre R Vieira"


class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena """
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    #outro_jogo = JogoMarilia()
    #outro_jogo.inicia()