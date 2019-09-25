# mary_shaw.parisa.main.py
#site: http://supygirls.pythonanywhere.com/

#Módulos em python: from roxanne.main import JogoTesouroInca as JogoCarlo

"""
     Jogo do Tesouro Inca

"""
__author__ = "Fernanda Prazeres (fprazeres@dcc.ufrj.br)"  
#camelcase (nome com letra maiúscula e minúscula) ("letra de camelo") = só se usa em nome de classe

class JogoTesouroInca:
    """ Representa o Jogo principal """ #documentação = string apos 2 pontos, pode ser executado. 
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo = "Templo do Tesouro Inca"
        print("Descrição:",self.cena_do_templo,__name__)
        
if __name__ == "__main__":
    jogo = JogoTesouroInca() 
    outro_jogo = JogoTesouroInca()
    jogo.inicia()
    
    
    
    

