# mary_shaw.lisa.main.py
"""
    Título: Jogo do Tesouro Inca
"""
__author__ = "Victor Azevedo (victorvaacs@gmail.com)"
#PEP 8 diz que a primeira parte é a documentação
from spy.vitollino.main import Cena
IMAGEM_DO_TEMPLO = "https://i.imgur.com/hgBdcTi.jpg"
#constantes em python são escritas em CAPSLOCK por isso IMAGEM_DO_TEMPLO é escrita assim pq ela é uma constante


class JogoTesouroInca:
#kamelcase só usa em classes
#ver documento PEP 8
    """ Representa o Jogo principal """
#define o comportamento inicial
#self = comportamento do objeto
    def inicia(self):
        self.cena_do_templo = "Templo do Tesouro Inca"
        print("Descrição:", self.cena_do_templo)
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()