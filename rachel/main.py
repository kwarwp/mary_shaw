# mary_shaw.rachel.main.py

# Imgur é um serviço semelhante ao cloudinary, que serve 
# para hospedar imagens, entregando um endereço URL para 
# ser referenciado dentro de um código qualquer. Aqui 
# utilizamos o Imgur para poder hospedar a imagem do templo.
# Tal serviço funciona com um extensão do firefox, na qual
# basta clicar com o botão direito e fazer upload to imgur.
# Depois, clicar no ícone do Imgur e copiar o link gerado.

# PEP 8 é uma convência do Python que indica as melhores
# práticas para a escrita da linguagem. Nesta são definidos
# pontos como a ordem de aparecimento das estruturas, 
# espaçamentos, formas de nomes de variáveis, identação
# entre outros.

# O PEP 8 define que a primeira coisa que se tem no código
# é a sua documentação. No caso, aqui é representada pelas
# aspas duplas repetidas 3 vezes. Observe que este tipo de 
# comentário é executado pelo interpretador do Python, apesar
# de ser um comentário. Nesse caso, código Python dentro 
# dele será executado.
"""
    Jogo do Tesouro Inca
     
"""

# Essa é uma forma de se importar uma classe Python pelo 
# super python de uma outra máquina. Ou seja, é a importação
# de uma classe de outro aluno.
# from adda.main import JogoTesouroInca as JogoMarilia

# A classe vitollino foi feita pelo professor e trabalha com 
# a parte gráfica do Python. Aqui, será utilizada para exibir
# o fundo com a imagem do templo.
from _spy.vitollino.main import Cena

# A definição do nome de constantes, segundo o PEP8 é feita
# com letras maiúsculas, sendo as palavras separadas por 
# underline
IMAGEM_DO_TEMPLO = "https://i.imgur.com/TyH3QTV.jpg"

# A variável __author__ é interna e aqui contém informações
# acerca do autor do código.
__author__ = "Andre R Vieira"


# Entre as classes, o PEP 8 indica que deve ter 2 linhas em
# branco, como as acima. Além disso, nomes de classes usam 
# a camel case, como no Java. Observe que somente nomes de 
# classe utilizam tal formato, métodos, atributos, variáveis,
# constantes etc, utilizam outros formatos.
class JogoTesouroInca:
    # A identação pelo PEP 8 após um ":" é de 4 espaços e não 
    # de um tab. Prestar atenção nisso, senão o compilador 
    # reclama e deixa marcado de vermelho.
    # A primeira linha de código depois do ":", segundo o PEP 8
    # deve ser a documentação da funcionalidade daquela classe
    # ou método.
    """ Representa o Jogo principal """
    # No Python, o __init__ representa o construtor da classe.
    # Nesse caso, foi passado o self, que representa a instância 
    # da classe que está sendo criada. Eu poderia passar cls, o 
    # que indica que a classe em si está sendo passada no 
    # argumento.
    def __init__(self):
        """ Constroi a cena """
        # Aqui eu crio uma variável na minha instância, da classe
        # JogoTesouroInca, a qual recepciona um objeto da classe
        # Cena criado pelo construtor com a passagem da URL do 
        # imgur.
        # Observe que a classe se chama Cena justamente porque 
        # demos esse apelido a ela na importação lá em cima.
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO)
        
    # Aqui vamos criar um método para a classe que também receberá
    # como argumento a instância em si da classe. Essa instância que
    # possui a variável com a instância da classe Cena. A partir dai
    # vamos chamar o método vai dessa instância que irá exibir a 
    # imagem do templo.
    def inicia(self):
        """ Inicia a construção do Jogo """
        self.cena_do_templo.vai()
        # Quando um método está vazio e eu quero deixar ele para 
        # implementar depois, o Python irá reclamar porque não pode
        # existir métodos que não façam nada. Para resolver esse 
        # problema, eu utilizo a palavra "pass" como a abaixo.
        # pass



class Jogador:
class Tumba:
class Acampamento:
class Camara:
class Gemas:

        

# Com a classe definda, agora preciso realmente instanciar objetos 
# dela e chamar os métodos desejados, como em uma main do Java.
# Nesse moomento, a melhor prática para se realizar isso é com a 
# statement abaixo, utilizando o if para testar se o nome do código
# é o main. Lá em cima definimos mary_shaw.rachel.main.py, o que 
# indica que esse código se chama main.
if __name__ == "__main__":
    jogo = JogoTesouroInca()
    jogo.inicia()
    # O trecho abaixo é para ser usado com a importação do código 
    # de outro aluno.
    #outro_jogo = JogoMarilia()
    #outro_jogo.inicia()