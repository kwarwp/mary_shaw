# mary_shaw.danae.main.py
from browser import document, html
pagina = html.HEAD()
title = html.TITLE("Olá mundo HTML")
corpo = html.BODY()
div = html.DIV()
span = html.SPAN("Olá mundo HTML")
strong = html.STRONG("Isto é importante")
titulo1 = html.H1("é um título")
pagina <= title

document.head.innerHTML = ""
document.body.innerHTML = ""
document.documentElement.innerHTML = ""
document <= pagina
document <= corpo
corpo <= div
div <= titulo1
div <= span
div <= strong