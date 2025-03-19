
{'date': 'Wed Mar 19 2025 18:14:07.440 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 66
    jogo = JogoTesouroInca()
  module <module> line 56
    self.acampamento = Acampamento(ACAMPAMENTO)
  module <module> line 45
    self.pedra = Elemento(TURQUESA, cena=self)
  module elemento.main line 19
    self.img, self.title, self.dropper, self.alt = img, tit, drop, alt
  module _spy.vitollino.main line 668
    self.elt.style.backgroundImage = "url({})".format(value)
AttributeError: 'Elemento' object has no attribute 'elt'
'''},