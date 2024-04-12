# Completa la función, que calcula cuánto debes dejar de propina en función del importe total de la factura y del servicio.

# Debe considerar las siguientes calificaciones:

# Terrible: propina 0%
# Pobre: ​​propina 5%
# Bueno: propina 10%
# Genial: propina 15%
# Excelente: propina 20%
# La calificación no distingue entre mayúsculas y minúsculas (por lo tanto, "excelente" = "GRANDE"). Si se recibe una calificación no reconocida, deberá devolver:

# "Rating not recognised"en Javascript, Python y Ruby...
# ...o nullen Java
# ...o -1en C#
# Como eres una buena persona, siempre redondeas la propina, independientemente del servicio.

import math
def calculate_tip(importe_total, calidad_servicio):
    calidad_servicio = calidad_servicio.lower()

    if calidad_servicio == "terrible":
        return 0
    elif calidad_servicio == "poor":
        return math.ceil((importe_total * 5) / 100)
    elif calidad_servicio == "good":
        return math.ceil((importe_total * 10) / 100)
    elif calidad_servicio == "great":
        return math.ceil((importe_total * 15) / 100)
    elif calidad_servicio == "excellent":
        return math.ceil((importe_total * 20) / 100)
    else:
        return "Rating not recognised"
        
print(calculate_tip(107.65, "GReat"))

    