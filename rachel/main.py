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
MONSTER_OFFSET_X = 0
MONSTER_OFFSET_Y = 0
MONSTER_LEFT_SLOT_X = 0
MONSTER_LEFT_SLOT_Y = 80
MONSTER_RIGHT_SLOT_X = 15
MONSTER_RIGHT_SLOT_Y = 50
MONSTER_PLAT_W = 260
MONSTER_PLAT_H = 327

IMG_DWARF =  f"{IGR}sLfY1So.png"
DWARF = "dwarf"
DWARF_W = 123
DWARF_H = 221
DWARF_OFFSET_X = 60
DWARF_OFFSET_Y = 20
DWARF_LEFT_SLOT_X = 0
DWARF_LEFT_SLOT_Y = 310
DWARF_RIGHT_SLOT_X = 190
DWARF_RIGHT_SLOT_Y = 120
DWARF_PLAT_W = 183
DWARF_PLAT_H = 241

IMG_APPLE =  f"{IGR}XKaUgKW.png"
APPLE = "apple"
APPLE_W = 111
APPLE_H = 113
APPLE_OFFSET_X = 55
APPLE_OFFSET_Y = 140
APPLE_LEFT_SLOT_X = 100
APPLE_LEFT_SLOT_Y = 170
APPLE_RIGHT_SLOT_X = 230
APPLE_RIGHT_SLOT_Y = 280
APPLE_PLAT_W = 161
APPLE_PLAT_H = 258

#IMG_BOAT_TO_RIGHT = f"{IGR}fsOXdlN.png"
#BOAT_H = 353
#BOAT_LEFT_SLOT_Y = 163
#BOAT_RIGHT_SLOT_Y = 163
IMG_BOAT_TO_RIGHT = f"{IGR}9eVfl1k.png"
IMG_BOAT_TO_LEFT = f"{IGR}uGo3Btw.png"
BOAT_W = 286
BOAT_H = 106
BOAT_OFFSET_X = 0
BOAT_OFFSET_Y = 174
BOAT_LEFT_SLOT_X = 230
BOAT_LEFT_SLOT_Y = 236
BOAT_RIGHT_SLOT_X = 0
BOAT_RIGHT_SLOT_Y = 236
BOAT_PLAT_W = 286
BOAT_PLAT_H = 280

""" CONSTANTES PARA A TELA DE INÍCIO DO JOGO """

CENA_START = f"{IGR}NyC1rxr.jpg"

IMG_BOTAO_START = f"{IGR}1bmM4Vk.png"
BOTAO_START = "start"
BOTAO_START_W = 256
BOTAO_START_H = 256
BOTAO_START_X = 300
BOTAO_START_Y = 280

""" CONSTANTES PARA A TELA DE INÍCIO DO JOGO """

CENA_END = f"{IGR}sipMMNk.jpg"

IMG_BOTAO_HOME = f"{IGR}pN7aJYM.png"
BOTAO_HOME = "home"
BOTAO_HOME_W = 128
BOTAO_HOME_H = 163
BOTAO_HOME_X = 500
BOTAO_HOME_Y = 390


IMG_BOTAO_RESTART = f"{IGR}HowIM6S.png"
BOTAO_RESTART = "restart"
BOTAO_RESTART_W = 128
BOTAO_RESTART_H = 192
BOTAO_RESTART_X = 650
BOTAO_RESTART_Y = 360

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
    def __init__(self, image, cena, x=100, y=0, w=60, h=60, left_margin, right_margin, left_slot, right_slot, game):
        super().__init__(image, cena=cena, x=x, y=y, w=w, h=h)
        self.state = 0
        self.margins = [left_margin, right_margin]
        self.slots = [left_slot, right_slot]
        self.passengers = [None, None]
        self.vai = self.click
        self.game = game

    def getState(self):
        return self.margins[self.state]

    def getIn(self, character):
        if (self.margins[self.state] == character.getState()):
            if (self.passengers[0] == None):
                self.characterCommit(0, character)
            else:
                if (self.passengers[1] == None):
                    self.characterCommit(1, character)
            
    def characterCommit(self, position, character):
        character.state.remove(character)
        self.passengers[position] = character
        character.state = self
        character.entra(self.slots[self.state])

    def getOut(self, character):
        character.state = self.margins[self.state]
        character.state.put(character)
        if (self.passengers[0] == character):
            self.passengers[0] = None
        else:
            self.passengers[1] = None
        self.margins[self.state].checkFinal()

    def click(self, evento=None):
        if(DEBUG):
            self.printStatus()
            
        if (self.passengers[0] != None or self.passengers[1] != None):
            self.margins[self.state].verify()
            self.verify()
            self.state = (self.state + 1) % 2
            slot = self.margins[self.state].getBoatSlot()
            self.entra(slot)
            if (self.passengers[0] != None):
                self.passengers[0].entra(slot)
            if (self.passengers[1] != None):
                self.passengers[1].entra(slot)
        
        if(DEBUG):
            self.printStatus()
            
    def verify(self):
        crew = []
        if (self.passengers[0] != None):
            crew.append(self.passengers[0].getId())
        if (self.passengers[1] != None):
            crew.append(self.passengers[1].getId())
            
        if (MONSTER in crew and DWARF in crew):
            #input("Fim de jogo: O monstro comeu o anão!")
            self.game.showEndScreen()
        if (DWARF in crew and APPLE in crew):
            #input("Fim de jogo: O anão comeu a maçã!")
            self.game.showEndScreen()
                        
    def printStatus(self):
        if (self.passengers[0] == None):
            pas_zero = None
        else:
            pas_zero = self.passengers[0].getId()
            
        if (self.passengers[1] == None):
            pas_um = None
        else:
            pas_um = self.passengers[1].getId()
        
        input(f"Posição = {self.margins[self.state].getId()}, Passageiro[0] = {pas_zero}, Passageiro[1] = {pas_um}")

            
            

