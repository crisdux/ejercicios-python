#  Sabiendo que la longitud de una lista se calcula igual que la longitud de una cadena de texto, obtenga el número de palabras que  ││ contiene una cadena de texto dada. 

def num_words(text):
    text_list = text.split()
    return len(text_list)
        
print(num_words('Before software can be reusable it first has to be usable'))
    