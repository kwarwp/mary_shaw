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
    def __init__(self, imagem, cena, x=0, y=200):
        super().__init__(imagem, cena=cena, w=200, h=400, x=x, y=y)
        #self.elt.style.transition = "all 1s"
        self.destino = self
        self.nome = "base"
        
    def movimenta(self, destino):
        destino.move(self.destino)


class Personagem(Elemento):
    def __init__(self, imagem, destino, cena, x=0, y=0):
        super().__init__(imagem, cena=cena, x=x, y=y, w=60, h=60)
        self.destino = destino
        self.vai = self.move
        
    def move(self, evento=None):
        self.entra(self.destino)
        self.x = 0


class Veiculo(Elemento):
    def __init__(self, imagem, destino, cena, x=100, y=0):
        self.nome = "veiculo"
        super().__init__(imagem, cena=cena, x=x, y=y)
        # self.fundo.entra(self)
        self.fundo = Elemento(imagem, cena=self, x=0, y=0)
        frente = Elemento(imagem, cena=self, x=0, y=0)
        self.destino = destino
        self.outro = self
        frente.vai = self.mover
        #self.entra = self._entra
        
    def mover(self, evento=None):
        self.do_move()
        self.outro.do_move()
        
    def do_move(self, evento=None):
        self.destino.movimenta(self)
        
    def move(self, destino):
        self.entra(destino)
        self.destino = destino
        
    def movimenta(self, destino):
        destino.move(self)


class Basico:
    def __init__(self):
        self.cena = cena = Cena(CENA)
        self.base0 = Plataforma(BASE, x=100, cena=cena)
        self.base1 = Plataforma(BASE, x=500, cena=cena)
        self.base0.destino, self.base1.destino = self.base1, self.base0 
        self.cart0 = Veiculo(CART, destino=self.base1, cena=self.base0)
        self.cart1 = Veiculo(CART, destino=self.base0, cena=self.base1, y=200)
        self.cart0.outro, self.cart1.outro = self.cart1.outro, self.cart0.outro
        #self.cart.entra(self.base0)
        self.gato = Personagem(CAT, destino=self.cart0.fundo, cena=cena, x= 100)
        cena.vai()
        
        
if __name__ == "__main__":
    Basico()