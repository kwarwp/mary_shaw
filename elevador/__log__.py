
{'date': 'Tue Nov 26 2019 20:08:12.963 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 29
  INVENTARIO.score(self, casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1):
                                                                                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Nov 26 2019 20:08:52.66 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 29
  INVENTARIO.score(casa="elevador", carta=self.na_cesta, move="desce", ponto=0, valor=0, _level=1):
                                                                                                   ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Nov 27 2019 17:00:17.732 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 63
    Elevador()
  module <module> line 22
    a = Texto(predio, "oi", A="ee", B="uu")
NameError: name 'Texto' is not defined
'''},
{'date': 'Wed Nov 27 2019 17:22:00.588 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 65
    Elevador()
  module <module> line 24
    b = Texto(predio, Popup.POP.optou)
NameError: name 'Popup' is not defined
'''},