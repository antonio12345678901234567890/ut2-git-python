nota = float(input('Dame una de tus notas'))
calificacion = ""

print(nota[0])

if nota < 0 or nota > 10:
    calificacion = "Nota no valida"
elif (0 <= nota < 5):
    calificacion = "Insuficiente"
elif (5 <= nota < 6):
    calificacion = "Suficiente"
elif (6 <= nota < 7):
    calificacion = "Bien"
elif (7 <= nota < 9):
    calificacion = "Notable"
elif (9 <= nota <= 10):
    calificacion = "Sobresaliente"

print(f"Calificacion: {calificacion}")

