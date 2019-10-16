
{'date': 'Wed Oct 02 2019 12:27:57.566 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 50
  Tesouro(choice(range)(1,4))).vai()
                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 02 2019 12:29:38.997 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 48
  class ProximaCamara:
  ^
IndentationError: unexpected indent
'''},
{'date': 'Wed Oct 02 2019 12:30:24.631 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 61
  def __init__(self, acampamento):
  ^
IndentationError: unexpected indent
'''},
{'date': 'Wed Oct 02 2019 12:35:39.553 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 100
    jogo = JogoTesouroInca()
  module <module> line 89
    self.tumba = Tumba(self.acampamento, self.eu)
  module <module> line 63
    self.tumba = [Tesouros(pedras+1, acampamento, eu) for pedras in range(4)]
TypeError: __init__() takes 2 positional argument but more were given
'''},
{'date': 'Wed Oct 02 2019 12:35:43.293 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 100
    jogo = JogoTesouroInca()
  module <module> line 89
    self.tumba = Tumba(self.acampamento, self.eu)
  module <module> line 63
    self.tumba = [Tesouros(pedras+1, acampamento, eu) for pedras in range(4)]
TypeError: __init__() takes 2 positional argument but more were given
'''},
{'date': 'Wed Oct 16 2019 11:15:35.552 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 23
  TemploInca.camara -= 1
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Oct 16 2019 11:16:03.542 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Uma expedição para coletar os tesouros de um templo Inca
O que existe nela
Você coloca 1 tesouro na mochila
Você fica com 1 tesouros na mochila
O que existe nela
Você coloca 1 tesouro na mochila
Você fica com 2 tesouros na mochila
O que existe nela
Você coloca 1 tesouro na mochila
Você fica com 3 tesouros na mochila
O que existe nela
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
  module <module> line 42
    TemploInca().inicia()
  module <module> line 17
    self.entra()
  module <module> line 24
    self.pega(1)
  module <module> line 39
    self.entra()
  module <module> line 24
    self.pega(1)
  module <module> line 39
    self.entra()
  module <module> line 24
    self.pega(1)
  module <module> line 39
    self.entra()
  module <module> line 26
    print(f"A rodada acabou para você, leve suas {Templo.cabana} para cabana")
  module <module> line 1
    (Templo.cabana)
NameError: name 'Templo' is not defined
'''},
{'date': 'Wed Oct 16 2019 11:18:15.818 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Uma expedição para coletar os tesouros de um templo Inca
O que existe nela
Você coloca 1 tesouro na mochila
Você fica com 1 tesouros na mochila
O que existe nela
Você coloca 1 tesouro na mochila
Você fica com 2 tesouros na mochila
O que existe nela
Você coloca 1 tesouro na mochila
Você fica com 3 tesouros na mochila
O que existe nela
A rodada acabou para você, leve suas 0 para cabana
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
  module <module> line 42
    TemploInca().inicia()
  module <module> line 17
    self.entra()
  module <module> line 24
    self.pega(1)
  module <module> line 39
    self.entra()
  module <module> line 24
    self.pega(1)
  module <module> line 39
    self.entra()
  module <module> line 24
    self.pega(1)
  module <module> line 39
    self.entra()
  module <module> line 27
    self.sai()
  module <module> line 31
    Print("Você sai do templo e guarda os tesouros!")
NameError: name 'Print' is not defined
'''},
{'date': 'Wed Oct 16 2019 11:50:04.444 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 30
  def __init__
               ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 12:15:37.727 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Uma expedição para coletar os tesouros de um templo Inca
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
  module <module> line 58
    TemploInca().inicia()
  module <module> line 50
    self.Camara.entra(self.explorador)
AttributeError: 'TemploInca' object has no attribute 'Camara'
'''},