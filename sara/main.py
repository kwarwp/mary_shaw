# mary_shaw.rachel.main.py
# Este jogo é um software livre com licensa GPL3 `GPL <http://is.gd/3Udt>`__.
"""
Jogo de Missionários e Canibais
"""
__author__ = "André Vieira"
__version__ = "19.12.04"

from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, INVENTARIO

DEBUG = False
#DEBUG = True

STYLE["width"] = 900
STYLE["height"] = "600px"
IGR = "https://i.imgur.com/"

CENA = f"{IGR}IugWsGp.jpg"

LEFT_MARGIN = "left_margin"
LEFT_MARGIN_X = 0
LEFT_MARGIN_Y = 0
LEFT_MARGIN_W = 510
LEFT_MARGIN_H = 800

RIGHT_MARGIN = "right_margin"
RIGHT_MARGIN_X = 500
RIGHT_MARGIN_Y = 0
RIGHT_MARGIN_W = 510
RIGHT_MARGIN_H = 800

IMG_MONSTER =  f"{IGR}eQOoUiz.png"
MONSTER = "monster"
MONSTER_W = 260
MONSTER_H = 247
MONSTER_LEFT_SLOT_X = 0
MONSTER_LEFT_SLOT_Y = 50
MONSTER_RIGHT_SLOT_X = 15
MONSTER_RIGHT_SLOT_Y = 50

IMG_DWARF =  f"{IGR}sLfY1So.png"
DWARF = "dwarf"
DWARF_W = 123
DWARF_H = 221
DWARF_LEFT_SLOT_X = 20
DWARF_LEFT_SLOT_Y = 330
DWARF_RIGHT_SLOT_X = 250
DWARF_RIGHT_SLOT_Y = 120

IMG_APPLE =  f"{IGR}XKaUgKW.png"
APPLE = "apple"
APPLE_W = 111
APPLE_H = 113
APPLE_LEFT_SLOT_X = 150
APPLE_LEFT_SLOT_Y = 310
APPLE_RIGHT_SLOT_X = 150
APPLE_RIGHT_SLOT_Y = 310

IMG_BOAT_TO_RIGHT = f"{IGR}9eVfl1k.png"
IMG_BOAT_TO_LEFT = f"{IGR}uGo3Btw.png"
BOAT_W = 286
BOAT_H = 106
BOAT_LEFT_SLOT_X = 230
BOAT_LEFT_SLOT_Y = 410
BOAT_RIGHT_SLOT_X = 0
BOAT_RIGHT_SLOT_Y = 410



class Character(Elemento):
    def __init__(self, image, cena, left_slot, x=0, y=0, w=60, h=60, name, margin, boat):
        super().__init__(image, cena=cena, x=x, y=y, w=w, h=h)
        self.id = name
        self.state = margin
        self.boat = boat
        self.vai = self.click
        self.left_slot = left_slot

    def getId(self):
        return self.id

    def getState(self):
        return self.state

    def click(self, evento=None):
        if(DEBUG):
            temp_state = self.state
            self.state.printStatus()
        
        if (self.state == self.boat):
            self.boat.getOut(self)
        else:
            self.boat.getIn(self)            
            
        if(DEBUG):
            temp_state.printStatus()
            self.state.printStatus()
            

class Boat(Elemento):
    def __init__(self, image, cena, x=100, y=0, w=60, h=60, left_margin, right_margin):
        super().__init__(image, cena=cena, x=x, y=y, w=w, h=h)
        self.state = 0
        self.margins = [left_margin, right_margin]
        self.passenger = None
        self.vai = self.click

    def getState(self):
        return self.margins[self.state]

    def getIn(self, character):
        if (self.margins[self.state] == character.getState() ):
            character.state.remove(character)
            self.passenger = character
            character.state = self
            character.entra(self)

    def getOut(self, character):
        character.state = self.margins[self.state]
        character.state.put(character)
        self.passenger = None

    def click(self, evento=None):
        if(DEBUG):
            self.printStatus()
            
        self.margins[self.state].verify()
        self.state = (self.state + 1) % 2
        self.entra(self.margins[self.state].getBoatSlot())
        
        if(DEBUG):
            self.printStatus()

    def printStatus(self):
        if (self.passenger != None):
            input(f"Posição = {self.margins[self.state].getId()}, Passageiro = {self.passenger.getId()}")
        else:
            input(f"Posição = {self.margins[self.state].getId()}, Passageiro = {self.passenger}")
            
            

