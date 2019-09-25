# mary_shaw.parisa.main.py
#site: http://supygirls.pythonanywhere.com/

#Módulos em python: from roxanne.main import JogoTesouroInca as JogoCarlo

"""
     Jogo do Tesouro Inca

"""

from _spy.vitollino.main import Cena  #importa módulo da biblioteca gráfica
IMAGEM_DO_TEMPLO = "https://i.imgur.com/8puEH1k.jpg"   #constante em python é com letra maiúscula 

__author__ = "Fernanda Prazeres (fprazeres@dcc.ufrj.br)"  
#camelcase (nome com letra maiúscula e minúscula) ("letra de camelo") = só se usa em nome de classe


class JogoTesouroInca: #define classe
    """ Representa o Jogo principal """ #documentação = string após 2 pontos, pode ser executado. 
    
    def __init__(self):   #classe tem um atributo 
        "Constroi a cena "
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO) # atributo

    def inicia(self): #define comportamento
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
          
#self.cena_do_templo = "Templo do Tesouro Inca"
# print("Descrição:",self.cena_do_templo,__name__)
      
#PASS = comando que passa e não lê onde não tem comando, logo não dá erro.
        
if __name__ == "__main__":
    jogo = JogoTesouroInca() 
    outro_jogo = JogoTesouroInca()
    jogo.inicia() #instancia a class
    
    
    
    

