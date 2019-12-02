
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
{'date': 'Wed Nov 27 2019 18:19:00.62 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 23
    a = Texto(predio, "oi", A="ee", B="uu")
TypeError: 'module' object is not callable
'''},
{'date': 'Wed Nov 27 2019 18:20:53.701 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 4
    from texto.main import Texto
  module texto.main line 105
    class Texto(Popup):
  module texto.main line 106
    def __init__(self, cena=NADA, tit="", txt="", foi=None, **kwargs):
NameError: name 'NADA' is not defined
'''},
{'date': 'Wed Nov 27 2019 18:23:51.513 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 23
    a = Texto(predio, "oi", A="ee", B="uu")
  module texto.main line 107
    super().__init__(None, tit=tit, txt=txt, vai=None, **kwargs)
  module texto.main line 12
    Popup.__setup__()
  module texto.main line 89
    Popup.POP = Pop()
  module texto.main line 34
    self.popup = html.DIV(Id="__popup__", Class="overlay")
NameError: name 'html' is not defined
'''},
{'date': 'Wed Nov 27 2019 18:25:28.141 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
    a.vai()
  module texto.main line 139
    self.mostra(self.foi, self.tit, self.txt)
  module texto.main line 133
    Popup.POP.mostra(act, tit=tit, txt=txt, **kwargs)
  module texto.main line 86
    self.monta_optar(**kwargs)
  module texto.main line 80
    self.div <= opta(*op)
  module texto.main line 71
    optou = html.A(chr(ABOXED + ord(letra) - ord("A")), Class="option", href="#")
NameError: name 'ABOXED' is not defined
'''},
{'date': 'Wed Nov 27 2019 18:35:44.662 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 23
  def _foi(l="ZZ")
                   ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Dec 02 2019 18:30:09.835 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 23
    a = Texto(predio, "oi", foi=lambda op="YY": Texto(predio, f"escolheu {op}").vai(), A="ee", B="uu")
  module texto.main line 114
    super().__init__(None, tit=tit, txt=txt, vai=None, **kwargs)
  module texto.main line 15
    if isinstance(cena, Cena):
NameError: name 'Cena' is not defined
'''},
{'date': 'Mon Dec 02 2019 20:45:31.599 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 23
    a = Texto(predio, "oi", foi=lambda op="YY": Texto(predio, f"escolheu {op}").vai(), A="ee", B="uu")
  module texto.main line 114
    super().__init__(None, tit=tit, txt=txt, vai=None, **kwargs)
  module texto.main line 15
    if isinstance(cena, Cena):
NameError: name 'Cena' is not defined
'''},
{'date': 'Mon Dec 02 2019 20:56:08.900 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 23
    a = Texto(predio, "oi", foi=lambda op="YY": Texto(predio, f"escolheu {op}").vai(), A="ee", B="uu")
  module texto.main line 114
    super().__init__(None, tit=tit, txt=txt, vai=None, **kwargs)
  module texto.main line 15
    if isinstance(cena, Cena):
NameError: name 'Cena' is not defined
'''},