# mary_shaw.elevador.main.py
# mary_shaw.amanda.main.py
from _spy.vitollino.main import Cena, Elemento, INVENTARIO, STYLE
STYLE.update(width=900, height=650)
PREDIO= "https://i.imgur.com/K7xS3Oa.jpg"
CESTA = "https://i.imgur.com/ouziL1K.png"
Doggie = "https://i.imgur.com/1YbsNfD.png"
class Elevador:
    def __init__(self):
        predio = Cena(PREDIO)
        predio.vai()
        self._sobe_desce = self._desce
        self._entra_sai = self._entra
        self._doggie_sobe_desce = lambda *_:None
        self._doggie_desce = lambda *_:None
        self._doggie_sobe = lambda *_:None
        self.na_cesta = "nada"
        self.cesta = Elemento(CESTA, x=300, y=100,w=180,h=180, cena=predio, vai=self.sobe_desce)
        self.doggie = Elemento(Doggie, x=350, y=80, cena=predio, vai=self.entra_sai)
        
    def sobe_desce(self, *_):
        self.cesta.y = 400
        self._sobe_desce()
        
    def _desce(self, *_):
        self._sobe_desce = self._sobe
        self._doggie_desce()
        self.cesta.elt.style.top = 400
        INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1):
        
    def _sobe(self, *_):
        self._sobe_desce = self._desce
        self._doggie_sobe()
        self.cesta.elt.style.top = 100
        INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="sobe", ponto=0, valor=0, _level=1):
        
    def entra_sai(self, *_):
        self._entra_sai()
        
    def _move_doggie(self, tanto):
        self.doggie.elt.style.top = tanto
        
    def _entra(self, *_):
        self._entra_sai= self._sai
        self._doggie_sobe = lambda:self._move_doggie(100)
        self._doggie_desce = lambda:self._move_doggie(400)
        self.na_cesta="doggie"
        self.doggie.elt.style.left = 300
        INVENTARIO.score(casa="doggie", carta=self.na_cesta, move="entra", ponto=0, valor=0, _level=1):
        
    def _sai(self, *_):
        self._entra_sai= self._entra
        self._doggie_sobe = lambda:None
        self._doggie_desce = lambda:None
        self.na_cesta="nada"
        self.doggie.elt.style.left = 350
        INVENTARIO.score(casa="doggie", carta=self.na_cesta, move="sai", ponto=0, valor=0, _level=1):
        
Elevador()