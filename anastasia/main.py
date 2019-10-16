# mary_shaw.anastasia.main.py

"""
    Uma Ewexpediçaõ para coletar os tesouros do Templo Inca
    --Relato:
    Fomos explorar um tempo Inca onde havia câmaras com tesouros. Acampamos perto do templo onde fomos 
    guardando os tesouros. Fizemos diversas incursões mas tivemos que enfrentar diversos perigos. Voltei com meu tesouro
    mas nem todos tiveram a mesma sorte.
"""

__author__ = "Claudia L R Motta <claudiam at nce.ufrj.br>"


class TemploInca:
    cabana = 0
    mochila = 0
    camara = 3
    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros do Templo Inca")
        self.entra(1)
        
    def entra(self):
        """ entra em uma câmara"""
        print("Você entra em uma câmara com tesouros!")
        self.pega(1)
        
    def pega(self, quantidade)
        """ Coloca um tesouro na mochila """ 
        print(f" Você coloca {quantidade} tesouro na mochila")
        
        
if __name__ == "__main__":
    TemploInca().inicia()
        