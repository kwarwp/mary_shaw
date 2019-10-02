# mary_shaw.roxanne.main.py
# from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
from elemento.main import Elemento
from random import choice

__author__ = "Lorena"
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
MUMIA = "https://i.imgur.com/a9ePBx5.png"
COBRA = "https://i.imgur.com/T9EwoOc.png"
TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
FOGO = "https://i.imgur.com/LGlVkUM.png"
ARANHA = "https://i.imgur.com/DMAU5DF.gif"
PEDREIRA = "https://i.imgur.com/4JPWbQg.png"
TURQUESA = "https://i.imgur.com/8WDBJM3.png"
ACAMPAMENTO = "https://i.imgur.com/BoPPjLb.jpg"

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
        ...
        

    def ganho(self, valor):
        """ Aumenta o tesouro com valor equivalente de turquesas 
            :param valor: valor a acrescentar ao tesouro em número de Turquesas.        
        """   
        self.tesouro += valor      

class Jogador():
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro """


class Tesouros(Cena):
    """ Camaras secretas contendo tesouros """
    def __init__(self, quantas_pedras=4):
        """ Inicia a camara contendo umas pedras
            :param int quantas_pedras: numero de pedras nesta camara
        """
        self.tesouro = quantas_pedras
        super().__init__(TESOURO)
        #self.pedra = Elemento(TURQUESA, x=50, y=250, w=40, h=40, cena=self)
        self.pedras = [Elemento(
             TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in
             range(self.tesouro)]


class Tumba():
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self):
        """ Inicia o complexo de camaras """
        self.tumba = [Tesouros(pedras+1) for pedras in range(4)]
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
        self.tumba = Tumba()
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
