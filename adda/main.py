# mary_shaw.adda.main.py
"""
Uma expedição para coletar os tesouros do templo Inca
--Relato:
Entramos em uma tumba, percorremos câmaras que continham tesouros e perigos 
e podiamos escolher entre ficar ou sair.
"""
__autor__ = "Marília Campos Galvão"

class TemploInca:
    cabana = 0
    mochila = 0
    camara = 3
    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros de um templo Inca")
        self.entra()
        
    def entra(self):
        """ entra em uma câmera"""
        print("O que existe nela")
        self.pega(1)
        
    def pega(self, quantidade):
        """ guarda um tesouro na machila """
        print(f"Você coloca {quantidade} tesouro na mochila" )
        TemploInca.mochila += quantidade
        print(f"Você fica com {TemploInca.mochila} tesouros na mochila")
        
if __name__ == "__main__":
    TemploInca().inicia()