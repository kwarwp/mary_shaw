
{'date': 'Wed Sep 25 2019 11:44:01.956 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 15
  if __name__ = "__main__":
               ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Oct 16 2019 10:25:23.819 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 28
    Templo().inicia()
NameError: name 'Templo' is not defined
'''},
{'date': 'Wed Oct 16 2019 10:41:21.198 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Uma expedição para coletar os tesouros o Templo Inca
Você entrou em uma câmara com tesouros!
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
  module <module> line 36
    TemploInca().inicia()
  module <module> line 21
    self.entra()
  module <module> line 32
    self.pega(1)
  module <module> line 27
    print(f"Agora você tem {mochila} tesouros na mochila")
  module <module> line 1
    (mochila)
NameError: name 'mochila' is not defined
'''},