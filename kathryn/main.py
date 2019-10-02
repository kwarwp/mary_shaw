# mary_shaw.kathryn.main.py
# from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
from random import choice

__author__ = "Pablo LV"

IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
IMAGEM_DO_ACAMPAMENTO = "https://caminoincamachupicchu.org/cmingutd/images/campamentos-en-el-camino-inca.jpg"
MUMIA = "https://i.imgur.com/YGV3CPB.jpg"
COBRA = "https://i.imgur.com/IeC0gBj.jpg"
TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]

TUMBA = [COBRA, MUMIA] + [TESOURO]*3

#-------------------------------------------------------------------------
class PedrasPreciosas():
    """ Um conjunto de pedras que  """
    def __init__(self, valor):
        """ Inicia com valor equivalentebde turquesas """
        ...
    def aumenta(self, valor):
        """ Inicia com tesouro """
        ...
#-------------------------------------------------------------------------
class PedrasPreciosas():
    """ Um conjunto de pedras que  """
    def __init__(self, valor):
#-------------------------------------------------------------------------
class Jogador():
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro """
#-------------------------------------------------------------------------
class Tumba():
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self,cena):
        """ Inicia o complexo de camaras """

#-------------------------------------------------------------------------
class Acampamento(cena):
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self,cena):
        """ Inicia o complexo de camaras """
        self.tesouro = 0
        super().__init(cena)__

#-------------------------------------------------------------------------
class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena"""
        self.acampamento = Acampamento(IMAGEM_DO_ACAMPAMENTO)
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
        
#-------------------------------------------------------------------------
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    print(JogoTesouroInca,JogoTesouroInca())




