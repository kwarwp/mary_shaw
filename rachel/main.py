# mary_shaw.rachel.main.py
#Aula03


# Refatoração: É quando você mexe em toda a estrutura do programa, mas 
# a funcionalidade dele não muda. Isso geralmente é feito quando vc 
# precisa colocar novas funcionalidades no programa e o código atual
# não comporta tal adição. Nesse momento, tenho que repensar toda a
# estrutura orientada a objeto do código realizado.
#
# Níveis de abstração: Quando vc vai desenvolver um sistema, vc deve 
# analisar o problema em diferentes graus de abstração. Um nível inicial
# inidicaria que vc tem um bird eye do problema, ou seja, uma visão aérea
# e superficial da coisa. Aos poucos, vou me aprofundando no problema e 
# detalhando cada vez mais o mesmo. Nesse momento, vou passando os níveis
# e posso chegar a ter que refatorar o meu código, pq podem ter classes que
# já foram desenvolvidas e vc não precisa mais, ou ainda, posso precisar de 
# estruturas que não visualizei de tão longe nas abstrações.
# Nível gaivota (bird eye)
# Nível peixe (visão superficial inserida no problema)
# Nível concha do mar ou tatuí (visão de dentro da implementação do código)
#
# 


"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena, INVENTARIO
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
        self.tesouro = 0
    
    def ganho(self, valor):
        """ Aumenta o tesouro com valor equivalente de turquesas 
            :param valor: valor a acrescentar ao tesouro em número de Turquesas.        
        """   
        self.tesouro += valor
        [INVENTARIO.bota("turquesa", TURQUESA) for _ in range(valor)]


class PedrasPreciosas:
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
