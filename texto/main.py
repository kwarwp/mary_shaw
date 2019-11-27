# mary_shaw.texto.main.py
from _spy.vitollino.main import NADA, DOC_PYDIV, NoEv, ABOXED
from browser import document, html, timer, alert

class Popup:
    POP = None

    def __init__(self, cena, tit="", txt="", vai=None, **kwargs):
        self.cena, self.tit, self.txt, = cena, tit, txt
        self.kwargs = kwargs
        self._vai = vai
        self.optar = {}
        Popup.__setup__()
        Popup.inicia()
        if isinstance(cena, Cena):
            self.d(cena, tit, txt)

    def vai(self):
        return self._vai() if self._vai else None

    def __call__(self, cena=None, tit="", txt="", *args, **kwargs):
        cena = cena or self.cena
        out = cena(*args, **kwargs)
        self.d(out, tit or self.tit, txt or self.txt)

        return out  # CenaPopup

    @staticmethod
    def __setup__():
        class Pop:
            def __init__(self, tela=DOC_PYDIV):
                self.tela = tela
                self.optou = ""
                self.foi = None
                self.popup = html.DIV(Id="__popup__", Class="overlay")
                self.div = div = html.DIV(Class="popup")
                self.tit = html.H2()
                self.a = html.A("&times;", Class="close", href="#")
                self.go = html.A(Id="txt_button", Class="button", href="#__popup__")
                self.go.onclick = self._open
                self.a.onclick = self._close
                self.alt = html.DIV(Class="content")
                self.popup <= div
                self.popup.style = {"visibility": "hidden", "opacity": 0}
                self.inicia()
            def inicia(self):
                self.foi = lambda *_: None
                self.div.html = ""
                self.div <= self.tit
                self.div <= self.a
                self.div <= self.alt

            def __repr__(self):
                return "<Popup>"

            def _close(self, *_):
                self.popup.style = {"visibility": "hidden", "opacity": 0}
                self.esconde()

            def _open(self, *_):
                self.popup.style = {"visibility": "visible", "opacity": 0.7}

            def esconde(self, *_):
                ...

            def monta_optar(self, **kwargs):
                def opcao(letra):
                    alert(self.foi)
                    self.foi(letra)

                def opta(letra, texto):
                    div = html.DIV(Class="content")
                    optou = html.A(chr(ABOXED + ord(letra) - ord("A")), Class="option", href="#")
                    optou.onclick = lambda *_: opcao(letra) or self._close()
                    texto_opcao = html.SPAN(texto)
                    div <= optou
                    div <= texto_opcao
                    return div

                optar = [[optou, texto] for optou, texto in kwargs.items() if optou in "ABCDEFGHIJK"]
                for op in optar:
                    self.div <= opta(*op)

            def mostra(self, act, tit="", txt="", **kwargs):
                self.foi = act if act else self.foi
                if tit or txt:
                    self.tit.text, self.alt.text = tit, txt
                self.monta_optar(**kwargs)
                # self.popup.style = {"visibility": "visible", "opacity": 0.7}
                self._open()

        Popup.POP = Pop()
        Popup.__setup__ = lambda: None

    @staticmethod
    def d(cena, tit="", txt=""):
        cena.elt <= Popup.POP.popup
        cena.elt <= Popup.POP.go
        act = cena.vai
        cena.vai = lambda *_, **__: Popup.POP.mostra(act, tit, txt)
        return cena

    @staticmethod
    def inicia():
        Popup.POP.inicia()


class Texto(Popup):
    def __init__(self, cena=NADA, tit="", txt="", foi=None, **kwargs):
        super().__init__(None, tit=tit, txt=txt, vai=None, **kwargs)
        #self.elt = Popup.POP.popup
        self.cena = cena
        self.kwargs = kwargs
        self.esconde = foi if foi else self.esconde
        #cena <= self

    @property  
    def foi(self):
        return self.esconde

    @foi.setter  
    def foi(self, value):
        self.esconde = value

    def esconde(self, ev=NoEv()):
        pass

    def mostra(self, tit="", txt="", act=None, **kwargs):
        kwargs = kwargs if kwargs else self.kwargs
        act = act if act else lambda *_: None
        self.elt = Popup.POP.popup
        self.cena.elt <= self.elt
        
        Popup.POP.esconde = self.esconde
        Popup.POP.mostra(act, tit=tit, txt=txt, **kwargs)

    def vai(self, ev=NoEv()):
        # self.elt = Popup.POP.popup
        ev.stopPropagation()
        self.cena.elt <= Popup.POP.popup
        self.mostra(self.tit, self.txt, act=self.foi)
        return False
