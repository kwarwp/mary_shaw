# mary_shaw.rachel.main.py
# Este jogo é um software livre com licensa GPL3 `GPL <http://is.gd/3Udt>`__.
"""
Jogo de Missionários e Canibais
"""
__author__ = "André Vieira"
__version__ = "19.12.04"

from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, INVENTARIO

STYLE["width"] = 900
STYLE["height"] = "600px"
IGR = "https://i.imgur.com/"

CENA = f"{IGR}IugWsGp.jpg"
LEFT_MARGIN = "left_margin"
RIGHT_MARGIN = "right_margin"

IMG_MONSTER =  f"{IGR}eQOoUiz.png"
MONSTER = "monster"
MONSTER_W = 260
MONSTER_H = 247
MONSTER_LEFT_SLOT_X = 0
MONSTER_LEFT_SLOT_Y = 20

IMG_DWARF =  f"{IGR}sLfY1So.png"
DWARF = "dwarf"
DWARF_W = 123
DWARF_H = 221
DWARF_LEFT_SLOT_X = 0
DWARF_LEFT_SLOT_Y = 310

IMG_APPLE =  f"{IGR}XKaUgKW.png"
APPLE = "apple"
APPLE_W = 111
APPLE_H = 113
APPLE_LEFT_SLOT_X = 100
APPLE_LEFT_SLOT_Y = 220

IMG_BOAT_TO_RIGHT = f"{IGR}9eVfl1k.png"
IMG_BOAT_TO_LEFT = f"{IGR}uGo3Btw.png"
BOAT_W = 286
BOAT_H = 106
BOAT_X = 230
BOAT_Y = 410



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
        if (self.state == self.boat):
            self.boat.getOut(self)
            self.entra(self.left_slot)
        else:
            self.boat.getIn(self)
            self.entra(self.boat)
            

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
        if (self.margins[self.state] == character.getState() and self.passenger == None):
            character.state.remove(character)
            self.passenger = character
            character.state = self

    def getOut(self, character):
        character.state = self.margins[self.state]
        character.state.put(character)
        self.passenger = None

    def click(self):
        self.margins[self.state].verify()
        self.state = (self.state + 1) % 2
        self.entra(self.margins[self.state])


    def printStatus(self):
        if (self.passenger != None):
            print("Posição = ", self.margins[self.state].getId(), ", Passageiro = ", self.passenger.getId())
        else:
            print("Posição = ", self.margins[self.state].getId(), ", Passageiro = ", self.passenger)
            
            

class Platform(Elemento):

    def __init__(self, image, cena, x=0, y=0, w=400, h=800, id):
        super().__init__(image, cena=cena, x=x, y=y, w=w, h=h)
        self.id = id
        self.place = {
            MONSTER : False,
            DWARF : False,
            APPLE : False
        }

    def getId(self):
        return self.id

    def put(self, character):
        self.place[character.getId()] = True
        character.entra(self)

    def remove(self, character):
        if (self.place[character.getId()] == True):
            self.place[character.getId()] = False

    def verify(self):
        print("VERIFY")
        if (self.place[MONSTER] == True and self.place[DWARF] == True):
            print("Fim de jogo: O monstro comeu o anão!")
        if (self.place[DWARF] == True and self.place[APPLE] == True):
            print("Fim de jogo: O anão comeu a maçã!")

    def printStatus(self):
        print("Margem ", self.id, ": ", self.place)
        
        
        
class Game():
    def __init__(self):
        self.cena = Cena(CENA)
        
        self.left_margin = Platform(None, self.cena, 0, 0, 300, 800, LEFT_MARGIN)
        self.left_margin.entra(self.cena)
        
        self.right_margin = Platform(None, self.cena, 600, 0, 300, 800, RIGHT_MARGIN)
        self.right_margin.entra(self.cena)
        
        self.boat = Boat(IMG_BOAT_TO_RIGHT, self.cena, BOAT_X, BOAT_Y, BOAT_W, BOAT_H, self.left_margin, self.right_margin)
        self.boat.entra(self.cena)
        
        self.monster_left_slot = Platform(None, self.cena, MONSTER_LEFT_SLOT_X, MONSTER_LEFT_SLOT_Y, MONSTER_W, MONSTER_H,"left")
        self.dwarf_left_slot = Platform(None, self.cena,DWARF_LEFT_SLOT_X, DWARF_LEFT_SLOT_Y, DWARF_W, DWARF_H,"left")
        self.apple_left_slot = Platform(None, self.cena, APPLE_LEFT_SLOT_X, APPLE_LEFT_SLOT_Y, APPLE_W, APPLE_H,"left")
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
            DWARF_LEFT_SLOT_X, DWARF_LEFT_SLOT_Y, 
            DWARF_W, DWARF_H, 
            DWARF, 
            self.left_margin, 
            self.boat)
        self.apple = Character(
            IMG_APPLE, 
            self.cena, 
            self.apple_left_slot,
            APPLE_LEFT_SLOT_X, APPLE_LEFT_SLOT_Y, 
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