# Problema:
#     Dado un texto, determinar el numero de veces que se repite cada palabra

a = "Este. este es El texto! QUE estare, ComParanDo. lo estare? utilizando. utiliZando Estare este teXto Previamente asiGnado. Sacando Al MoxiTo QuE Llevo Dentro"

print (a)

# Funcion para normalizar todas las palabras. Eliminamos minusculas y signos de puntuacion
def normalize(word):
    to_remove = ["!","?",",","."]
    for character in to_remove:
        word = word.replace(character,'')
    return word.lower()


# Definir un diccionario
myDict = {}
myDict.clear()

# Separacion de palabras
a = normalize(a)
a = a.split(" ")

# Procesamiento
for word in a:
    if word in myDict:
        myDict[word] = myDict[word]+1
    else:
        myDict.setdefault(word,1)

# Resultados
print("Word -> Number of appearances")
for key,value in myDict.items():
    print('{:<11s}{:>6d}'.format(key,value))

#