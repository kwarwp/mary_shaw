# mary_shaw.roxanne.main.py
from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
__author__ = "Carlo"


class JogoTesouroInca:
    """ Representa o Jogo principal """
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo = "Templo perdido do tesouro Inca"
        print("Descrição:", self.cena_do_templo, __name__)
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoMarilia()
    jogo.inicia()
    outro_jogo.inicia()