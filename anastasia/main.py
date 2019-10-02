# mary_shaw.anastasia.main.py

"""
    Jogo do Tesouro Inca
     
"""  
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
from random import choice

__author__ = "Claudia L R Motta (claudiam@nce.ufrj.br)"
IMAGEM_DO_TEMPLO = "https://i.imgur.com/6RL5A3g.jpg" 
MUMIA = "https://i.imgur.com/SoMZVzD.jpg"
COBRA = "https://i.imgur.com/IeC0gBj.jpg"
TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]

TUMBA = [COBRA, MUMIA] + [TESOURO]*3

class Jogador():
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro """


class Tumba():
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self):
        """ Inicia o complexo de camaras """


class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena"""
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    print(JogoTesouroInca,JogoTesouroInca())

    