class Platform(Elemento):

    def __init__(self, image, cena, x=0, y=0, w=400, h=800, id, monster_slot, dwarf_slot, apple_slot, boat_slot, game):
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
        self.game = game
        
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
                (self.place[DWARF] == True and self.place[APPLE] == True and self.place[MONSTER] == False,"Fim de jogo: O anão comeu a maçã!")]
        #cond = [(self.place[MONSTER] == True and self.place[DWARF] == True and self.place[APPLE] == False,self.game.showEndScreen()),
        #        (self.place[DWARF] == True and self.place[APPLE] == True and self.place[MONSTER] == False,self.game.showEndScreen())]
        
        for cd in cond:
            a , b = cd 
            if a:
                #input(b)
                self.game.showEndScreen()
                break
                
    def checkFinal(self):
        if (self.place[DWARF] == True and self.place[APPLE] == True and self.place[MONSTER] == True and self.id == RIGHT_MARGIN):
            #input("Ahhh! Você conseguiu!")
            self.game.showEndScreen()

    def printStatus(self):
        input(f"Margem {self.id}: Monstro={self.place[MONSTER]}, Anão={self.place[DWARF]}, Maçã={self.place[APPLE]}")
        

class Botao(Elemento):
    def __init__(self, image, cena, x=0, y=0, w=128, h=128, name, game):
        super().__init__(image, cena=cena, x=x, y=y, w=w, h=h)
        self.id = name
        self.vai = self.click
        self.game = game

    def getId(self):
        return self.id

    def click(self, evento=None):
        if(self.id == "home"):
            self.game.showStartScreen()
        else:
            self.game.showGameScreen()



        
