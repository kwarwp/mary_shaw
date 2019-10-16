# mary_shaw.lisa.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca
Nós aventureiros fomos para o Templo Inca em busca de tesouros. 
Chegando lá emcontramos uma longa escada com 5 andares, em cada andar haviam diversas câmaras. 
Ao entrar nas câmaras encontramos tesouros, se a quantidade de tesouros fosse igual a quantidade de aventureiros dividinhamos igualmente, se não deixavamos na câmara.
Contudo quando encontramos um artefato, item de extremo valor, deixamos na câmara pois ele não era divisível.
O problema foi quando encontramos um perigo, ficamos preocupados e um aventureiro saiu, ele ficou com o artefato e tudo que deixamos para trás.
Continuei e ao sair o segundo perigo todos nós deixamos para trás o que tinhamos catado e ficamos sem nada.

"""

class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        print(f"Você coloca {quantidade} tesouro na mochila ")
        self.mochila += quantidade
        print(f"Você fica com {self.mochila} tesouros na mochila ")
        camara.entra()
            
    def sai(self):
        """ sai do templo """
        print("Você sai do templo e guarda os tesouros!")
        self.cabana += self.mochila
        self.mochila - 0
        print(f"Você ficou com {self.cabana} tesouros na cabana!")
        if input("Nova Incursão?")
#class Cabana:
    #def __init__(self):
        #self.

class Camara:
    def __init__(self):
        self.explorador = Explorador()
        self.camaraquantidade = 3

    def entra(self):
        """ entra em uma câmara """
        print("Você entra em uma câmara com tesouros!")
        self.pega(1)
        self.camaraquantidade -= 1
        if self.camaraquantidade:
            self.pega(1)
        else:
            print("Não havia mais tesouros!")
            self.sai()


class TemploInca:
    camara = 3
    def __init__(self):
        # self.camara = Camara()
        self.explorador = Explorador()  # (self) (self.camara)

    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros do Templo Inca")
        self.entra()
        
        
    def entra(self):
        """ entra em uma câmara"""
        print("Você entra em uma câmara com tesouros!")
        if TemploInca.camara:
            TemploInca.camara -= 1        
            self.explorador.pega(1, self)
        else:
            print("Não havia mais tesouros!")
            self.explorador.sai()


if __name__ == "__main__":
    TemploInca().inicia()