#===========================================================================
# TESOURO INCA
#===========================================================================
''' UMA EXPEDICAO PARA COLETAR OS TESOUROS DEO TEMPLO INCA '''
#===========================================================================
#===========================================================================
#===========================================================================
__author__ = "Pablo LV"
#===========================================================================
#===========================================================================
class TemploInca:
    cabana = 0
    mochila = 0
    TOTAL_CAMARAS = 3
    camara_atual = 0
    #-----------------------------------------------------------------------
    def inicia(self):
        print("Uma Expedicao para COletar os Tesouros do Templo Inca")
        self.entra()
    #-----------------------------------------------------------------------
    def entra(self):
        TemploInca.camara_atual = TemploInca.camara_atual + 1
        #if TemploInca.TOTAL_CAMARAS == 0:
        if TemploInca.camara_atual > TemploInca.TOTAL_CAMARAS:
            print("\nJa nao há mais Camaras...!!!")
            self.sai()
        else:
            print("\nENTRANDO PARA CAMARA ", TemploInca.camara_atual)
            #print("-----------------------------")
            #print(f"Vocé entra em uma camara {TemploInca.camara_atual} do Templo")
            self.pega(1)
    #-----------------------------------------------------------------------
    def sai(self):
        print("\nVocé sai do Templo e guarda os Tesouros")
        TemploInca.cabana = TemploInca.mochila
        TemploInca.mochila = 0
        print(f"Voce fica com {TemploInca.cabana} tesouros na cabana")
        print(f"\nFim do Jogo")
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------
    def pega(self, quantidade):
        print(f"Voce coloca {quantidade} tesouro na mochila")
        TemploInca.mochila = TemploInca.mochila + quantidade
        print(f"Voce fica com {TemploInca.mochila} tesouros na mochila")
        self.entra()
    #-----------------------------------------------------------------------
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
if __name__ == "__main__":
    TemploInca().inicia()
    #print(JogoTesouroInca,JogoTesouroInca())
