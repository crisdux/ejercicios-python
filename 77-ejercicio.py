# Defina String.prototype.toAlternatingCase(o una función/método similar como to_alternating_case // en el idioma seleccionado; consulte la solución inicial para obtener más detalles ) de manera que cada letra minúscula se convierta en mayúscula y cada letra mayúscula se convierta en minúscula toAlternatingCase. Por ejemplo:ToAlternatingCase

# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

def to_alternating_case(text):
    res = ""
    for i in text:
        if i.islower():
            res += i.upper()
        elif i.isupper():
            res += i.lower()
        elif i == " ":
            res += " "
        elif i.isdigit():
            res += i
        else:
            res+= i
    return res     
print(to_alternating_case("hello world"))
print(to_alternating_case("HELLO WORLD"))
print(to_alternating_case("hello WORLD"))
print(to_alternating_case("HeLLo WoRLD"))
print(to_alternating_case("12345"))
print(to_alternating_case("1a2b3c4d5e"))
print(to_alternating_case("String.prototype.toAlternatingCase"))
    