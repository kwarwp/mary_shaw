
{'date': 'Tue Dec 10 2019 14:17:16.44 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 76
    Basico()
  module <module> line 71
    self.gato = Personagem(CAT, destino=self.cart, cena=cena, x= 100)
AttributeError: 'Basico' object has no attribute 'cart'
'''},
{'date': 'Tue Dec 10 2019 15:31:55.376 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 81
    Basico()
  module <module> line 72
    self.cart0 = Veiculo(CART, destino=self.base1, cena=self.base0)
  module <module> line 40
    super().__init__(imagem, cena=cena, x=x, y=y)
  module _spy.vitollino.main line 551
    _ = self.entra(cena) if cena and (cena != INVENTARIO) else None
  module <module> line 56
    self.fundo.entra(passageiro)
AttributeError: 'Veiculo' object has no attribute 'fundo'
'''},