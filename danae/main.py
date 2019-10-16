# mary_shaw.danae.main.py

class Templo:
    cabana = 0
    explorador = 0
    camara = 3
    def inicia(self):
        """Inicia a aventura,explorador entra na camara"""
        print("Aventura inicia!")
        self.entra()
        
    def entra(self):
        """Explorador entra na camara"""
        Templo.camara -=1
        Templo.explorador +=1        
        print(f"Você consegue um tesouro, e tem {self.explorador} em sua mochila")
        if Templo.camara:
            self.entra()
        else:
            Templo.cabana, Templo.explorador = Templo.explorador, 0       
            print(f"Você termina a incursão, e tem {self.cabana} em sua cabana e {self.explorador} na mochila ")

        
Templo().inicia()
        