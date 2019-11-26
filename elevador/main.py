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
        self.cesta = Elemento(CESTA, x=300, y=100,w=180,h=180, cena=predio, vai=self.sobe_desce)
        self.doggie = Elemento(Doggie, x=350, y=80, cena=predio, vai=self.entra_sai)
        
    def sobe_desce(self, *_):
        self.cesta.y = 400
        self._sobe_desce()
        INVENTARIO.send(data=dict(elevador=))
        
    def _desce(self, *_):
        self._sobe_desce = self._sobe
        self._doggie_desce()
        self.cesta.elt.style.top = 400
        INVENTARIO.send(data=dict(elevador="desce", cesta=self.na_cesta))
        
    def _sobe(self, *_):
        self._sobe_desce = self._desce
        self._doggie_sobe()
        self.cesta.elt.style.top = 100
        
    def entra_sai(self, *_):
        self._entra_sai()
        
    def _move_doggie(self, tanto):
        self.doggie.elt.style.top = tanto
        
    def _entra(self, *_):
        self._entra_sai= self._sai
        self._doggie_sobe = lambda:self._move_doggie(100)
        self._doggie_desce = lambda:self._move_doggie(400)
        self.doggie.elt.style.left = 300
        
    def _sai(self, *_):
        self._entra_sai= self._entra
        self._doggie_sobe = lambda:None
        self._doggie_desce = lambda:None
        self.doggie.elt.style.left = 350
        
Elevador()