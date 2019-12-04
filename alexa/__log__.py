
{'date': 'Wed Dec 04 2019 12:10:38.534 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  pass
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Dec 04 2019 12:45:10.737 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 22
  def move(self, evento = None)
                                ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Dec 04 2019 12:46:36.800 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 47
    Basico()
  module <module> line 41
    self.gato = Elemento(CAT, cena=cena, x=700, y=200,w=60,h=60, vai = cart)
NameError: name 'cart' is not defined
'''},