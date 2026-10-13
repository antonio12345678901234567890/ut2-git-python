nota = float(input('Dame una de tus notas'))
calificacion = ""

if (nota < 5):
    calificacion = "Suspenso"
elif (5 <= nota < 7):
    calificacion = "Aprobado"
elif (7 <= nota < 9):
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

print(f"Calificacion: {calificacion}")

