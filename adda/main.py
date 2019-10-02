# mary_shaw.adda.main.py
# http://supygirls.pythonanywhere.com/
"""
   Tesouro Inca
   
"""
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
from random import choice

__author__= "Marilia Campos Galvao"
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
ACAMPAMENTO = "https://i.imgur.com/BYbVL1h.png"
MUMIA = "https://i.imgur.com/7zpjq5n.jpg"
COBRA = "https://i.imgur.com/oedLlYp.png"
ARANHA = "https://i.imgur.com/4fLlUgc.png"
FOGO = "https://i.imgur.com/4CqvxjJ.png"
DESABAMENTO = "https://i.imgur.com/rJVEyMd.png"
TESOURO = "https://i.imgur.com/kUJCXLT.png"
TURQUESA = "https://i.imgur.com/UyWcGCx.png"
OBSIDIANA = "https://i.imgur.com/dVl5lML.png"
OURO = "https://i.imgur.com/ZtBckCi.png"


TUMBA = [COBRA, MUMIA] + [TESOURO]*3


class PedrasPreciosas:
    """ Um conjunto de pedras que se organizam por valor """
    def __init__(self, valor):
        """ Inicia com valor equivalente de turquesas
           :param valor: valor do tesouro em número de turquesas.
        """
        ...

    def aumenta(self, valor):
        """ aumenta o tesouro com valor equivalente de turquesas
           :param valor: valor a acrescentar ao tesouro em número de turnos
        """
        ...
        
class Acampamento(Cena):
    """ um lugar seguro e quentinho para admirar seus ganhos """
    def __init__(self, cena):
        """ Inicia com tesouro vazio """
        self.tesouro = 0
        super().__init__(cena)
        
        
    def ganho(self, valor):
        """ aumenta o tesouro com valor equivalente de turquesas
           :param valor: valor acrescentar ao tesouro em número de turnos
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


#camel case só se usa em nome de classe
class JogoTesouroInca:
    """ Representa o Jogo principal """
    def __init__(self):
        """ Constroi a cena """
        self.acampamento = Acampamento(ACAMPAMENTO)
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        self.acampamento.direita = self.cena_do_templo
         
    def inicia(self):
        """ Inicia a construção do jogo """
        self.cena_do_templo.vai()
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()