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

M0 = "margin0"
M1 = "margin1"
MONSTER = "monster"
DWARF = "dwarf"
APPLE = "apple"


class Plataforma(Elemento):
    self.id = ""
    self.place = {
        MONSTER:"",
        DWARF:"",
        APPLE:""
    }
    
    #def __init__(self, imagem, cena, id):
    def __init__(self, id):
        self.id = id
        
    def getId(self):
        return self.id
        
    def put(self, person):
        self.place[person.getId()] = true
        
    def remove(self, person):
        if (self.place[person] == true):
            self.place[person] = false
        
    

class Personagem(Elemento):
    self.id = ""
    self.state = ""
    
    #def __init__(self, imagem, cena, name):
    def __init__(self, name, margin):
        self.id = name
        self.state = margin
        
    def getId(self):
        return self.id
        
    def click(self):
        pass



class Veiculo(Elemento):
    self.id
    self.state = ""

    #def __init__(self, imagem, cena, margin):
    def __init__(self, margin):
        self.state = margin
        
    def getId(self):
        return self.id
        
    def getState(self):
        return self.state
        
    def moveTo(self, margin):
        state = margin



class Basico:
    def __init__(self):
        self.m0 = Plataforma(M0)
        self.m1 = Plataforma(M1)
        self.boat = Veiculo(self.m0)
        
        self.monster = Personagem(MONSTER, self.m0)
        self.dwarf = Personagem(DWARF, self.m0)
        self.apple = Personagem(APPLE, self.m0)
        
        self.m0.put(self.monster)
        self.m0.put(self.dwarf)
        self.m0.put(self.apple)
        
        print("Teste ", "Uhuuu")
        #self.cena = cena = Cena(CENA)
        #self.base0 = Elemento(BASE, cena=cena)
        #self.gato = Elemento(CAT, cena=cena)
        #self.cart = Elemento(CART, cena=cena)
        #cena.vai()
        
        
if __name__ == "__main__":
    Basico()