# mary_shaw.rachel.main.py
#Aula03


# Refatoração: 
# É quando você mexe em toda a estrutura do programa, mas 
# a funcionalidade dele não muda. Isso geralmente é feito quando vc 
# precisa colocar novas funcionalidades no programa e o código atual
# não comporta tal adição. Nesse momento, tenho que repensar toda a
# estrutura orientada a objeto do código realizado. Há diversos 
# modelos de refactoring.
#
# Níveis de abstração: Quando vc vai desenvolver um sistema, vc deve 
# analisar o problema em diferentes graus de abstração. Um nível inicial
# inidicaria que vc tem um bird eye do problema, ou seja, uma visão aérea
# e superficial da coisa. Aos poucos, vou me aprofundando no problema e 
# detalhando cada vez mais o mesmo. Nesse momento, vou passando os níveis
# e posso chegar a ter que refatorar o meu código, pq podem ter classes que
# já foram desenvolvidas e vc não precisa mais, ou ainda, posso precisar de 
# estruturas que não visualizei de tão longe nas abstrações.
# - Nível gaivota (bird eye)
# - Nível peixe (visão superficial inserida no problema)
# - Nível concha do mar ou tatuí (visão de dentro da implementação do código)
#
# Modelagem e programação estão intrínsecamente relacionados de modo que
# um pode fazer com que eu tenha que alterar o outro durante suas
# produções.
#
# MontyPython - Capítulo Bycicle Repair Man
# Mostra um modelo de refatoração que foi seguido pelo Python.
# 
# ClassExtraction:
# É um modelo de refatoração realizado pelas próprias IDEs, que utiliza
# uma inteligência artificial para extrair uma classe de dentro da outra.
# Observe que tudo é feito automaticamente pela IDE, retirando a classe, 
# arrumando os parâmetros e retirando os ctrl+C e ctrl+V que vc utilizou 
# pelo código
#
#
# A orientação objeto com as refatorações perde um pouco de desempenho na 
# execução, no entanto se ganha tempo no desenvolvimento do código e 
# manutenção do mesmo.
#
#
# Paradigma MVC:
# É uma forma de se organizar o código que acaba por criar cópias de códigos
# em 3 locais diferentes, mas possibilita uma melhor manutenção do código.
# Camadas = Model, View, Controller
# Nesse modelo, separamos as classes de modelos de dados, as classes que irão
# mexer com a apresentação preciosa e as classes que controlam todo o funcionamento
# do sistema. Nesse momento, posso ter uma classe de PedrasPreciosas para 
# cuidar da modelagem dos dados das pedras, uma para cuidar da apresentação das
# pedras na tela e uma terceira para cuidar do funcionamento das pedras, ou seja, 
# cuidar das trocas automáticas das pedras de menor valor para as de maior 
# valor.
#
# Observe que isso possibilita que eu consiga separar o desenvolvimento das três
# classes, posso inclusive ter uma equipe de fronted, ou seja, só de apresentação
# dos elementos, posso ter uma equipe de backend para cuidar do funcionamento e 
# posso ter uma equipe de banco de dados para modelar os dados e tratá-los. Tudo
# isso funcionaria com APIs entre as três camadas.
#
# API declarativa é aquela que documenta a forma de funcionamento para que as 
# diferentes equipes possam entender como funciona.

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


# Foi decidido que PedrasPreciosas é uma classe a parte e não deve ser utilizado
# ctrl+C e ctrl+V para ficar acertando elas em diversas partes do código. Nesse
# momento, vemos a necessidade de se criar uma classe própria para representar as 
# PedrasPreciosas. Nesse momento, temos que aplicar o refactor para extrair a 
# classe PedrasPreciosas de dentro de Tesouros. Do mesmo modo, teremos que modificar
# todos os pontos que tinham implementações das PedrasPreciosas. 
# Se eu não fizesse isso, eu teria que realizar alterações em diversas partes do 
# código quando precisasse modificar as funcionalidades da classe PedrasPreciosas
# que ainda não existia.
class PedrasPreciosas:
    """ Pedras que integram o tesouro """
    def __init__(self, quantas_pedras=4):
        """ Inicia a camara contendo umas pedras
            :param int quantas_pedras: numero de pedras nesta camara
        """
        # tesouro_contabil irá me indicar quanto eu tenho de tesouro em unidades 
        # mínimas que são as turquesas. Observe que essa primeira linha pertence 
        # ao MODEL, quanto que a seguinte pertence ao VIEW. Está tudo misturado na 
        # mesma classe
        
        # = MODEL = 
        self.tesouro_contabil = quantas_pedras
        # = MODEL = 
        
        # DOM (Documento Object Model) é um elemento dentro do browser, como estamos 
        # utilizando aqui o browser para rodar o jogo, iremos representar os objetos 
        # no DOM. Esse DOM aparece aqui como a classe Elemento.
        # = VIEW =
        self.pedras_especificas = [Elemento(
             TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in
             range(self.tesouro_contabil)]
             
        self.limbo_onde_as_pedras_desaparecem = Cena()
        # = VIEW =
        
    # = CONTROLLER = 
    def representa(self, local):
        """
            Apresenta as pedras organizadas em um local
        """
        for pedra in self.pedras_especificas:
            pedra.entra(local)
            
    def some(self):
        """
            Desaparece com as pedras organizadas em um local
        """
        for pedra in self.pedras_especificas:
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
                # Atribuição múltipla
                # Em Python posso fazer atribuições múltiplas, ou seja, eu coloco várias na
                # mesma linha e tudo vai sendo atribuído em cascata.
                self.pedras = pedras_na_camara = choice(range(1,5))
                self.c = camara = Tesouros(pedras_na_camara, acampamento, eu)
                camara.vai()
                # Aparece a imagem com o texto e quando vc dispensa ela, ele chama o método
                # pega_tesouro.
                Texto(camara, "Você encontra um tesouro!", foi=self.pega_tesouro).vai()
                
            def pega_tesouro(self):
                eu.ganho(self.pedras)
                self.pedras = 0
                self.c.esvazia_camara()
                
        self.tesouro = quantas_pedras
        super().__init__(TESOURO, esquerda=acampamento, direita=ProximaCamara())
        
        # Se eu estivesse em uma IDE com refactor, eu podia selecionar o código abaixo 
        # e pedir extract class. Ele iria indicar a dependência do self.tesouro que seria
        # colocado no init da classe nova, assim como perguntaria sobre o nome da nova classe
        # essa nova classe é a PedrasPreciosas que está criada acima.
        #self.pedras = [Elemento(
             #TURQUESA, x=50+50*pedra, y=250, w=40, h=40, cena=self) for pedra in
             #range(self.tesouro)]
        self.pedras = PedrasPreciosas(quantas_pedras=self.tesouro)
        
        # A classe Tesouro herda de Cena, ou seja, ela é uma cena também, pq mostra a
        # carta da câmara com as pedras em cima. Nesse caso, preciso chamar o método
        # representa da classe PedrasPreciosas para poder representá-las na tela. No 
        # entanto, tal método precisa receber o local aonde será desenhado. Aqui este
        # local é o próprio Tesouro, ou seja, self.
        self.pedras.representa(self)
        
        # Poderia ainda trocar as duas linhas anteriores por
        # PedrasPreciosas(quantas_pedras=self.tesouro).representa(self)
        # mas isso poderia ficar complicado para entender depois e eu não sei se p
        # precisarei utilizar a variável self.pedras mais adiante no código.
        
    def esvaziar_camara(self):
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
