# mary_shaw.danae.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca
 --Relato:
 fui e voltei rico
"""
__author__ = "Carlo E T Oliveira <carlo at nce ufrj br>"


class TemploInca:
    cabana = 0
    mochila = 0
    camara = 3
    cabana = 0
    
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
        self.entra()
        
    def sair(self):
        """ sair do jogo e acumular na cabana com o que há na mochila """
        print("sair do jogo e acumular na cabana com o que há na mochila")
        self.cabana += self.mochila


if __name__ == "__main__":
    TemploInca().inicia()


