# mary_shaw.morgan.main.py
# http://supygirls.python.pythonanywhere.com/
from _spy.vitollino.main import Cena
IMAGEM_DO_TEMPLO = "https://i.imgur.com/rY28mtM.jpg"

"""
Nossa aventura em busca do tesouro inca consiste no descobrimento do tesouro inca 
"""

__author__ = "Rafael Ris-Ala (rafaelrisala@ufrj.br)"


class TemploInca:
    cabana = 0
    mochila = 0
    camara = 3
    def inicia(self):
        """inicia a exploração"""
        print("Uma expedição para coletar os tesouros do Templo Inca")
        self.entra()
        
    def entra(self):
        """entra em uma câmara"""
        print("Você entra em uma câmara com tesouros!")
        self.pega(1)
        #string formatada = f
        #{} chama a quantidade
    def pega(self, quantidade):
        """Você coloca o tesouro na mochila"""
        print(f"Você coloca {quantidade} " %s "tesouro na mochila") %s quantidade
        
if __name__ == "__main__":
    TemploInca().inicia()