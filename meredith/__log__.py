
{'date': 'Wed Nov 06 2019 10:34:55.779 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 97
    TemploInca().inicia()
  module <module> line 82
    self.decide[o_que_decidiu]()
  module <module> line 86
    self.camara.entra(self.explorador)
  module <module> line 51
    self.decide[o_que_decidiu]()
TypeError: explora() missing 1 positional argument: explorador
'''},