# mary_shaw.roxanne.main.py
# from adda.main import JogoTesouroInca as JogoMarilia
"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
# from elemento.main import Elemento
from random import choice

__author__ = "Lorena"
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
IMAGEM_DO_TEMPLO2 = "https://i.imgur.com/TZHHss8.jpg"
MUMIA = "https://i.imgur.com/a9ePBx5.png"
COBRA = "https://i.imgur.com/T9EwoOc.png"
TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
FOGO = "https://i.imgur.com/LGlVkUM.png"
ARANHA = "https://i.imgur.com/DMAU5DF.gif"
PEDREIRA = "https://i.imgur.com/4JPWbQg.png"
TURQUESA = "https://i.imgur.com/8WDBJM3.png"
ACAMPAMENTO = "https://i.imgur.com/BoPPjLb.jpg"

TUMBA = [COBRA, MUMIA] + [TESOURO]*3
'''
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
        self.tesouro += valor      '''

class Jogador():
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro, com acampamento 
            :param acampamento: o acampamento do jogador para a hora que ele desiste, ele colocar as pedras
        """
        self.tesouro = 0
    
    def ganho(self, valor):
        """ Aumenta o tesouro com valor equivalente de turquesas 
            :param valor: valor a acrescentar ao tesouro em número de Turquesas.        
        """   
        self.tesouro += valor
        [INVENTARIO.bota("turquesa", TURQUESA) for _ in range(valor)]

    def desiste(self):
        """ remove as pedras do inventário e coloca na cabana """

class PedrasPreciosas:
    """ Pedras que integram o tesouro"""
    def __init__(self, quantas_pedras=0):
        """ Inicia aa coleção de padras com uma quantidade
            :param int quantas_pedras: numero de pedras neste tesouro
        """
        # = MODELO Conceitual = 
        self.tesouro_contabil = quantas_pedras
        # = VISTA = Modelo visual de como apresentar o tesouro
        self.limbo_onde_as_pedras_desaparecem = Cena()
        self.pedras_especificas = [Elemento(
             TURQUESA, x=50+50*pedra, y=250, w=40, h=40) for pedra in
             range(self.tesouro_contabil)]
             
    def representa(self, local):
        """ Apresenta as pedras organizadas em um local """
        for pedra in self.pedras_especificas:
            pedra.entra(local)
             
    def some(self):
        """ Desaparece com as pedras organizadas em um local """
        for pedra in self.pedras_especificas:
            pedra.entra(self.limbo_onde_as_pedras_desaparecem)

class Tesouros(Cena):
    """ Camaras secretas contendo tesouros """
    def __init__(self, quantas_pedras=0, acampamento=None, eu=None):
        """ Inicia a camara contendo umas pedras
            :param int quantas_pedras: numero de pedras nesta camara
        """
        class ProximaCamara:
            def vai(self):
                self.pedras = pedras_na_camara = choice(range(1,5))
                self.c = camara = Tesouros(pedras_na_camara, acampamento, eu)
                camara.vai()
                Texto(camara, 
                      "Você encontra um tesouro!",
                      foi=self.pega_tesouro).vai()
            def pega_tesouro(self):
                eu.ganho(self.pedras)
                self.pedras = 0
                self.c.esvazia_camara()
        self.tesouro = quantas_pedras
        super().__init__(TESOURO, esquerda=acampamento, direita=ProximaCamara())
        self.pedras = PedrasPreciosas(quantas_pedras=self.tesouro)
        self.pedras.representa(self)
    def esvazia_camara(self):
        self.tesouro = 0
        self.pedras.some()


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
        self.tesouro = 0
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
    #print(JogoTesouroInca,JogoTesouroInca())
