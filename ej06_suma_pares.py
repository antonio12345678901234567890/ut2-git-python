limite = int(input("Suma los pares hasta: "))

suma = 0

for x in range(1, limite + 1):
    if (x % 2 == 0):
        suma += x

print(f"La suma de los pares es: {suma}")