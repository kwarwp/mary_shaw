# mary_shaw.libby.main.py
#http://supygirls.pythonanywhere.com/
"""
    Jogo do Tesouro Inca
"""
__author__ = "Carlos Augusto T. Alves"

class JogoTesouroInca:
    """ Representa o jogo principal """
    def inicia(self):
        """ Inicia a construção do jogo"""
        self.cena_do_templo = "Templo do tesouro Inca"
        print("Descrição:",self.cena_do_templo)

if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_Jogo = JogoTesouroInca()
    jogo.inicia()