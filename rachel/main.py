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
IMG_MONSTER =  f"{IGR}DWFOnKO.png"
IMG_DWARF =  f"{IGR}ZJcqxr8.png"
IMG_APPLE =  f"{IGR}a9qsM6a.png"
IMG_BOAT_TO_RIGHT = f"{IGR}vH35dWf.png"
IMG_BOAT_TO_LEFT = f"{IGR}QsryhIQ.png"
CENA = f"{IGR}IugWsGp.jpg"

LEFT_MARGIN = "left_margin"
RIGHT_MARGIN = "right_margin"
MONSTER = "monster"
DWARF = "dwarf"
APPLE = "apple"



class Character(Elemento):
    def __init__(self, image, cena, x=0, y=0, w=60, h=60, name, margin):
        super().__init__(image, cena=cena, x=x, y=y, w=w, h=h)
        self.id = name
        self.state = margin

    def getId(self):
        return self.id

    def getState(self):
        return self.state

    def click(self, boat):
        if (self.state == boat):
            boat.getOut(self)
        else:
            boat.getIn(self)
            

class Boat(Elemento):
    def __init__(self, image, cena, x=100, y=0, left_margin, right_margin):
        super().__init__(image, cena=cena, x=x, y=y)
        self.state = 0
        self.margins = [left_margin, right_margin]
        self.passenger = None

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


    def printStatus(self):
        if (self.passenger != None):
            print("Posição = ", self.margins[self.state].getId(), ", Passageiro = ", self.passenger.getId())
        else:
            print("Posição = ", self.margins[self.state].getId(), ", Passageiro = ", self.passenger)
            
            

class Platform():

    def __init__(self, id):
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
        # Colocar aqui toda a parte que o professor ensinou na aula que está em
        # http://supygirls.pythonanywhere.com/supygirls/gamer/mary_shaw/basico
        self.left_margin = Platform(LEFT_MARGIN)
        self.right_margin = Platform(RIGHT_MARGIN)
        
        self.boat = Boat(IMG_BOAT_TO_RIGHT, self.cena, 100, 0, self.left_margin, self.right_margin)
        self.boat.entra(self.cena)
        
        self.monster = Character(IMG_MONSTER, self.cena, 0, 0, 268, 370, MONSTER, self.left_margin)
        self.dwarf = Character(IMG_DWARF, self.cena, 0, 320, 188, 290, DWARF, self.left_margin)
        self.apple = Character(IMG_APPLE, self.cena, 100, 220, 208, 310, APPLE, self.left_margin)
        
        self.left_margin.put(self.monster)
        self.left_margin.put(self.dwarf)
        self.left_margin.put(self.apple)
        
        self.monster.entra(self.cena)
        self.dwarf.entra(self.cena)
        self.apple.entra(self.cena)
        
        self.cena.vai()
    
        #self.left_margin = Platform(LEFT_MARGIN)
        #self.right_margin = Platform(RIGHT_MARGIN)
        #self.boat = Boat(self.left_margin, self.right_margin)

        #self.monster = Character(MONSTER, self.left_margin)
        #self.dwarf = Character(DWARF, self.left_margin)
        #self.apple = Character(APPLE, self.left_margin)

        #self.left_margin.put(self.monster)
        #self.left_margin.put(self.dwarf)
        #self.left_margin.put(self.apple)
        #self.gameStatus()


        #self.monster.click(self.boat)
        #self.gameStatus()
        #self.boat.click()
        #self.gameStatus()
        #self.monster.click(self.boat)
        #self.gameStatus()
        #self.boat.click()
        #self.gameStatus()
        #self.dwarf.click(self.boat)
        #self.gameStatus()
        #self.boat.click()
        #self.gameStatus()
        #self.dwarf.click(self.boat)
        #self.gameStatus()
        #self.boat.click()
        #self.gameStatus()
        #self.apple.click(self.boat)
        #self.gameStatus()
        #self.boat.click()
        #self.gameStatus()
        #self.apple.click(self.boat)
        #self.gameStatus()


    def gameStatus(self):
        self.left_margin.printStatus()
        self.right_margin.printStatus()
        self.boat.printStatus()
        print("\n")
        
        
        
if __name__ == "__main__":
    Game()