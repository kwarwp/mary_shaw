# mary_shaw.basico.main.py
# Este jogo é um software livre com licensa GPL3 `GPL <http://is.gd/3Udt>`__.
"""
Demonstração de elementos para jogo de transporte
"""
__author__ = "Carlo Oliveira"
__version__ = "19.12.03"
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE, INVENTARIO

STYLE["width"]=900
STYLE["height"]= "600px"
IGR = "https://i.imgur.com/"
CART, CAT, BASE, CENA = f"{IGR}m2k5sv6.png", f"{IGR}ek8oINR.png", f"{IGR}DAUyvBP.jpg", f"{IGR}nkwZCrR.jpg"


class Plataforma(Elemento):
    def __init__(self, imagem, cena, x=0, y=400):
        super().__init__(imagem, cena=cena, x=x, y=y)
        #self.elt.style.transition = "all 1s"
        pass


class Personagem(Elemento):
    def __init__(self, imagem, veiculo, cena, x=0, y=400):
        super().__init__(imagem, cena=cena, x=x, y=y)
        self.veiculo = veiculo
        self.vai = self.move
        
    def move(self, evento=None):
        self.entra(self.veiculo)


class Veiculo(Elemento):
    def __init__(self, imagem, cena, x=0, y=400):
        super().__init__(imagem, cena=cena, x=x, y=y)


class Basico:
    def __init__(self):
        self.cena = cena = Cena(CENA)
        self.base0 = Plataforma(BASE, x=100, cena=cena)
        self.base1 = Plataforma(BASE, x=500, cena=cena)
        self.cart = Veiculo(CART, x=100, cena=cena)
        self.gato = Personagem(CAT, veiculo=self.cart, cena=cena)
        cena.vai()
        
        
if __name__ == "__main__":
    Basico()