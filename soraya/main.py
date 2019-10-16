# mary_shaw.roxanne.main.py
"""
Uma expedição para coletar os tesouros do Templo Inca

Descrição: Uma excursão em busca do tesouro, entrando
em tumbas e abrindo câmaras para pegar tesouros ou 
enfrentar riscos, arriscando os prêmios a cada incursão.
O único local seguro é a cabana fora do templo.
"""

__author__ = "Sávyo V Morais <savyo dot morais at labnet dot nce dot ufrj dot br>"

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
        self.entra()
        
    def entra(self):
        """ entra em uma câmara """
        if TemploInca.camara:
            TemploInca.camara -= 1
            print("Você entrou em uma câmara com tesouros!")
            self.pega(1)
        else:
            print("Você já entrou em todas as câmaras!")
            self.sai()
            
    def sai(self):
        TemploInca.cabana += TemploInca.mochila
        TemploInca.mochila = 0
        print(f"Agora você tem {TemploInca.cabana} itens na sua cabana")
        
        
if __name__ == "__main__":
    TemploInca().inicia()