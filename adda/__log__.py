
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
{'date': 'Wed Oct 16 2019 12:15:48.145 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
    Camara.entra(self.explorador)
TypeError: entra() missing 1 positional argument: explorador
'''},
{'date': 'Wed Oct 16 2019 12:16:46.207 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
    Camara.entra(Explorador())
TypeError: entra() missing 1 positional argument: explorador
'''},
{'date': 'Wed Oct 16 2019 12:18:01.86 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
    Camara.entra(self.explorador)
TypeError: entra() missing 1 positional argument: explorador
'''},
{'date': 'Wed Oct 16 2019 12:22:44.895 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 57
    TemploInca().inicia()
  module <module> line 49
    Camara.entra(self.explorador)
TypeError: entra() missing 1 positional argument: explorador
'''},
{'date': 'Wed Oct 16 2019 12:24:13.53 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 57
    TemploInca().inicia()
  module <module> line 49
    Camara.entra(self.explorador)
TypeError: entra() missing 1 positional argument: explorador
'''},
{'date': 'Wed Oct 16 2019 12:26:30.453 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Uma expedição para coletar os tesouros de um templo Inca
O que existe nela
Você coloca 1 tesouro na mochila
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
  module <module> line 59
    TemploInca().inicia()
  module <module> line 51
    self.camara.entra(self.explorador)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 19
    print(f"Você fica com {TemploInca.mochila} tesouros na mochila")
  module <module> line 1
    (TemploInca.mochila)
AttributeError: 'TemploInca' object has no attribute 'mochila'
'''},
{'date': 'Wed Oct 16 2019 12:28:29.338 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Uma expedição para coletar os tesouros de um templo Inca
O que existe nela
Você coloca 1 tesouro na mochila
Você fica com 1 tesouros na mochila
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
  module <module> line 59
    TemploInca().inicia()
  module <module> line 51
    self.camara.entra(self.explorador)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra()
TypeError: entra() missing 1 positional argument: explorador
'''},
{'date': 'Wed Oct 16 2019 12:29:03.74 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 59
    TemploInca().inicia()
  module <module> line 51
    self.camara.entra(self.explorador)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra(self)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra(self)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra(self)
  module <module> line 39
    print(f"A rodada acabou para você, leve suas {TemploInca.cabana} para cabana")
  module <module> line 1
    (TemploInca.cabana)
AttributeError: 'TemploInca' object has no attribute 'cabana'
'''},
{'date': 'Wed Oct 16 2019 12:30:09.711 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
Você sai do templo e guarda os tesouros!
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
  module <module> line 59
    TemploInca().inicia()
  module <module> line 51
    self.camara.entra(self.explorador)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra(self)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra(self)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra(self)
  module <module> line 40
    explorador.sai()
  module <module> line 26
    print(f"Você ficou com {self.camera} tesouros na mochila")
  module <module> line 1
    (self.camera)
AttributeError: 'Explorador' object has no attribute 'camera'
'''},
{'date': 'Wed Oct 16 2019 12:30:36.396 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
Você sai do templo e guarda os tesouros!
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
  module <module> line 59
    TemploInca().inicia()
  module <module> line 51
    self.camara.entra(self.explorador)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra(self)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra(self)
  module <module> line 37
    explorador.pega(1, self)
  module <module> line 20
    camara.entra(self)
  module <module> line 40
    explorador.sai()
  module <module> line 26
    print(f"Você ficou com {self.camara} tesouros na mochila")
  module <module> line 1
    (self.camara)
AttributeError: 'Explorador' object has no attribute 'camara'
'''},
{'date': 'Wed Oct 16 2019 12:40:29.980 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Uma expedição para coletar os tesouros de um templo Inca
O que existe nela
Você coloca 4 tesouro na mochila
Você fica com 4 tesouros na mochila
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
  module <module> line 64
    TemploInca().inicia()
  module <module> line 56
    self.camara.entra(self.explorador)
  module <module> line 42
    explorador.pega(randint(1, 4), self)
  module <module> line 22
    if inpunt("Continua?").lower() == "s":
NameError: name 'inpunt' is not defined
'''},