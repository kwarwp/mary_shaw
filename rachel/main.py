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
MUMIA = "https://i.imgur.com/YGV3CPB.jpg"
COBRA = "https://i.imgur.com/IeC0gBj.jpg"
TESOURO = "https://i.imgur.com/xkBdHCE.jpg"
TURQUESA = "https://i.imgur.com/8WDBJM3.png"
ACAMPAMENTO = "https://i.imgur.com/dmSDeDF.jpg"

# A variável __author__ é interna e aqui contém informações
# acerca do autor do código.
__author__ = "Andre R Vieira"

class PedrasPreciosas:
    """ Um conjunto de pedras que se organizam por valor """
    # Quando eu quero descrever parâmetros de métodos de classes, eu 
    # faço esse formato com : que está abaixo. Observe que isso é lido
    # e interpretado pleo python
    def __init__(self, valor):
        """ Inicia com valor equivalente de turquesas
            :param valor: valor do tesouro em número de turquesas. 
        """
        # Os 3 pontinhos funciona semelhante ao pass para implementação futura
        # Semelhante ao TODO do java
        #
        # A diferença entre o pass e os ...
        # O pass indica que não terá mais nada naquele local, ou seja, é definitivo
        # Já os ... é como o TODO, é temporário e será implementado algo posteriormente
        ...
        
    def aumenta(self, valor):
        """ Aumenta o tesouro com valor equivalente de turquesas
            :param valor: valor a acrescentar ao tesouro em número de turquesas
        """
        
        
        
# Os parênteses depois do nome da classe indica que está herda daquela,
# ou seja, Acampamento herda de Cena
class Acampamento(Cena):
    """ Um lugar seguro e quentinho para admirar os seus ganhos """
    def __init__(self, cena):
        """ Inicia com tesouro vazio """
        self.tesouro = 0
        # Após executar tudo que preciso para a minha classe herdeira, eu 
        # chamo o construtor da super classe com o statement abaixo.
        # Isso fará com que o Python chame o __init__ da super classe.
        super().__init__(cena)
        self.pedra = Elemento(TURQUESA, cena=self)
        
    def ganho(self, valor):
        """ Aumenta o tesouro com valor equivalente de turquesas
            :param valor: valor a acrescentar ao tesouro em número de turquesas
        """
        self.tesouro += valor
        
        

class Jogador():
    """ Um explorador em busca de tesouros """
    def __init__(self):
        """ Inicia com tesouro """



class Tumba():
    """ Um complexo de camaras secretas sob o templo """
    def __init__(self):
        """ Inicia o complexo de camaras """


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
    # No Python, o __init__ representa uma espécie de construtor da classe.
    # Nesse caso, foi passado o self, que representa a instância 
    # da classe que está sendo criada. Eu poderia passar cls, o 
    # que indica que a classe em si está sendo passada no 
    # argumento.
    # A diferença do __init__ para o construtor é que no Python não 
    # se tem um construtor definido no código, este será feito implicitamente
    # quando se chama a classe. O __init__ é a função executada quando
    # uma classe criada, semelhante a um onCreate do java. Observe que
    # o construtor teria que alocar espaços na memória etc, o que 
    # o init não faz
    def __init__(self):
        """ Constroi a cena """
        # Aqui eu crio uma variável na minha instância, da classe
        # JogoTesouroInca, a qual recepciona um objeto da classe
        # Cena criado pelo construtor com a passagem da URL do 
        # imgur.
        # Observe que a classe se chama Cena justamente porque 
        # demos esse apelido a ela na importação lá em cima.
        self.acampamento = Acampamento(ACAMPAMENTO)
        self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO, self.acampamento)
        self.acampamento.direita = self.cena_do_templo
        
        
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
    
    # Toda aquela documentação criada com os """ será utilizada para
    # gerar um help utilizando a função help() nativa do Python, como 
    # exemplificado nas duas linhas abaixo.
    #print(help(PedrasPreciosas))
    #print(help(PedrasPreciosas.aumenta))
    #print(help(Cena))