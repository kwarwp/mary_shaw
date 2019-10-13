
{'date': 'Sun Oct 13 2019 11:38:16.820 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  from vitollino.main import Cena Elemento, STYLE
                                          ^
SyntaxError: trailing comma not allowed without surrounding parentheses
'''},
{'date': 'Sun Oct 13 2019 11:48:01.491 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 8
  [Elemento(LOREM.format(choice(THEMES)), x=10+(count*200)%1400, y=10+(count*200)//1400 w=190, h=190, cena=cena) 
                                                                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Oct 13 2019 11:53:24.623 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: obj is undefined
  module '$exec_1835' line 9
[Elemento(LOREM.format(theme), x=10+(count*200)%1400, y=10+(count*200)//1400, w=190, h=190, cena=cena) 
'''},
{'date': 'Sun Oct 13 2019 11:54:42.918 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: undefined has no properties
  module '$exec_1843' line 9
[Elemento(LOREM.format(theme), x=10+(count*200)%1400, y=10+(count*200)//1400, w=190, h=190, cena=cena) for count, theme in enumerate(TH)]
'''},
{'date': 'Sun Oct 13 2019 11:55:30.902 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: undefined has no properties
  module '$exec_1851' line 9
[Elemento(LOREM.format(t=theme), x=10+(count*200)%1400, y=10+(count*200)//1400, w=190, h=190, cena=cena) for count, theme in enumerate(TH)]
'''},
{'date': 'Sun Oct 13 2019 11:57:14.675 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: undefined has no properties
  module '$exec_1859' line 9
LOREM.format(t=TH[0])
'''},
{'date': 'Sun Oct 13 2019 11:58:24.312 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: undefined has no properties
  module '$exec_1867' line 9
LOREM%TH[0]
'''},
{'date': 'Sun Oct 13 2019 11:59:02.902 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: undefined has no properties
  module '$exec_1875' line 10
[Elemento(LOREM%theme, x=10+(count*200)%1400, y=10+(count*200)//1400, w=190, h=190, cena=cena) for count, theme in enumerate(TH)]
'''},
{'date': 'Sun Oct 13 2019 11:59:58.98 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''<undefined>

Exception: undefined has no properties
  module '$exec_1883' line 11
[Elemento(LOREM%theme, x=10+(count*200)%1400, y=10+(count*200)//1400, w=190, h=190, cena=cena) for count, theme in enumerate(TH)]
'''},
{'date': 'Sun Oct 13 2019 12:03:16.645 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 2
    from _spy.vitollino.main import Cen, Elemento
ImportError: cannot import name 'Cen'

ImportError
Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 264
    action()
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 2
    from _spy.vitollino.main import Cen, Elemento
'''},