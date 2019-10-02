# http://supygirls.pythonanywhere.com/supygirls/gamer/mary_shaw/kathryn
# mary_shaw.kathryn.main.py
# from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
from random import choice

#-------------------------------------------------------------------------
__author__ = "Pablo LV"
#-------------------------------------------------------------------------
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
IMAGEM_DO_ACAMPAMENTO = "https://caminoincamachupicchu.org/cmingutd/images/campamentos-en-el-camino-inca.jpg"
IMAGEM_DO_MUMIA = "https://i.imgur.com/YGV3CPB.jpg"
IMAGEM_DO_COBRA = "https://i.imgur.com/IeC0gBj.jpg"
IMAGEM_DO_TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
IMAGEM_DO_TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]
#-------------------------------------------------------------------------
IMAGEM_DO_TUMBA = [IMAGEM_DO_COBRA, IMAGEM_DO_MUMIA] + [IMAGEM_DO_TESOURO]*3
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
class Tesouros():
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self,quantas_pedras=4):
        self.tesouro=quantas_pedras
        super().__init__(TESOURO)
        #self.pedra  =  Elemento(IMAGEM_DO_TURQUESA, x=50, y=250, w=40, h=40, cena=self)
        self.pedras = [Elemento(
             IMAGEM_DO_TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in range(self.tesouro)]
#-------------------------------------------------------------------------
class Tumba():
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self):
        """ Inicia o complexo de camaras """
        self.tumba    = [Tesouro(pedras+1) for pedras in range(4)]
        self.inicial  = choice(self.tumba)
1#-------------------------------------------------------------------------
class Acampamento(Cena):
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self,cena):
        """ Inicia o complexo de camaras """
        self.tesouro = 4
        super().__init(cena)__
       #self.pedra  =  Elemento(IMAGEM_DO_TURQUESA, x=50, y=250, w=40, h=40, cena=self)
        self.pedras = [Elemento(
             IMAGEM_DO_TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in range(self.tesouro)]

def ganho(self,valor):
        tesouro+=valor
#-------------------------------------------------------------------------
class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena"""
        self.acampamento = Acampamento(IMAGEM_DO_ACAMPAMENTO)
        self.tumba = Tumba()
        self.cena_do_templo = Cena()

    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
        
#-------------------------------------------------------------------------
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    print(JogoTesouroInca,JogoTesouroInca())

