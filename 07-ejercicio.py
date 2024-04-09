# No te puedes dormir, pero afortunadamente un programa Python te ayuda a ello. Dado un número entero num_sheeps devuelve la cuenta
# de las ovejas...

def count_sheeps(num_sheeps):
    if num_sheeps == 0:
        return ""
    return f"sheep..."*num_sheeps

print(count_sheeps(3)) ## sheep...sheep...sheep...
print(count_sheeps(0)) ## ""
print(count_sheeps(7)) ## sheep...sheep...sheep...sheep...sheep...sheep...sheep...
    
    