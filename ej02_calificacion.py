nota = float(input('Dame una de tus notas'))
calificacion = ""

if (0 <= nota < 5):
    calificacion = "Insuficiente"
elif (5 <= nota < 6):
    calificacion = "Suficiente"
elif (6 <= nota < 7):
    calificacion = "Bien"
elif (7 <= nota < 9):
    calificacion = "Notable"
elif (9 <= nota <= 10):
    calificacion = "Sobresaliente"
else:
    calificacion = "Nota no válida"

print(f"Calificacion: {calificacion}")

