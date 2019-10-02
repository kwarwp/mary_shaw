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
TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]
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
        
class Acampamento(Cena):
    """ Acampamento é um lugar seguro e quentinho para admirar os seus ganhos """
    def __init__(self, cena):
        """ Cria a cena de um acampmanto com tesouro vazio """
        self.tesouro = 0
        super().__init__(cena)
        self.pedra = Elemento(TURQUESA, cena=self)
        
    def ganoho(self, valor):
        """ Aumenta o tesouro com valor equivalente de turquesas 
            :param valor: valor a acrescentar ao tesouro em número de Turquesas.        
        """   
        self.tesouro += valor      

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
        #self.acampamento = Cena(ACAMPAMENTO)
        self.acampamento = Acampamento(ACAMPAMENTO)
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO, self.acampamento)
        self.acampamento.direita = self.cena_do_templo
        
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    #print(help(JogoTesouroInca.inicia, JogoTesouroInca.inicia())
    #print(help(Cena))