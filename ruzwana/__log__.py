
{'date': 'Wed Oct 09 2019 11:55:51.259 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 223
    jogo = JogoTesouroInca()
  module <module> line 212
    self.tumba = Tumba(self.acampamento, self.eu)
  module <module> line 185
    self.tumba = [Tesouros(pedras+1, acampamento, eu) for pedras in range(4)]
  module <module> line 166
    self.pedras = PedrasPreciosas(quantas_pedras=self.tesouro)
  module <module> line 128
    self.pedras_especificas = [Elemento(
  module elemento.main line 40
    self.scorer = dict(ponto=1, valor=cena.nome, carta=tit or img, casa=self.xy, move=None)
AttributeError: 'PedrasPreciosas' object has no attribute 'nome'
'''},