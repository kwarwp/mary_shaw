# mary_shaw.lisa.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca
Nós aventureiros fomos para o Templo Inca em busca de tesouros. 
Chegando lá emcontramos uma longa escada com 5 andares, em cada andar haviam diversas câmaras. 
Ao entrar nas câmaras encontramos tesouros, se a quantidade de tesouros fosse igual a quantidade de aventureiros dividinhamos igualmente, se não deixavamos na câmara.
Contudo quando encontramos um artefato, item de extremo valor, deixamos na câmara pois ele não era divisível.
O problema foi quando encontramos um perigo, ficamos preocupados e um aventureiro saiu, ele ficou com o artefato e tudo que deixamos para trás.
Continuei e ao sair o segundo perigo todos nós deixamos para trás o que tinhamos catado e ficamos sem nada.

""""

class TemploInca:
    cabana = 0
    mochila = 0
    camara = 3
    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros do Templo Inca")
        
    def entra(self):
        """ entra em uma câmara """
        print("Você entra em uma câmara com tesouros!")
