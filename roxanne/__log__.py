
{'date': 'Wed Oct 02 2019 05:06:44.778 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 37
    jogo = JogoTesouroInca()
  module <module> line 29
    self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO, direita=Camara())
TypeError: __init__() missing 1 positional argument: jogador
'''},
{'date': 'Wed Oct 02 2019 05:08:00.179 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 37
    jogo = JogoTesouroInca()
  module <module> line 29
    self.cena_do_templo = Cena(IMAGEM_DO_TEMPLO, direita=Camara(Jogador()))
  module <module> line 24
    super().__init__(MUMIA, direita=ProximaCamara())
TypeError: __init__() missing 1 positional argument: jogador
'''},