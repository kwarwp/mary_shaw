# mary_shaw.rachel.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
 
 19.11.06c - usa defaultdict na Camara no caso de if quantidade: também
 19.11.06b - usa defaultdict na Camara também
 19.11.06a - usa defaultdict como uma forma de switch
 19.11.06 - troca print por input
"""

__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"
__version__ = "19.11.06b"
from random import randint
from collections import defaultdict


class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara?
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        self.mochila += quantidade
        input(f"Você coloca {quantidade} pedras na mochila e fica com {self.mochila} tesouros")
        camara.entra(self)
                    
    def sai(self):
        """ sai do templo """
        self.cabana, self.mochila = self.mochila, 0
        input(f"Você sai do templo e guarda {self.cabana} tesouros na cabana!")


class Camara:
    """ Uma câmara do templo.
    o explorador usa o método entra para ter acesso aos tesouros
    """
    def __init__(self):
        self.quantidade = 3
        self.decide = defaultdict(lambda: self.desiste)
        self.decide["s"] = self.encara
        for counter in range(1, self.quantidade + 1):
            self.decide[counter] = self.continua
        
    def entra(self, explorador):
        """ entra em uma câmara"""
        o_que_decidiu = input("Você entra em uma câmara com tesouros! Continua?")
        self.decide[o_que_decidiu.lower()](explorador)
        
        
    def encara(self, explorador):
        """ decide continuar a exploração """
        self.decide[self.quantidade](explorador)
        '''
        if self.quantidade:
            self.quantidade -= 1        
            explorador.pega(randint(1, 4), self)
        else:
            #input("Não havia mais tesouros!")
            explorador.sai()
        '''
        
    def continua(self, explorador):
        """ desiste da exploração """
        self.quantidade -= 1        
        explorador.pega(randint(1, 4), self)
        
    def desiste(self, explorador):
        """ desiste da exploração """
        explorador.sai()


class TemploInca:
    """ O jogo do Tesouro Inca
    
    o jogo inicia quando se chama o método inicia
    """
    def __init__(self):
        self.explorador = Explorador()
        self.camara = Camara()
        self.decide = defaultdict(lambda: self.desiste)
        self.decide["s"] = self.encara
        
    def inicia(self):
        """ inicia a exploração """
        o_que_decidiu = input("Uma expedição para saquear o Templo Inca. Vai encarar (s/N)?")
        self.decide[o_que_decidiu]()
        
    def encara(self):
        """ decide iniciar a exploração """
        self.camara.entra(self.explorador)
        
    def desiste(self):
        """ desiste da exploração """
        input("Sábia decisão, vamos evitar este templo macabro!")
        
        
    


if __name__ == "__main__":
    TemploInca().inicia()


































# mary_shaw.rachel.main.py

#"""
#    Tesouro Inca
#"""
#from _spy.vitollino.main import Cena, INVENTARIO
#from elemento.main import Elemento
#from random import choice

#__author__ = "Andre"
#IMAGEM_DO_TEMPLO = "https://i.imgur.com/hYLSAKf.jpg"
#MUMIA = "https://i.imgur.com/YGV3CPB.jpg"
#COBRA = "https://i.imgur.com/IeC0gBj.jpg"
#TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
#TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]
#OBSIDIANA = "https://i.imgur.com/84kWpjt.png"
#OURO = "https://i.imgur.com/50TXu9B.png"
#ACAMPAMENTO = "https://i.imgur.com/dmSDeDF.jpg"

#TUMBA = [COBRA, MUMIA] + [TESOURO]*3


#class Jogador():
#    """ Um explorador em busca de tesouros """
#    def __init__(self):
#        """ Inicia com tesouro , com acampamento
#            :param acampamento: o acampamento do jogador
#        """
#       self.tesouro = 0
#    
#    def ganho(self, valor):
#        """ Aumenta o tesouro com valor equivalente de turquesas 
#            :param valor: valor a acrescentar ao tesouro em número de Turquesas.        
#        """   
#        self.tesouro += valor
#        
#        ouro = int(valor / 10)
#        quantidade = valor % 10
#        obsidiana = int(quantidade / 5)
#        turquesa = quantidade % 5
        
#        [INVENTARIO.bota("ouro", OURO) for _ in range(ouro)]
#        [INVENTARIO.bota("obsidiana", OBSIDIANA) for _ in range(obsidiana)]
#        [INVENTARIO.bota("turquesa", TURQUESA) for _ in range(turquesa)]

#    def desiste(self):
#        """
#            Remove as pedras do inventario e coloca na cabana
#        """


#class PedrasPreciosas:
#    """ Pedras que integram o tesouro"""
#    def __init__(self, quantas_pedras=4):
#        """ Inicia aa coleção de pedras com uma quantidade
#            :param int quantas_pedras: numero de pedras neste tesouro
#        """
#        # = MODEL = 
#        self.tesouro_contabil = quantas_pedras
#        self.tipos_de_pedras = self.cambio_de_pedras(quantas_pedras)
#        # = MODEL = 

        # = VIEW =
#        self.limbo_onde_as_pedras_desaparecem = Cena()
        
#        self.pedras_ouro = [Elemento(
#             OURO, x=50+50*pedra, y=250, w=40, h=40) for pedra in
#             range(self.tipos_de_pedras['ouro'])]
#        self.origem = 50 + 50 * self.tipos_de_pedras['ouro']
        
