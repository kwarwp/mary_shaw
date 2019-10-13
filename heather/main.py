# mary_shaw.heather.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from random import shuffle
NAMES = "Igor Leonardo Diogo Vinicios Benjamim Enzo Rodrigo Tomás Diego Luis Kevin Augusto Filipe" +\
" Pablo André Emanuel Fernando Danilo Renan Levi Alexandre Lorenzo Octávio Ricardo Marcelo Kelvin Leandro"+\
" Wilian Alan Júlio Jonathan Calebe Paulo Joaquim Fabrício Francisco Douglas António Carlos Vicente Fábio"+\
" Lourenço Marcos Renato Ângelo Raul Frederico José Valentim Manuel Artur Gabriel Guilherme Bernardo Lucas"+\
" Gustavo Bryan Rafael Henrique David Mateus Nicolas Victor Caio Theo Felipe Santiago Martim Jonas Maurício"+\
" Afonso Michael César Cristiano Jorge Ramom Edgar Ulisses Juliano Ivan Marco Flávio Anderson Aquiles Alexander"+\
" Álvaro Muriel Adriano Roberto"
NAMES=NAMES.split()
shuffle(NAMES)
STYLE.update(width=1350, height=650)
THEMES = "nature food animals transport city sports people technics".split()
THEMES = [theme+f"/{count}/" for count in range(1,6) for theme in THEMES]
shuffle(THEMES)
#THEMES = [f"{theme}{name}" for theme, name in zip( THEMES,NAMES)]
CN=10
delta = 1350//CN

#LOREM = "https://loremflickr.com/200/200/{}"
LOREM = "http://lorempixel.com/150/150/{}/"
theme = "sky"
def calc(count):
    return dict(x=(count%CN)*delta, y=(count//CN)*delta) 
#print(LOREM.format(theme))
cena = Cena("https://lorempixel.com/1350/650/abstract/")
[Elemento(LOREM.format(theme), w=delta, h=delta, cena=cena, **calc(count)) for count, theme in enumerate(THEMES)]
cena.vai()
#print(LOREM.format(theme, 2))