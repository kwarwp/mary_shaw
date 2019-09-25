
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