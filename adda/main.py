# mary_shaw.adda.main.py
# http://supygirls.pythonanywhere.com/
"""
   Tesouro Inca
   
"""
__author__= "Marilia Campos Galvao"

#camel case só se usa em nome de classe
class JogoTesouroInca:
    """ Representa o Jogo principal """
    def inicia(self):
        """ Inicia a construção do jogo """
        self.cena_do_templo = "Templo do tesouro Inca"
        print("Descrição:",self.cena_do_templo, __name__)
        
        
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    outro_jogo = JogoTesouroInca()
    jogo.inicia()