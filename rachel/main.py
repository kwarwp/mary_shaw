# mary_shaw.rachel.main.py
"""
    Jogo do Tesouro Inca
     
"""
__author__ = "Andre R Vieira"


class JogoTesouroInca:
    """ Representa o Jogo principal """
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo = "Templo do tesouro Inca"
        print("Descrição:", self.cena_do_templo, __name__)
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoTesouroInca()
    jogo.inicia()