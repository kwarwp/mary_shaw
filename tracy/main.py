# mary_shaw.tracy.main.py
"""
    Tesouro Inca
"""
__author__ = "Lorena"


class JogoTesouroInca:
    """ Representa o Jogo principal """
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo = "Templo do tesouro Inca"
        print("Descrição:", self.cena_do_templo)
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoTesouroInca()