# mary_shaw.soraya.main.py
"""
    Jogo do Tesouro Inca
"""

__author__ = "Sávyo V Morais (savyo.morais@labnet.nce.ufrj.br)"

from _spy.vitollino.main import Cena
IMAGEM_DO_TEMPLO = "https://i.imgur.com/i3RQJUF.jpg"

class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena """
        
        
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo  = "Templo do Tesouro Inca"
        print("Descrição: ", self.cena_do_templo)
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoTesouroInca()
    jogo.inicia()