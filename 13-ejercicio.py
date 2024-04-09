def bisiesto(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

print(bisiesto(1900))
print(bisiesto(1904))
print(bisiesto(1983))
print(bisiesto(1992))
print(bisiesto(2000))