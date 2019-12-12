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
CART, CAT, BASE, CENA, RECT = f"{IGR}m2k5sv6.png", f"{IGR}ek8oINR.png", f"{IGR}DAUyvBP.jpg", f"{IGR}nkwZCrR.jpg", f"{IGR}92GKogg.png"


class Plataforma(Elemento):
    def __init__(self, imagem, cena, x=0, y=200):
        super().__init__(imagem, cena=cena, w=200, h=400, x=x, y=y)
        self.veiculo = None
        #self.elt.style.transition = "all 1s"
        self.destino = self
        self.nome = "base"
        
    def aporta(self, veiculo):
        self.veiculo = veiculo
        return self.destino
        
    def recebe(self, passageiro):
        passageiro.move(self)
        return self
        
    def embarca(self, passageiro):
        return self.veiculo.recebe(passageiro)
        
    def movimenta(self, veiculo):
        veiculo.move(self.destino)
        self.destino.aporta(veiculo)


class Personagem(Elemento):
    def __init__(self, imagem, destino, cena, x=0, y=0):
        super().__init__(imagem, cena=cena, x=x, y=y, w=80, h=80)
        self.destino = destino
        self.vai = self._move
        
    def move(self, destino):
        self.entra(destino)
        
    def _move(self, evento=None):
        self.destino = self.destino.embarca(self)
        #self.entra(self.destino)
        self.x = 0


class Veiculo(Elemento):
    def __init__(self, imagem, destino, base, x=100, y=0):
        self.nome = "veiculo"
        super().__init__(RECT, cena=base, x=x, y=y, w=100, h=130)
        # self.fundo.entra(self)
        self.fundo = Elemento(RECT, cena=self, x=0, y=0, w=100, h=130)
        frente = Elemento(imagem, cena=self, x=0, y=30)
        self.destino = base.aporta(self)
        
        self.outro = self
        frente.vai = self.mover
        #self.entra = self._entra
        
    def recebe(self, passageiro):
        passageiro.move(self.fundo)
        return self
        
    def embarca(self, passageiro):
        return self.destino.recebe(passageiro)
        
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
        self.cart0 = Veiculo(CART, destino=self.base1, base=self.base0)
        self.cart1 = Veiculo(CART, destino=self.base0, base=self.base1, y=200)
        self.cart0.outro, self.cart1.outro = self.cart1.outro, self.cart0.outro
        #self.cart.entra(self.base0)
        self.gato = Personagem(CAT, destino=self.base0, cena=cena, x= 100)
        cena.vai()
        
        
if __name__ == "__main__":
    Basico()