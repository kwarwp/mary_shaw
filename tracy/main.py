# mary_shaw.roxanne.main.py
# from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
from random import choice

__author__ = "Lorena"
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
MUMIA = "https://i.imgur.com/a9ePBx5.png"
COBRA = "https://i.imgur.com/T9EwoOc.png"
TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
FOGO = "https://i.imgur.com/LGlVkUM.png"
ARANHA = "https://i.imgur.com/DMAU5DF.gif"
PEDREIRA = "https://i.imgur.com/4JPWbQg.png"
TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]

TUMBA = [COBRA, MUMIA] + [TESOURO]*3

class PedrasPreciosas():
    """ Um Conjunto de pedras que se organizam por valor """
    def __init__(self, valor):
        """ Inicia com valor equivalente de turquesas 
            :param valor: valor do tesouro em número de Turquesas.        
        """
        ...
        
    def aumenta(self, valor):
        """ Aumenta o tesouro com valor equivalente de turquesas 
            :param valor: valor a acrescentar ao tesouro em número de Turquesas.        
        """        

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
#jogo.inicia()
#print(help(JogoTesouroInca.inicia, JogoTesouroInca.inicia())
print(help(PedrasPreciosas))