class Game():
    def __init__(self):
        #self.showGameScreen()
        self.showStartScreen()
        
        
    def showGameScreen(self):
        self.cena = Cena(CENA)
        
        self.monster_left_slot = Elemento(None, cena=self.cena, x=MONSTER_LEFT_SLOT_X, y=MONSTER_LEFT_SLOT_Y, w=MONSTER_PLAT_W, h=MONSTER_PLAT_H)
        self.dwarf_left_slot = Elemento(None, cena=self.cena, x=DWARF_LEFT_SLOT_X, y=DWARF_LEFT_SLOT_Y, w=DWARF_PLAT_W, h=DWARF_PLAT_H)
        self.apple_left_slot = Elemento(None, cena=self.cena, x=APPLE_LEFT_SLOT_X, y=APPLE_LEFT_SLOT_Y, w=APPLE_PLAT_W, h=APPLE_PLAT_H)
        self.boat_left_slot = Elemento(None, cena=self.cena, x=BOAT_LEFT_SLOT_X, y=BOAT_LEFT_SLOT_Y, w=BOAT_PLAT_W, h=BOAT_PLAT_H)
        self.left_margin = Platform(None, self.cena, LEFT_MARGIN_X, LEFT_MARGIN_Y, LEFT_MARGIN_W, LEFT_MARGIN_H, LEFT_MARGIN, self.monster_left_slot, self.dwarf_left_slot, self.apple_left_slot, self.boat_left_slot, self)
        self.monster_left_slot.entra(self.left_margin)
        self.dwarf_left_slot.entra(self.left_margin)
        self.apple_left_slot.entra(self.left_margin)
        self.boat_left_slot.entra(self.left_margin)
        self.left_margin.entra(self.cena)
        
        self.monster_right_slot = Elemento(None, cena=self.cena, x=MONSTER_RIGHT_SLOT_X, y=MONSTER_RIGHT_SLOT_Y, w=MONSTER_PLAT_W, h=MONSTER_PLAT_H)
        self.dwarf_right_slot = Elemento(None, cena=self.cena, x=DWARF_RIGHT_SLOT_X, y=DWARF_RIGHT_SLOT_Y, w=DWARF_PLAT_W, h=DWARF_PLAT_H)
        self.apple_right_slot = Elemento(None, cena=self.cena, x=APPLE_RIGHT_SLOT_X, y=APPLE_RIGHT_SLOT_Y, w=APPLE_PLAT_W, h=APPLE_PLAT_H)
        self.boat_right_slot = Elemento(None, cena=self.cena, x=BOAT_RIGHT_SLOT_X, y=BOAT_RIGHT_SLOT_Y, w=BOAT_PLAT_W, h=BOAT_PLAT_H)
        self.right_margin = Platform(None, self.cena, RIGHT_MARGIN_X, RIGHT_MARGIN_Y, RIGHT_MARGIN_W, RIGHT_MARGIN_H, RIGHT_MARGIN, self.monster_right_slot, self.dwarf_right_slot, self.apple_right_slot, self.boat_right_slot, self)
        self.monster_right_slot.entra(self.right_margin)
        self.dwarf_right_slot.entra(self.right_margin)
        self.apple_right_slot.entra(self.right_margin)
        self.boat_right_slot.entra(self.right_margin)
        self.right_margin.entra(self.cena)
        
        self.boat = Boat(IMG_BOAT_TO_RIGHT, self.cena, BOAT_OFFSET_X, BOAT_OFFSET_Y, BOAT_W, BOAT_H, self.left_margin, self.right_margin, self.boat_left_slot, self.boat_right_slot, self)
        self.boat.entra(self.boat_left_slot)
        
        self.monster = Character(
            IMG_MONSTER, 
            self.cena, 
            self.monster_left_slot, 
            MONSTER_OFFSET_X, MONSTER_OFFSET_Y, 
            MONSTER_W, MONSTER_H, 
            MONSTER, 
            self.left_margin, 
            self.boat)
        self.dwarf = Character(
            IMG_DWARF, 
            self.cena, 
            self.dwarf_left_slot,
            DWARF_OFFSET_X, DWARF_OFFSET_Y, 
            DWARF_W, DWARF_H, 
            DWARF, 
            self.left_margin, 
            self.boat)
        self.apple = Character(
            IMG_APPLE, 
            self.cena, 
            self.apple_left_slot,
            APPLE_OFFSET_X, APPLE_OFFSET_Y, 
            APPLE_W, APPLE_H, 
            APPLE, 
            self.left_margin, 
            self.boat)
        
        self.left_margin.put(self.monster)
        self.left_margin.put(self.dwarf)
        self.left_margin.put(self.apple)
        
        self.cena.vai()


    def showStartScreen(self):
        self.cena = Cena(CENA_START)

        self.start_button_slot = Botao(image=IMG_BOTAO_START, cena=self.cena, x=BOTAO_START_X, y=BOTAO_START_Y, w=BOTAO_START_W, h=BOTAO_START_H, name=BOTAO_START, game=self)
        self.start_button_slot.entra(self.cena)

        self.cena.vai()
        
    def showEndScreen(self):
        self.cena = Cena(CENA_END)

        self.home_button_slot = Botao(image=IMG_BOTAO_HOME, cena=self.cena, x=BOTAO_HOME_X, y=BOTAO_HOME_Y, w=BOTAO_HOME_W, h=BOTAO_HOME_H, name=BOTAO_HOME, game=self)
        self.home_button_slot.entra(self.cena)
        
        self.restart_button_slot = Botao(image=IMG_BOTAO_RESTART, cena=self.cena, x=BOTAO_RESTART_X, y=BOTAO_RESTART_Y, w=BOTAO_RESTART_W, h=BOTAO_RESTART_H, name=BOTAO_RESTART, game=self)
        self.restart_button_slot.entra(self.cena)

        self.cena.vai()


    def gameStatus(self):
        self.left_margin.printStatus()
        self.right_margin.printStatus()
        self.boat.printStatus()
        print("\n")
        
        
        
if __name__ == "__main__":
    Game()