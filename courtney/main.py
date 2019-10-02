# mary_shaw.roxanne.main.py
# from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
from random import choice

__author__ = "Carlo"
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
MUMIA = "https://i.imgur.com/YGV3CPB.jpg"
COBRA = "https://i.imgur.com/IeC0gBj.jpg"
TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]
MINHAMUMIA = "https://i.imgur.com/GlvQM3x.jpg"

TUMBA = [COBRA, MUMIA] + [TESOURO]*3

class Jogador(Cena):
    def continua(self):
        INVENTARIO.bota("turquesa", TURQUESA)

class Camara(Cena):
    """ Uma das Camaras """
    def __init__(self, cena=MUMIA, jogador=None):
        """ Constroi a cena"""
        camara = self
        class ProximaCamara(Cena):
            def vai(self):
                jogador.continua()
                proxima = choice(TUMBA)
                Camara(proxima, jogador).vai()
                #super().vai()
        self._proxima = ProximaCamara()
        super().__init__(cena, direita=self._proxima)
    @property
    def direita(self):
        pass
    @direita.setter
    def set_direita(self, camara):
        self._proxima = camara
class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena"""
        camara = Camara(jogador=Jogador())
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO, direita=camara)
        camara.direita = Camara(COBRA, Jogador())
        
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
        
class Jogador():
    """Um eplorador em busca de tesouros"""
    def __ini__(self):
        """Inicia com tesouro"""
        
class Tumba():
    """Um complexo de camaras secretas sob o templo"""
    def __ini__(self):
        """Inicia com tesouro"""
        
class PedrasPreciosas:        
      """Um conjunto de pedras que se organizam por valor"""
    def __ini__(self,valor):
        """Inicia com valor equivalente de turquesas
           :param valor: valor do tesouro em número de turquesas.
        """
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    #print(help(JogoTesouroInca.inicia))
