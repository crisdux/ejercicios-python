# Después de un duro trimestre en la oficina, decides descansar un poco y tomarte unas vacaciones. Así que reservarás un vuelo para ti y tu novia e intentarás dejar todo el desorden atrás.

# Necesitará un coche de alquiler para poder desplazarse durante sus vacaciones. El responsable del alquiler de coches te hace buenas ofertas.

# Cada día que alquilas el auto cuesta $40. Si alquilas el auto por 7 días o más, obtienes $50 de descuento en tu total. Alternativamente, si alquilas el auto por 3 días o más, obtienes $20 de descuento en tu total.

# Escriba un código que proporcione el monto total para diferentes días (d).

def alquilar_auto(dias_alquiler):
    costo_diario = 40
    total_alquiler = dias_alquiler * costo_diario
    if 3 <= dias_alquiler <=6:
        descuento = (total_alquiler * 20 ) / 100
        total_alquiler = total_alquiler - descuento
        return total_alquiler
    elif dias_alquiler >= 7:
        total_alquiler = total_alquiler / 2
        return total_alquiler
print(alquilar_auto(3))
print(alquilar_auto(7))
    