#  Combinando las teclas CTRL y ALT podemos conseguir muchos shortcuts (atajos de teclado) en sistemas tipo Linux.                   │
# │                                                                                                                                   │
# │ Se pide identificar las combinaciones de teclas indicando la función que realizan.

def shortcuts(key1, key2, key3):
    key1 = key1.upper()
    key2 = key2.upper()
    key3 = key3.upper()
    
    dict_values = {"0": "CTRL", "1": "ALT", "2":"F2", "3": "DEL"}
    
    if (key1 == dict_values["0"] and key2 == dict_values["1"] and key3 == "T"):
        return "open terminal"
    if (key1 == dict_values["0"] and key2 == dict_values["1"] and key3 == "L"):
        return "lock screen"
    if (key1 == dict_values["0"] and key2 == dict_values["1"] and key3 == "D"):
        return "show desktop"
    if (key1 == dict_values["1"] and key2 == dict_values["2"] and key3 == ""):
        return "run console"
    if (key1 == dict_values["0"] and key2 == "Q", key3 ==""):
        return "close window"
    if( key1 ==dict_values["0"] and key2 == dict_values["1"] and key3 == dict_values["3"]):
        return "log out"
print(shortcuts("CTRL", "ALT", "T"))