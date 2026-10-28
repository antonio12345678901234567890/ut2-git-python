numero = input('Introduce un número:')

if (numero.isdigit()):
    #Autor: Compañero
    if int(numero) % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")