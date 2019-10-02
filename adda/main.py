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


class Jogador():
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro """
        self.tesouro = 0 
        
        
    def ganho(self, valor):
        """ aumenta o tesouro com valor equivalente de turquesas
           :param valor: valor acrescentar ao tesouro em número de turnos
        """
        self.tesouro += valor
        INVENTARIO.bota("turquesa", TURQUESA)


class Tesouros(Cena):
    """ Camaras secretas contendo tesouros """
    def __init__(self, quantas_pedras=4):
        """ Inicia a camara contendo umas pedras
            :param int quantas_pedras: numero de pedras nesta camara
        """
        class ProximaCamara:
            def vai(self):
                pedras_na_camara = choice(range(1,5))
                Tesouros(pedras_na_camara, acampamento, eu).vai()
                eu.ganho(pedras_na_camara)
        self.tesouro = quantas_pedras
        super().__init__(TESOURO, esquerda=acampamento, direita=ProximaCamara())
        self.pedras = [Elemento(
             TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in
             range(self.tesouro)]
             
class Tumba():
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self, acampamento, eu):
        """ Inicia o complexo de camaras """
        self.tumba = [Tesouros(pedras+1, acampamento, eu) for pedras in range(4)]
        self.inicial = choice(self.tumba)



class Acampamento(Cena):
    """ um lugar seguro e quentinho para admirar seus ganhos """
    def __init__(self, cena):
        """ Inicia com tesouro vazio """
        self.tesouro = 0
        super().__init__(cena)
        self.pedra = Elemento(TURQUESA, cena=self)
        
    def ganho(self, valor):
        """ aumenta o tesouro com valor equivalente de turquesas
           :param valor: valor acrescentar ao tesouro em número de turnos
        """
        self.tesouro += valor


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