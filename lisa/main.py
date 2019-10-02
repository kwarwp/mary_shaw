# mary_shaw.lisa.main.py
"""
    Título: Jogo do Tesouro Inca
"""
__author__ = "Victor Azevedo (victorvaacs@gmail.com)"
#PEP 8 diz que a primeira parte é a documentação
from _spy.vitollino.main import Cena, INVENTARIO, Elemento
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
#constantes em python são escritas em CAPSLOCK por isso IMAGEM_DO_TEMPLO é escrita assim pq ela é uma constante

#tem que entender a class e a instancia
#class é um processo para fazer algo - 



class Jogador():
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro """

class Tesouro(Cena):
    """ Um lugar seguro e quentinho para admirar seus ganhos """
    def __init__(self, quantas_pedras=4):
        """ Inicia a camara contendo umas padras 
        :param int quantas_pedras: numero de pedras nesta camara """
        self.tesouro = quantas_pedras
        super().__init__(cena)
        #self.pedra = Elemento(TURQUESA, x=50, y=250, w=40, h=40, cena=self)
        self.pedras = [Elemento(
             TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in
             range(self.tesouro)]

class Tumba():
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self):
        """ Inicia o complexo de camaras """
        self.tumba = [Tesouro(pedras+1) for pedras in range(4)]
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
#kamelcase só usa em classes
#ver documento PEP 8
    """ Representa o Jogo principal """
#define o comportamento inicial
#self = comportamento do objeto
    def __init__(self):
        """ Constroi a cena"""
        self.acampamento = Acampamento(ACAMPAMENTO)
        self.tmba = Tumba()
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO, self.acampamento)
        self.acampamento.direita = self.cena_do_templo
        
    def inicia(self):
    #self.cena_do_templo = "Templo do Tesouro Inca"
    #print("Descrição:", self.cena_do_templo)
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
    #pass = não faça nada  
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    #print(JogoTesouroInca,JogoTesouroInca())
