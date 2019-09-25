# mary_shaw.morgan.main.py
# http://supygirls.python.pythonanywhere.com/
from _spy.vitollino.main import Cena
IMAGE_DO_TEMPLO = "https://i.imgur.com/rY28mtM.jpg"

"""
    Jogo do Tesouro Inca

"""

__author__ = "Rafael Ris-Ala (rafaelrisala@ufrj.br)"

class JogoTesouroInca:
    """ Representa o Jogo Principal """
    def __init__(self):
        """Constroi a cena """
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        
    def inicia(self):
        """ Inicia a construção do jogo"""
        pass
"""        self.cena_do_templo = "Templo do tesouro Inca"
        print("Descrição:", self.cena_do_templo)
"""

if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()