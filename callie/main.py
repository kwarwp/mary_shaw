# mary_shaw.callie.main.py

'''
uMA EXPEDIÇÃO PARA COLETAR OS TESOUROS DO TEMPLO INCA

--Relato: Sou um incursor que se aventurou por cavernas e câmaras em busca do tesouro Inca.
Sempre que conseguíamos o tesouro, guardávamos na cabana. A cada problema, perdíamos as pedras obtidas.
'''


class TemploInca:
    cabana = 0
    mochila = 0
    camara = 3

    def inicia(self):
        # inicia a exploração
        print("Uma expedição para coletar os tesouros do Templo Inca")
        self.entra()

    def entra(self):
        # Entra em uma câmara
        print("Você entra em uma câmara com tesoutos!")
        if TemploInca.camara:
            TemploInca.camara -= 1
            self.pega(1)
        else:
            print("Não havia mais tesouros!")
            self.sai()

    def sai(self):
        print("Você sai do templo e guarda os tesouros!")
        TemploInca.cabana, TemploInca.mochila = TemploInca.mochila, 0

    def pega(self, quantidade):
        # Coloca um tesouro na mochila
        print(f"Você colocou {quantidade} do tesouro na mochila")
        TemploInca.mochila += quantidade
        print(f"Você fica com {TemploInca.mochila} tesouros na mochila")
        self.entra()


if __name__ == "__main__":
    TemploInca().inicia()