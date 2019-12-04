# mary_shaw.adda.main.py
"""
Uma expedição para coletar os tesouros do templo Inca
--Relato:
Entramos em uma tumba, percorremos câmaras que continham tesouros e perigos 
e podiamos escolher entre ficar ou sair.
"""
__autor__ = "Marília Campos Galvão"

__version__ = "19.12.03"
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE, INVENTARIO

STYLE["width"]=900
STYLE["height"]= "600px"
IGR = "https://i.imgur.com/"
CART, CAT, BASE, CENA = f"{IGR}m2k5sv6.png", f"{IGR}ek8oINR.png", f"{IGR}DAUyvBP.jpg", f"{IGR}nkwZCrR.jpg"

class Personagen(Elemento):
    def __init__(self,imagem, cena, x=0, y=400):
        super().__init__(imagem, cena=cena, x=x, y=y)
        self.veiculo = destino
        self.vai = self.move
    

class Veiculo(Elemento):
    def __init__(self,imagem, destino, cena, x=0, y=400):
        super().__init__(imagem, cena=cena, x=x, y=y)
        self.nome = "veiculo"


class Plataforma(Elemento):
    def __init__(self,imagem, cena):
    #super().__init__(???/)
        pass


class Basico:
    def __init__(self):
        self.cena = cena = Cena(CENA)
        self.base0 = Elemento(BASE, y=100, x=400, cena=cena)
        self.base1 = Elemento(BASE, y=500, x=400, cena=cena)
        self.gato = Elemento(CAT, x=400, cena=cena)
        self.gato1 = Elemento(CAT, x=350, cena=cena)
        self.gato2 = Elemento(CAT, x=450, cena=cena)
        self.cart = Elemento(CART, y=100, x=300, cena=cena)
        self.cart1 = Elemento(CART, y=500, x=500, cena=cena)
        cena.vai()
        
        
if __name__ == "__main__":
    Basico()