#        self.pedras_obsidiana = [Elemento(
#             OBSIDIANA, x=self.origem+50*pedra, y=250, w=40, h=40) for pedra in
#             range(self.tipos_de_pedras['obsidiana'])]
#        self.origem = self.origem + 50 * self.tipos_de_pedras['obsidiana']
        
#        self.pedras_turquesa = [Elemento(
#             TURQUESA, x=self.origem+50*pedra, y=250, w=40, h=40) for pedra in
#             range(self.tipos_de_pedras['turquesa'])]
        # = VIEW =
        
    # = MODEL = 
#    def cambio_de_pedras(self, quantidade):
#        print(quantidade)
        
#        tipos_de_pedras = {
#             'ouro' : 0,
#             'obsidiana' : 0,
#             'turquesa' : 0
#        }
        
#        tipos_de_pedras['ouro'] = int(quantidade / 10)
#        quantidade = quantidade % 10
#        tipos_de_pedras['obsidiana'] = int(quantidade / 5)
#        tipos_de_pedras['turquesa'] = int(quantidade % 5)
        
        
#        print(tipos_de_pedras)
        
#        return tipos_de_pedras
    # = MODEL = 
    
    # = CONTROLLER = 
#    def representa(self, local):
#        """ Apresenta as pedras organizadas em um local """
#        for pedra in self.pedras_ouro:
#            pedra.entra(local)
#        for pedra in self.pedras_obsidiana:
#            pedra.entra(local)
#        for pedra in self.pedras_turquesa:
#            pedra.entra(local)
            
#    def some(self):
#        """ Desaparece com as pedras organizadas em um local """
#        for pedra in self.pedras_ouro:
#            pedra.entra(self.limbo_onde_as_pedras_desaparecem)
#        for pedra in self.pedras_obsidiana:
#            pedra.entra(self.limbo_onde_as_pedras_desaparecem)
#        for pedra in self.pedras_turquesa:
#            pedra.entra(self.limbo_onde_as_pedras_desaparecem)
    # = CONTROLLER = 


#class Tesouros(Cena):
#    """ Camaras secretas contendo tesouros """
#    def __init__(self, quantas_pedras=4, acampamento=None, eu=None):
#        """ Inicia a camara contendo umas pedras
#            :param int quantas_pedras: numero de pedras nesta camara
#        """
#        class ProximaCamara:
#            def vai(self):
#                self.pedras = pedras_na_camara = choice(range(1,20))
#                self.c = camara = Tesouros(pedras_na_camara, acampamento, eu)
#                camara.vai()
#                Texto(camara, 
#                      "Você encontra um tesouro!",
#                      foi=self.pega_tesouro).vai()
                
#            def pega_tesouro(self):
#                eu.ganho(self.pedras)
#                self.pedras = 0
#                self.c.esvazia_camara()
                
#        self.tesouro = quantas_pedras
#        super().__init__(TESOURO, esquerda=acampamento, direita=ProximaCamara())
#        self.pedras = PedrasPreciosas(quantas_pedras=self.tesouro)
#        self.pedras.representa(self)
        
#    def esvazia_camara(self):
#        self.tesouro = 0
#        self.pedras.some()


#class Tumba():
#    """ Um complexo de camaras secretas sob o templo """
#    def __init__(self, acampamento, eu):
#        """ Inicia o complexo de camaras """
#        self.tumba = [Tesouros(pedras+1, acampamento, eu) for pedras in range(4)]
#        self.inicial = choice(self.tumba)


#class Acampamento(Cena):
#    """ Um lugar seguro e quentinho para admirar seus ganhos """
#    def __init__(self, cena):
#        """ Cria a cena de um acampamento com tesouros """
#        self.tesouro = 0
#        super().__init__(cena)        

#    def deposita(self, valor):
#        """ aumenta o tesouro com um valor de pedras """
#        self.tesouro += valor
#        self.pedras = [Elemento(
#             TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in
#             range(self.tesouro)]
        


#class JogoTesouroInca:
#    """ Representa o Jogo principal """
#    def __init__(self):
#        """ Constroi a cena"""
#        INVENTARIO.inicia()
#        self.acampamento = Acampamento(ACAMPAMENTO)
#        self.eu = Jogador()
#        self.tumba = Tumba(self.acampamento, self.eu)
#        self.cena_do_templo = Cena(
#        IMAGEM_DO_TEMPLO, self.acampamento, direita=self.tumba.inicial)
#        self.acampamento.direita = self.cena_do_templo
        
#    def inicia(self):
#        """ Inicia a construção do Jogo """
#        self.cena_do_templo.vai()
        
        
#if __name__ == "__main__":
#    jogo = JogoTesouroInca()
#    jogo.inicia()
    #print(JogoTesouroInca,JogoTesouroInca())
    
# https://www.magazineluiza.com.br/ar-condicionado-split-dual-inverter-lg-12-000-btus-frio-127v-/p/kd0gg0gg40/ar/aciv/?&utm_source=google&utm_medium=pla&utm_campaign=PLA_marketplace&partner_id=15696&seller_id=climario&gclid=EAIaIQobChMIz-HDr9nV5QIVFoCRCh1xYA9yEAQYAiABEgLxQvD_BwE

