# mary_shaw.roxanne.main.py
# from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
from elemento.main import Elemento
from random import choice

__author__ = "Carlo"
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
MUMIA = "https://i.imgur.com/YGV3CPB.jpg"
COBRA = "https://i.imgur.com/IeC0gBj.jpg"
TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]
ACAMPAMENTO = "https://i.imgur.com/dmSDeDF.jpg"

TUMBA = [COBRA, MUMIA] + [TESOURO]*3


class Jogador():
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro """


class Tesouros(Cena):
    """ Camaras secretas contendo tesouros """
    def __init__(self, quantas_pedras=4, acampamento=None):
        """ Inicia a camara contendo umas pedras
            :param int quantas_pedras: numero de pedras nesta camara
        """
        class ProximaCamara:
            def vai(self):
                Tesouros(choice(range(1,5)), acampamento).vai()
        self.tesouro = quantas_pedras
        super().__init__(TESOURO, esquerda=acampamento, direita=ProximaCamara())
        #self.pedra = Elemento(TURQUESA, x=50, y=250, w=40, h=40, cena=self)
        self.pedras = [Elemento(
             TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in
             range(self.tesouro)]


class Tumba():
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self, acampamento):
        """ Inicia o complexo de camaras """
        self.tumba = [Tesouros(pedras+1, acampamento) for pedras in range(4)]
        self.inicial = choice(self.tumba)


class Acampamento(Cena):
    """ Um lugar seguro e quentinho para admirar seus ganhos """
    def __init__(self, cena):
        """ Cria a cena de um acampamento com tesouros """
        self.tesouro = 4
        super().__init__(cena)
        #self.pedra = Elemento(TURQUESA, x=50, y=250, w=40, h=40, cena=self)
        self.pedras = [Elemento(
             TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in
             range(self.tesouro)]

    def ganho(self, valor):
        """ aumenta o tesouro com um valor de pedras """
        self.tesouro += valor


class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena"""
        self.acampamento = Acampamento(ACAMPAMENTO)
        self.tumba = Tumba(self.acampamento)
        self.cena_do_templo = Cena(
        IMAGEM_DO_TEMPLO, self.acampamento, direita=self.tumba.inicial)
        self.acampamento.direita = self.cena_do_templo
        
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    #print(JogoTesouroInca,JogoTesouroInca())
