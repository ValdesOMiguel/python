# Problema:
# Dado un string formado por (), [] y {}, escribir un programa que indique si los pares correspondientes son correctos.

# Entrada: [()]{}{[()()]()} (Correcta)
# Entrada: [(]) (Incorrecta)

# Strings a evaluar
a = '(())'
b = '[()]{}{[()()]()}'
c = '[(])'

# Estructuras de comparacion
# Diccionario
db = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
}

# Lista de apertura
op = ['(','[','{']

# Definicion de stack
stack = []

# Funcion para separar string
def split(string):
    return list(string)

# Funcion para determinar stack vacio
def empty(stack):
    return len(stack)==0

#Funcion de validacion
def validation(string,db,op,stack):
    string = split(string)
    for character in string:
        if(character in op):
            stack.append(character)
        else:
            temp = stack.pop()
            if (db[temp] != character):
                stack.clear()
                return print("Error, bracket does not match => \'"  + temp + "\' - \'" + character+"\'")
    if not empty(stack):
        print("Error, stack not empty, character found : " + stack.pop())
        stack.clear()

#Ejecucion
# validation(string,dictionary,openingList,stack)
validation(a,db,op,stack)
validation(b,db,op,stack)
validation(c,db,op,stack)

# End
