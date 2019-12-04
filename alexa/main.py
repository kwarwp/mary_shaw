# mary_shaw.alexa.main.py
# mary_shaw.amanda.main.py
# mary_shaw.basico.main.py
# Autor: Lorena, Horty e Marilia
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
    def __init__(self,imagem, cena, x=0, y=200):
        super().__init__(imagem, cena=cena, x=x, y=y)
        
    def move(self, evento = None)
        #self.elt.style.transition = "all"
        
class Personagen(Elemento):
    def __init__(self,imagem, cena):
        pass

class Veiculo(Elemento):
    def __init__(self,imagem, cena):
        pass



class Basico:
    def __init__(self):
        self.cena = cena = Cena(CENA)
        self.base0 = Elemento(BASE, cena=cena, x=200, y=200, w=100,h=100)
        self.base1 = Elemento(BASE, cena=cena, x=700, y=200, w=100,h=100)
        
        self.gato = Elemento(CAT, cena=cena, x=700, y=200,w=60,h=60)
        self.cart = Elemento(CART, cena=cena, x=600, y=200,w=90,h=90)
        cena.vai()
        
        
if __name__ == "__main__":
    Basico()