# mary_shaw.lisa.main.py
"""
    Título: Jogo do Tesouro Inca
"""
__author__ = "Victor Azevedo (victorvaacs@gmail.com)"
#PEP 8 diz que a primeira parte é a documentação

class JogoTesouroInca:
#kamelcase só usa em classes
#ver documento PEP 8
    """ Representa o Jogo principal """
#define o comportamento inicial
#self = comportamento do objeto
    def inicia(self):
        self.cena_do_templo = "Templo do Tesouro Inca"
        print("Descrição:", self.cena_do_templo)