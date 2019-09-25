# mary_shaw.tracy.main.py
from ada.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
__author__ = "Lorena P Grion"


class JogoTesouroInca:
    """ Representa a classe do Jogo principal """
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo = "Templo do tesouro Inca"
        print("Descrição:", self.cena_do_templo)
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoMarilia()
    jogo.inicia()
    outro_jogo.incia()