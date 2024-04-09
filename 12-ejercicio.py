#  Determine el primer y el último dígito de una cadena de texto dada.

def first_last_digit(text):
    digitos = []
    for item in text:
        if item.isdigit():
            digitos.append(item)
    return f"{digitos[0]} - {digitos[-1]}"
            
    
print(first_last_digit("1abc2"))
print(first_last_digit("pqr3stu8vwx"))
print(first_last_digit("a1b2c3d4e5f"))
print(first_last_digit("treb7uchet"))
