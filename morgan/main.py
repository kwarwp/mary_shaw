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
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros do Templo Inca")
        self.entra()
        
    def entra(self):
        """ entra em uma câmara"""
        print("Você entra em uma câmara com tesouros!")
        TemploInca.camara -= 1        
        if TemploInca.camara:
            self.pega(1)
            
    def pega(self, quantidade):
        """ coloca um tesouro na mochila """
        print(f"Você coloca {quantidade} tesouro na mochila ")
        TemploInca.mochila += quantidade
        print(f"Você fica com {TemploInca.mochila} tesouros na mochila ")
        print("Você coloca %s tesouro na mochila" % quantidade)

self.entra()

if __name__ == "__main__":
    TemploInca().inicia()
