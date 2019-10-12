# mary_shaw.rachel.main.py

"""
    Tesouro Inca
"""
from _spy.vitollino.main import Cena, INVENTARIO
from elemento.main import Elemento
from random import choice

__author__ = "Andre"
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
MUMIA = "https://i.imgur.com/YGV3CPB.jpg"
COBRA = "https://i.imgur.com/IeC0gBj.jpg"
TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]
OBSIDIANA = "https://i.imgur.com/84kWpjt.png"
OURO = "https://i.imgur.com/50TXu9B.png"
ACAMPAMENTO = "https://i.imgur.com/dmSDeDF.jpg"

TUMBA = [COBRA, MUMIA] + [TESOURO]*3


class Jogador():
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro , com acampamento
            :param acampamento: o acampamento do jogador
        """
        self.tesouro = 0
    
    def ganho(self, valor):
        """ Aumenta o tesouro com valor equivalente de turquesas 
            :param valor: valor a acrescentar ao tesouro em número de Turquesas.        
        """   
        self.tesouro += valor
        
        ouro = int(self.tesouro / 10)
        quantidade = self.tesouro % 10
        obsidiana = int(quantidade / 5)
        turquesa = quantidade % 5
        
        [INVENTARIO.bota("ouro", OURO) for _ in range(ouro)]
        [INVENTARIO.bota("obsidiana", OBSIDIANA) for _ in range(obsidiana)]
        [INVENTARIO.bota("turquesa", TURQUESA) for _ in range(tuquesa)]

    def desiste(self):
        """
            Remove as pedras do inventario e coloca na cabana
        """


class PedrasPreciosas:
    """ Pedras que integram o tesouro"""
    def __init__(self, quantas_pedras=4):
        """ Inicia aa coleção de pedras com uma quantidade
            :param int quantas_pedras: numero de pedras neste tesouro
        """
        # = MODEL = 
        self.tesouro_contabil = quantas_pedras
        self.tipos_de_pedras = self.cambio_de_pedras(quantas_pedras)
        # = MODEL = 

        # = VIEW =
        self.limbo_onde_as_pedras_desaparecem = Cena()
        
        self.pedras_ouro = [Elemento(
             OURO, x=50+50*pedra, y=250, w=40, h=40) for pedra in
             range(self.tipos_de_pedras['ouro'])]
        self.origem = 50 + 50 * self.tipos_de_pedras['ouro']
        
        self.pedras_obsidiana = [Elemento(
             OBSIDIANA, x=self.origem+50*pedra, y=250, w=40, h=40) for pedra in
             range(self.tipos_de_pedras['obsidiana'])]
        self.origem = self.origem + 50 * self.tipos_de_pedras['obsidiana']
        
        self.pedras_turquesa = [Elemento(
             TURQUESA, x=self.origem+50*pedra, y=250, w=40, h=40) for pedra in
             range(self.tipos_de_pedras['turquesa'])]
        # = VIEW =
        
    # = MODEL = 
    def cambio_de_pedras(self, quantidade):
        print(quantidade)
        
        tipos_de_pedras = {
             'ouro' : 0,
             'obsidiana' : 0,
             'turquesa' : 0
        }
        
        tipos_de_pedras['ouro'] = int(quantidade / 10)
        quantidade = quantidade % 10
        tipos_de_pedras['obsidiana'] = int(quantidade / 5)
        tipos_de_pedras['turquesa'] = int(quantidade % 5)
        
        
        print(tipos_de_pedras)
        
        return tipos_de_pedras
    # = MODEL = 
    
    # = CONTROLLER = 
    def representa(self, local):
        """ Apresenta as pedras organizadas em um local """
        for pedra in self.pedras_ouro:
            pedra.entra(local)
        for pedra in self.pedras_obsidiana:
            pedra.entra(local)
        for pedra in self.pedras_turquesa:
            pedra.entra(local)
            
    def some(self):
        """ Desaparece com as pedras organizadas em um local """
        for pedra in self.pedras_ouro:
            pedra.entra(self.limbo_onde_as_pedras_desaparecem)
        for pedra in self.pedras_obsidiana:
            pedra.entra(self.limbo_onde_as_pedras_desaparecem)
        for pedra in self.pedras_turquesa:
            pedra.entra(self.limbo_onde_as_pedras_desaparecem)
    # = CONTROLLER = 


class Tesouros(Cena):
    """ Camaras secretas contendo tesouros """
    def __init__(self, quantas_pedras=4, acampamento=None, eu=None):
        """ Inicia a camara contendo umas pedras
            :param int quantas_pedras: numero de pedras nesta camara
        """
        class ProximaCamara:
            def vai(self):
                self.pedras = pedras_na_camara = choice(range(1,20))
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

