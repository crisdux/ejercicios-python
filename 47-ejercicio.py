# Los números que terminan en ceros son aburridos.

# Puede que sean divertidos en tu mundo, pero no aquí.

# Deshazte de ellos. Sólo los finales.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Solo Zero está bien, no te preocupes. Pobre chico de todos modos


def no_boring_zeros(num):
    if num == 0:
        return 0
    str_num = str(num)
    len_str_num = len(str_num)
    
    for i in range(0, len_str_num):
        ultimo_digito = num % 10
        if ultimo_digito == 0:
            num = str(num)
            num = num[0:-1]
            num = int(num)
    return num
            
    
# print(no_boring_zeros(1450))
print(no_boring_zeros(960000))
print(no_boring_zeros(-1050))
print(no_boring_zeros(0))