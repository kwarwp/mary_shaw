# mary_shaw.danae.main.py
from browser import document, html
pagina = html.HEAD()
title = html.TITLE("Olá mundo HTML")
corpo = html.BODY()
div = html.DIV()
span = html.SPAN("Olá mundo HTML")
pagina <= title

document.head.innerHTML = ""
document.body.innerHTML = ""
document.documentElement.innerHTML = ""
document <= pagina
document <= corpo
corpo <= div
div <= span