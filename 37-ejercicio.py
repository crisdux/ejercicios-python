# Usted es un desarrollador web novato/promedio/experimentado/profesional/mundialmente famoso (elija uno) que posee un sitio web simple/limpio/elegante/hermoso/complicado/profesional/comercial (elija uno o más) que contiene campos de formulario para que los visitantes puedan enviar correos electrónicos o dejar un comentario en su sitio web con facilidad. Sin embargo, con la facilidad viene el peligro . De vez en cuando, un pirata informático visita su sitio web e intenta comprometerlo mediante el uso de XSS (Cross Site Scripting) . Esto se hace inyectando scriptetiquetas en el sitio web a través de campos de formulario que pueden contener código malicioso (por ejemplo, una redirección a un sitio web malicioso que roba información personal).

# Misión
# Tu misión es implementar una función que convierta los siguientes caracteres potencialmente dañinos:

# <-->&lt;
# >-->&gt;
# "-->&quot;
# &-->&amp;

def convert_symbols(simbolo):
    match(simbolo):
        case '<':
            return "&lt;"
        case '>':
            return "&gt;"
        case '"':
            return "&quot;"
        case '&':
            return "&amp;"
        case _:
            return None

print(convert_symbols(">"))
print(convert_symbols('"'))