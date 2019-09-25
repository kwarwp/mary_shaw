# mary_shaw.morgan.main.py
# http://supygirls.python.pythonanywhere.com/

"""
    Jogo do Tesouro Inca

"""

__author__ = "Rafael Ris-Ala (rafaelrisala@ufrj.br)"

class JogoTesouroInca:
    """ Representa o Jogo Principal """
    def inicia(self):
        """ Inicia a construção do jogo"""
        self.cena_do_templo = "Templo do tesouro Inca"
        print("Descrição:", self.cena_do_templo)
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoTesouroInca()
    jogo.inicia()