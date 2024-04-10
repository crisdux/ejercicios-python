# # Hay una oferta "3 por 2" (o "2+1" si lo desea) en mangos. Para una cantidad y precio determinados (por mango), calcule el costo total de los mangos.

# mango(2, 3) ==> 6    # 2 mangoes for $3 per unit = $6; no mango for free
# mango(3, 3) ==> 6    # 2 mangoes for $3 per unit = $6; +1 mango for free
# mango(5, 3) ==> 12   # 4 mangoes for $3 per unit = $12; +1 mango for free
# mango(9, 5) ==> 30   # 6 mangoes for $5 per unit = $30; +3 mangoes for free

def ofertas_mango(cantidad_mangos, precio_unitario):
    cantidad_ofertas = cantidad_mangos // 3
    total = (cantidad_mangos * precio_unitario) - (cantidad_ofertas * precio_unitario)
    return f"{total} | mangos gratis: {cantidad_ofertas}"
    
print(ofertas_mango(2,3))
print(ofertas_mango(3,3))
print(ofertas_mango(5,3))
print(ofertas_mango(9,5))
