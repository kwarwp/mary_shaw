# mary_shaw.grace.main.py
"""
    Jogo do Tesouro Inca
"""
__author__ = "Andre"

class JogoTesouroInca:
    """ Representa o jogo principal """
    def inicia(self):
        """ Inicia a construção do jogo """
        self.cena_do_templo = "Templo do Tesouro Inca"
        print("Descrição:", self.cena_do_templo)
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoTesouroInca()
    