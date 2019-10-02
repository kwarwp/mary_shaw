# mary_shaw.lisa.main.py
"""
    Título: Jogo do Tesouro Inca
"""
__author__ = "Victor Azevedo (victorvaacs@gmail.com)"
#PEP 8 diz que a primeira parte é a documentação
from _spy.vitollino.main import Cena
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hgBdcTi.jpg"
#constantes em python são escritas em CAPSLOCK por isso IMAGEM_DO_TEMPLO é escrita assim pq ela é uma constante

#tem que entender a class e a instancia
#class é um processo para fazer algo - 

class Jogador:
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro """

class JogoTesouroInca:
#kamelcase só usa em classes
#ver documento PEP 8
    """ Representa o Jogo principal """
#define o comportamento inicial
#self = comportamento do objeto
    def __init__(self):
        """Constroi a Cena"""
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)


    def inicia(self):
        #self.cena_do_templo = "Templo do Tesouro Inca"
        #print("Descrição:", self.cena_do_templo)
        self.cena_do_templo.vai() 
#pass = não faça nada 

if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()