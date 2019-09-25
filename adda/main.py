# mary_shaw.adda.main.py
# http://supygirls.pythonanywhere.com/
"""
   Tesouro Inca
   
"""
from _spy.vitollino.main import Cena
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"

__author__= "Marilia Campos Galvao"

#camel case só se usa em nome de classe
class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a construção do jogo """
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        
    def inicia(self):
        """ Inicia a construção do jogo """
        self.cena_do_templo.vai
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()