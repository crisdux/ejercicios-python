# Dada un fragmento de HTML que contiene una etiqueta de encabezado , , ...  Se pide transformarlo a su correspondiente versión de
# Markdown.


    
def extraer_texto(html):
    index_primera_etiqueta = html.find(">")
    nuevo_html = html[index_primera_etiqueta + 1:]
    index_ultima_etiqueta = nuevo_html.find("<")
    return (nuevo_html[: index_ultima_etiqueta]).strip()
    

def identificar_tipo_encabezado(html):
    nuevo_html = html[2:]
    index_primera_etiqueta = html.find(">")
    return nuevo_html[: index_primera_etiqueta-2]
    

def h2md(html):
    if int(identificar_tipo_encabezado(html)) > 6 or int(identificar_tipo_encabezado(html)) < 1:
        return "No es un encabezado valido html"
    dict_valores = {"1": "#", "2":"##", "3": "###", "4": "####", "5": "#####", "6": "######"}
    
    return f"{dict_valores[ identificar_tipo_encabezado(html) ]} {extraer_texto(html)}"
    
print(h2md("<h1> Core </h1>")) # Core
print(h2md("<h2> Tipos de cadenas </h2>")) ## Tipos de cadenas
print(h2md("<h3> Cadenas de Texto </h3>")) ### Cadenas de Texto
print(h2md("<h4> Hola </h4>")) ## Hola
    