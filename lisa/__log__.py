
{'date': 'Tue Sep 24 2019 19:20:44.264 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  """ Constroi a Cena"""
  ^
IndentationError: expected an indented block
'''},
{'date': 'Tue Sep 24 2019 19:21:04.732 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  """Constroi a Cena"""
  ^
IndentationError: expected an indented block
'''},
{'date': 'Tue Sep 24 2019 19:21:23.817 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  """Constroi a Cena"""
  ^
IndentationError: expected an indented block
'''},
{'date': 'Tue Sep 24 2019 19:22:15.621 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Descrição: Templo do Tesouro Inca
Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 31
    jogo.inicia()
  module <module> line 26
    self.cena_do_templo.vai() 
AttributeError: 'str' object has no attribute 'vai'
'''},
{'date': 'Wed Oct 02 2019 11:51:34.684 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 91
    jogo = JogoTesouroInca()
  module <module> line 79
    self.tmba = Tumba()
  module <module> line 48
    self.tumba = [Tesouro(pedras+1) for pedras in range(4)]
  module <module> line 38
    super().__init__(cena)
NameError: name 'cena' is not defined
'''},
{'date': 'Wed Oct 02 2019 11:56:45.294 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 91
    jogo = JogoTesouroInca()
  module <module> line 79
    self.tmba = Tumba()
  module <module> line 48
    self.tumba = [Tesouro(pedras+1) for pedras in range(4)]
NameError: name 'Tesouro' is not defined
'''},
{'date': 'Wed Oct 02 2019 11:59:30.457 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 92
    jogo = JogoTesouroInca()
  module <module> line 80
    self.tmba = Tumba()
  module <module> line 49
    self.tumba = [Tesouros(pedras+1) for pedras in range(4)]
  module <module> line 39
    super().__init__(TESOURO, direita=proxima_camara)
NameError: name 'proxima_camara' is not defined
'''},
{'date': 'Wed Oct 16 2019 10:45:05.371 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 30
  TemploInca.mochila + = quantidade
                        ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 11:08:43.289 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 40
  def sai(self, TemploInca.mochila)
                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 11:09:10.477 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 40
  def sai(self, quantidade)
                            ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 11:09:20.761 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 40
  def sai(self)
                ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 11:13:28.908 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 39
  def sai(self, TemploInca.mochila)
                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 11:13:47.674 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 39
  def sai(self, mochila)
                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 12:16:11.202 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 24
  def sai(self)
                ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 12:18:05.278 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 31
  Tesouro = 1
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Oct 16 2019 12:18:19.744 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 31
  def __init__(self)
                     ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 12:18:47.303 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 32
  self.camara = 3
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Oct 16 2019 12:19:46.227 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 32
  self.explorador=Explorador()
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Oct 16 2019 12:20:04.17 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 32
  self.explorador = Explorador()
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Oct 16 2019 12:20:37.680 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 30
  self.explorador = Explorador()
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Oct 16 2019 12:21:29.518 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 30
  self.explorador = Explorador()
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Oct 16 2019 12:22:06.833 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 48
  self.explorador = Explorador() #(self) (self.camara)
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Oct 16 2019 12:22:41.482 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Uma expedição para coletar os tesouros do Templo Inca
Você entra em uma câmara com tesouros!
Você coloca 1 tesouro na mochila 
Você fica com 1 tesouros na mochila 
Você entra em uma câmara com tesouros!
Você coloca 1 tesouro na mochila 
Você fica com 2 tesouros na mochila 
Você entra em uma câmara com tesouros!
Você coloca 1 tesouro na mochila 
Você fica com 3 tesouros na mochila 
Você entra em uma câmara com tesouros!
Não havia mais tesouros!
Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 74
    TemploInca().inicia()
  module <module> line 56
    self.entra()
  module <module> line 64
    self.explorador.pega(1, self)
  module <module> line 26
    camara.entra()
  module <module> line 64
    self.explorador.pega(1, self)
  module <module> line 26
    camara.entra()
  module <module> line 64
    self.explorador.pega(1, self)
  module <module> line 26
    camara.entra()
  module <module> line 67
    self.explorador.sai()
AttributeError: 'Explorador' object has no attribute 'sai'
'''},
{'date': 'Sun Nov 03 2019 19:14:44.752 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 33
  if input("Nova Incursão?")
                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Nov 03 2019 19:14:51.549 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 33
  if input("Nova Incursão?")
                             ^
SyntaxError: invalid syntax
'''},