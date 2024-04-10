# Complete the function which returns the weekday according to the input number:

# 1 returns "Sunday"
# 2 returns "Monday"
# 3 returns "Tuesday"
# 4 returns "Wednesday"
# 5 returns "Thursday"
# 6 returns "Friday"
# 7 returns "Saturday"
# Otherwise returns "Wrong, please enter a number between 1 and 7"

def regresa_dia(num_dia):
    match(num_dia):
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wendnesday"
        case 5:
            return "Thrusday"
        case 6:
            return "Friday"
        case 7:
            return "saturday"
        case _:
            return "Numero de dia no valido"

print(regresa_dia(1))
print(regresa_dia(5))
print(regresa_dia(-1))