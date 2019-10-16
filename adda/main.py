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
        if TemploInca.camara:
        TemploInca.camara -= 1
            self.pega(1)
        else:
            print(f"A rodada acabou para você, leve suas {Templo.cabana} para cabana")
            self.sai()
            
    def sai(self):
        """ sai do templo """
        Print("Você sai do templo e guarda os tesouros!")
        TemploInca.cabana, TemploInca.mochila = TemploInca.mochila, 0
        
    def pega(self, quantidade):
        """ guarda um tesouro na machila """
        print(f"Você coloca {quantidade} tesouro na mochila" )
        TemploInca.mochila += quantidade
        print(f"Você fica com {TemploInca.mochila} tesouros na mochila")
        self.entra()
        
if __name__ == "__main__":
    TemploInca().inicia()