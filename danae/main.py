# mary_shaw.danae.main.py
from browser import document, html
pagina = html.HEAD()
title = html.TITLE("Olá mundo HTML")
corpo = html.BODY("Olá mundo HTML")
pagina <= title

document.html = ""

document <= pagina
document <= corpo