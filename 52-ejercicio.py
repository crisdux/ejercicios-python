# En este kata tendrás que escribir una función que tome litresy price_per_litre( en dólares ) como argumentos.

# Las compras de 2 o más litros obtienen un descuento de 5 céntimos por litro, las compras de 4 o más litros obtienen un descuento de 10 céntimos por litro, y así sucesivamente cada dos litros, hasta un descuento máximo de 25 céntimos por litro. Pero el descuento total por litro no puede ser superior a 25 céntimos. Devuelve el coste total redondeado a 2 decimales. También puedes adivinar que no habrá entradas negativas o no numéricas.

# ¡Buena suerte!


def fuel_price(litres, price_per_litre):
    if not (isinstance(litres, int) or isinstance(litres, float)) or litres <= 0:
        print("La cantidad de litros debe ser mayor a 0 y un numero")
        return
    if not (isinstance(price_per_litre, int) or isinstance(price_per_litre, float)) or price_per_litre <= 0:
        print("Precio por litro debe ser mayor a 0 y un numero")
        return
    
    precio_sin_descuento = litres * price_per_litre
    descuento = 0
    if litres < 2:
        return precio_sin_descuento
    if litres >= 2 and litres < 4:
        descuento = (5 * litres) / 100 
        return precio_sin_descuento - descuento
    if litres >=4 and litres < 6:
        descuento = (10 * litres) / 100 
        return precio_sin_descuento - descuento
    if litres >=6 and litres < 8:
        descuento = (15 * litres) / 100 
        return precio_sin_descuento - descuento
    if litres >=8 and litres < 10:
        descuento = (20 * litres) / 100 
        return precio_sin_descuento - descuento
    if litres >= 10:
        descuento = (25 * litres) / 100 
        return precio_sin_descuento - descuento
    
print(fuel_price(15, 5.83))
