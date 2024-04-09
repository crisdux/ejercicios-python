# │ Dados dos valores numéricos de entrada así como un operador (como símbolo string) calcule el resultado de la operación.           │
# │                                                                                                                                   │
# │ NOTAS:                                                                                                                            │
# │                                                                                                                                   │
# │  • Utilice la sentencia match-case.                                                                                               │
# │  • En caso de que la operación no sea suma, resta, multiplicación o división, el resultado debe ser None.

def simple_op(num1, num2, op):
    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "_":
            return None
        
print(simple_op(5,2,"+"))
print(simple_op(5,2,"-"))
print(simple_op(5,2,"*"))
print(simple_op(5,2,"/"))
print(simple_op(5,2,"&"))