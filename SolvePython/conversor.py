import bs4
import requests
import re
from datetime import date

##Some websites do not allow scraping. So you need to provide a header with user-agent specifying type of browser and the system which says it is a browser request and not some code trying to scrape
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

today = date.today()

#Entro a la página que quiero scrapear
myurl = 'https://www.investing.com/currencies/usd-mxn'
respuesta = requests.get(myurl,headers=headers)

soup = bs4.BeautifulSoup(respuesta.text , "html.parser")

#Seleciono el identificador que quiero
# Para seleccionarlo entro a la pagina e inspecciono el elemento
# Despues Clic derecho en el elemento de HTML y Copy Selector
# Si tiene un ID lo copiara, si no, copiara toda la cadena
dolarPeso = soup.select("#last_last")

# Normaliamos el dato
# Lo convierto a float
dolarPeso = str(dolarPeso[0].text)
# Reemplazo la , por el punto para convertir en float
dolarPeso    = dolarPeso.replace(",",".")
dolarPeso = float(dolarPeso)


#Funciones de conversion
def pesoToDolar(dolarPeso):
    pesos = float(input("Ingresa la cantidad de pesos: "))
    totalDolar = round(pesos / dolarPeso, 2)
    return [totalDolar,pesos]


def dolarToPeso(dolarPerso):
    dolar = float(input("Ingresa la cantidad de dolares: "))
    totalPesos = round(dolarPeso * dolar,2)
    return [totalPesos,dolar]

operacion = 4

def menu(operacion,today,dolarPeso):
    
    while(operacion != 3):
        print("""Precio de Dolar Hoy {} = ${}""".format(today,dolarPeso))
        operacion = int(input('''
            Ingresa el 1 o  2 según  el tipo de cambio:
                [1] Dolar a peso
                [2] Peso a dolar
                [3] Salir
            Selecciona: '''))
        print('********************************')
        if(operacion == 1):
            [total,entrada] = dolarToPeso(dolarPeso)
            print("\n${} Dolares equivalen a ${} Pesos\n".format(entrada,total))
        elif(operacion == 2):
            [total,entrada] = pesoToDolar(dolarPeso)
            print("\n${} Pesos equivalen a ${} Dolares\n".format(entrada,total))
        elif(operacion == 3):
            print("Bye Bye!")
            print('********************************')
            return 0
        elif(operacion != (1 or 2 or 3)):
            print("\n**Selecciona la opcion correcta**\n")
        
        
#Menu
menu(operacion,today,dolarPeso)