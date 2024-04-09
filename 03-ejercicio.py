# Se pide obtener el dígito de control de un NIF de entrada.
# https://www.interior.gob.es/opencms/ca/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/

def nif_digit(nif):
    dict_valores = {"0": "T", "1": "R", "2":"W", "3": "A", "4": "G", "5": "M",
        "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B", "12": "N", "13": "J",
        "14": "Z", "15": "S", "16": "Q", "17": "V", "18": "H", "19": "H", "20": "C", "21": "K", "22": "E"}
    index_nif = int(nif) % 23
    letra = dict_valores[str(index_nif)]
    return (f"{nif}{letra}")
    
print(nif_digit("78654355")) # 78654355J
print(nif_digit("65895421")) # 65895421F
print(nif_digit("43298006")) # 43298006T