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
#===========================================================================
#===========================================================================
#===========================================================================
class Explorador:
    """ explora o templo inca"""
    def __init__(self):  # (self, camara)
        self.mochila = 0
        self.cabana = 0
        # self.camara = camara
            
    def pega(self, quantidade, camara):
        """ coloca um tesouro na mochila """
        print(f"Você coloca {quantidade} tesouro na mochila ")
        self.mochila += quantidade
        print(f"Você fica com {self.mochila} tesouros na mochila ")
        camara.entra()
            
    def sai(self):
        """ sai do templo """
        print("Você sai do templo e guarda os tesouros!")
        self.cabana, self.mochila = self.mochila, 0
        print(f"Você ficou com {self.cabana} tesouros na cabana!")

#===========================================================================
class Camara:
    '''def __init__(self):
        self.qualquercoisa = None
'''
    def entra(self):
        """ entra em uma câmara"""
        print("Você entra em uma câmara com tesouros!")
        EXP = Explorador()
        if TemploInca.camara:
            TemploInca.camara -= 1
            EXP.pega(1,self)
            #self.explorador.pega(1, self)
        else:
            print("Não havia mais tesouros!")
            EXP.sai()
            #self.explorador.sai()

#===========================================================================
class TemploInca:
    camara = 3
    def __init__(self):
        # self.camara = Camara()
        self.explorador = Explorador()  # (self) (self.camara)

    def inicia(self):
        """ inicia a exploração """
        print("Uma expedição para coletar os tesouros do Templo Inca")
        cmr = Camara()
        cmr.entra()



if __name__ == "__main__":
    TemploInca().inicia()











'''
class Explorador:
    #-----------------------------------------------------------------------
    def __init__(self):
        self.mochila = 0
    #-----------------------------------------------------------------------
    def pega(self, quantidade, camara):
        print(f"Voce coloca {quantidade} tesouro na mochila")
        self.mochila = self.mochila + quantidade
        print(f"Voce fica com {self.mochila} tesouros na mochila")
        camara.entra()
    #-----------------------------------------------------------------------
    def sai(self):
        print("\nVocé sai do Templo e guarda os Tesouros")
        TemploInca.cabana = TemploInca.mochila
        TemploInca.mochila = 0
        print(f"Voce fica com {TemploInca.cabana} tesouros na cabana")
        print(f"\nFim do Jogo")
    #-----------------------------------------------------------------------

#===========================================================================
class TemploInca:
    cabana = 0
    explorador = Explorador()
    TOTAL_CAMARAS = 3
    camara_atual = 0
    #-----------------------------------------------------------------------
    def __init__(self):
        self.explorador = Explorador()
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
            self.explorador.pega(1)
    #-----------------------------------------------------------------------
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
if __name__ == "__main__":
    TemploInca().inicia()
    #print(JogoTesouroInca,JogoTesouroInca())
'''