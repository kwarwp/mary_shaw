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
        """ Aumenta o tesouro com valor equivalente de turquesas 
            :param valor: valor a acrescentar ao tesouro em número de Turquesas.        
        """   
        self.tesouro += valor
        [INVENTARIO.bota("turquesa", TURQUESA) for _ in range(valor)]



class Tesouros(Cena):
    """ Camaras secretas contendo tesouros """
    def __init__(self, quantas_pedras=4, acampamento=None, eu=None):
        """ Inicia a camara contendo umas pedras
            :param int quantas_pedras: numero de pedras nesta camara
        """
        class ProximaCamara:
            def vai(self):
                pedras_na_camara = choice(range(1,5))
                Tesouros(0, acampamento, eu).vai()
                eu.ganho(pedras_na_camara)
        self.tesouro = quantas_pedras
        super().__init__(TESOURO, esquerda=acampamento, direita=ProximaCamara())
        #self.pedra = Elemento(TURQUESA, x=50, y=250, w=40, h=40, cena=self)
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
    """ Um lugar seguro e quentinho para admirar seus ganhos """
    def __init__(self, cena):
        """ Cria a cena de um acampamento com tesouros """
        self.tesouro = 4
        super().__init__(cena)
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
        INVENTARIO.inicia()
        self.acampamento = Acampamento(ACAMPAMENTO)
        self.eu = Jogador()
        self.tumba = Tumba(self.acampamento, self.eu)
        self.cena_do_templo = Cena(
        IMAGEM_DO_TEMPLO, self.acampamento, direita=self.tumba.inicial)
        self.acampamento.direita = self.cena_do_templo
        
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
