import random
intentos = 0
numeroGenerado = random.randint(1, 20)

while True:
    numero = int(input('Escriba un numero a ver si aciertas (1- 20)'))
    if (numero == numeroGenerado):
        intentos += 1
        print('Adivinaste el número!!')
        break
    else:
        intentos += 1
        if (numero < numeroGenerado):
            print("El número es mayor")
        else:
            print("El número es menor")

print(f"Han hecho falta {intentos} intentos.")

