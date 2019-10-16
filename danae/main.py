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
    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros do Templo Inca")
        self.entra()
        
    def entra(self):
        """ entra em uma câmara"""
        print("Você entra em uma câmara com tesouros!")
        if TemploInca.camara:
            TemploInca.camara -= 1        
            self.pega(1)
        else:
            print("Não havia mais tesouros!")
            self.sai()
            
    def sai(self):
        """ sai do templo """
        print("Você sai do templo e guarda os tesouros!")
        TemploInca.cabana, TemploInca.mochila = TemploInca.mochila, 0
        print(f"Você ficou com {TemploInca.cabana} tesouros na cabana!")
            
            
    def pega(self, quantidade):
        """ coloca um tesouro na mochila """
        print(f"Você coloca {quantidade} tesouro na mochila ")
        TemploInca.mochila += quantidade
        print(f"Você fica com {TemploInca.mochila} tesouros na mochila ")
        self.entra()


if __name__ == "__main__":
    TemploInca().inicia()