class Platform(Elemento):

    def __init__(self, image, cena, x=0, y=0, w=400, h=800, id, monster_slot, dwarf_slot, apple_slot, boat_slot):
        super().__init__(image, cena=cena, x=x, y=y, w=w, h=h)
        self.id = id
        self.place = {
            MONSTER : False,
            DWARF : False,
            APPLE : False
        }
        self.monster_slot = monster_slot
        self.dwarf_slot = dwarf_slot
        self.apple_slot = apple_slot
        self.boat_slot = boat_slot
        self.ator = [(MONSTER,self.monster_slot),(DWARF,self.dwarf_slot),(APPLE,self.apple_slot)]        
        

    def getId(self):
        return self.id
        
    def getBoatSlot(self):
        return self.boat_slot

    def put(self, character):
        self.place[character.getId()] = True
        id = character.getId()
        for ch in self.ator:
            a , b = ch
            if id == a:
                character.entra(b)
                break
        

    def remove(self, character):
        if (self.place[character.getId()] == True):
            self.place[character.getId()] = False

    def verify(self):    
        cond = [(self.place[MONSTER] == True and self.place[DWARF] == True and self.place[APPLE] == False,"Fim de jogo: O monstro comeu o anão!"),
                (self.place[DWARF] == True and self.place[APPLE] == True and self.place[MONSTER] == False,"Fim de jogo: O anão comeu a maçã!"),
                (self.place[DWARF] == True and self.place[APPLE] == True and self.place[MONSTER] == True and self.id == RIGHT_MARGIN,"Ahhh! Você conseguiu!")]
        
        for cd in cond:
            a , b = cd 
            if a:
                input(b)
                break
        

    def printStatus(self):
        input(f"Margem {self.id}: Monstro={self.place[MONSTER]}, Anão={self.place[DWARF]}, Maçã={self.place[APPLE]}")
        
        
        
class Game():
    def __init__(self):
        self.cena = Cena(CENA)
        
        self.monster_left_slot = Elemento(None, cena=self.cena, x=MONSTER_LEFT_SLOT_X, y=MONSTER_LEFT_SLOT_Y, w=MONSTER_W, h=MONSTER_H)
        self.dwarf_left_slot = Elemento(None, cena=self.cena, x=DWARF_LEFT_SLOT_X, y=DWARF_LEFT_SLOT_Y, w=DWARF_W, h=DWARF_H)
        self.apple_left_slot = Elemento(None, cena=self.cena, x=APPLE_LEFT_SLOT_X, y=APPLE_LEFT_SLOT_Y, w=APPLE_W, h=APPLE_H)
        self.boat_left_slot = Elemento(None, cena=self.cena, x=BOAT_LEFT_SLOT_X, y=BOAT_LEFT_SLOT_Y, w=BOAT_W, h=BOAT_H)
        self.left_margin = Platform(None, self.cena, LEFT_MARGIN_X, LEFT_MARGIN_Y, LEFT_MARGIN_W, LEFT_MARGIN_H, LEFT_MARGIN, self.monster_left_slot, self.dwarf_left_slot, self.apple_left_slot, self.boat_left_slot)
        self.monster_left_slot.entra(self.left_margin)
        self.dwarf_left_slot.entra(self.left_margin)
        self.apple_left_slot.entra(self.left_margin)
        self.boat_left_slot.entra(self.left_margin)
        self.left_margin.entra(self.cena)
        
        self.monster_right_slot = Elemento(None, cena=self.cena, x=MONSTER_RIGHT_SLOT_X, y=MONSTER_RIGHT_SLOT_Y, w=MONSTER_W, h=MONSTER_H)
        self.dwarf_right_slot = Elemento(None, cena=self.cena, x=DWARF_RIGHT_SLOT_X, y=DWARF_RIGHT_SLOT_Y, w=DWARF_W, h=DWARF_H)
        self.apple_right_slot = Elemento(None, cena=self.cena, x=APPLE_RIGHT_SLOT_X, y=APPLE_RIGHT_SLOT_Y, w=APPLE_W, h=APPLE_H)
        self.boat_right_slot = Elemento(None, cena=self.cena, x=BOAT_RIGHT_SLOT_X, y=BOAT_RIGHT_SLOT_Y, w=BOAT_W, h=BOAT_H)
        self.right_margin = Platform(None, self.cena, RIGHT_MARGIN_X, RIGHT_MARGIN_Y, RIGHT_MARGIN_W, RIGHT_MARGIN_H, RIGHT_MARGIN, self.monster_right_slot, self.dwarf_right_slot, self.apple_right_slot, self.boat_right_slot)
        self.monster_right_slot.entra(self.right_margin)
        self.dwarf_right_slot.entra(self.right_margin)
        self.apple_right_slot.entra(self.right_margin)
        self.boat_right_slot.entra(self.right_margin)
        self.right_margin.entra(self.cena)
        
        self.boat = Boat(IMG_BOAT_TO_RIGHT, self.cena, 0, 0, BOAT_W, BOAT_H, self.left_margin, self.right_margin)
        self.boat.entra(self.boat_left_slot)
        
        self.monster = Character(
            IMG_MONSTER, 
            self.cena, 
            self.monster_left_slot, 
            0, 0, 
            MONSTER_W, MONSTER_H, 
            MONSTER, 
            self.left_margin, 
            self.boat)
        self.dwarf = Character(
            IMG_DWARF, 
            self.cena, 
            self.dwarf_left_slot,
            0, 0, 
            DWARF_W, DWARF_H, 
            DWARF, 
            self.left_margin, 
            self.boat)
        self.apple = Character(
            IMG_APPLE, 
            self.cena, 
            self.apple_left_slot,
            0, 0, 
            APPLE_W, APPLE_H, 
            APPLE, 
            self.left_margin, 
            self.boat)
        
        self.left_margin.put(self.monster)
        self.left_margin.put(self.dwarf)
        self.left_margin.put(self.apple)
        
        self.cena.vai()


    def gameStatus(self):
        self.left_margin.printStatus()
        self.right_margin.printStatus()
        self.boat.printStatus()
        print("\n")
        
        
        
if __name__ == "__main__":
    Game()