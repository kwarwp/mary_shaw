# mary_shaw.grace.main.py
from _spy.vitollino.main import Cena
"""
    Jogo do Tesouro Inca
"""
__author__ = "Andre"

IMAGEM_DO_TEMPLO = "https://i.imgur.com/pq242D7.jpg" #É UMA CONSTANTE

class JogoTesouroInca:
    """ Representa o jogo principal """
    def __init__(self):
        """Constroi a cena"""
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)

    def inicia(self):
        """ Inicia a construção do jogo """
        self.cena_do_templo.vai()
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoTesouroInca()
    jogo.inicia()
    