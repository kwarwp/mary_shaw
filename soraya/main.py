# mary_shaw.roxanne.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca

Descrição: Uma excursão em busca do tesouro, entrando
em tumbas e abrindo câmaras para pegar tesouros ou 
enfrentar riscos, arriscando os prêmios a cada incursão.
O único local seguro é a cabana fora do templo.
"""

__author__ = "Sávyo V. Morais"

class TemploInca:
    cabana = 0
    mochila = 0
    camara = 3
    
    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros o Templo Inca")
        self.entra()
        
    def pega(self, qtd):
        """ coloca o tesouro encontrado na mochila """
        print(f"Você coloca {qtd} tesouro na mochila")
        TemploInca.mochila += qtd
        print(f"Agora você tem {TemploInca.mochila} tesouros na mochila")
        
        TemploInca.camara -= 1
        self.entra()
        
    def entra(self):
        """ entra em uma câmara """
        print("Você entrou em uma câmara com tesouros!")
        if TemploInca.camara:
            self.pega(1)
        
        
if __name__ == "__main__":
    TemploInca().inicia()