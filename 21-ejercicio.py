# human_years >=1 y solo numeros

# Cat years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that

# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

def calculo_anios_gato(human_years):
    anios_gato = 0
    for edad in range(1, human_years+1):
        if edad == 1:
            anios_gato += 15
        if edad == 2:
            anios_gato += 9
        if edad >=3:
            anios_gato +=4
    return anios_gato
    
def calculo_anios_perro(human_years):
    anios_perro = 0
    for edad in range(1, human_years+1):
        if edad == 1:
            anios_perro += 15
        if edad == 2:
            anios_perro += 9
        if edad >=3:
            anios_perro +=5
    return anios_perro
    
    
def human_years_cat_years_dog_years(human_years):
    return [human_years, calculo_anios_gato(human_years), calculo_anios_perro(human_years)]
    
print(human_years_cat_years_dog_years(10)) # [10,56,64]
