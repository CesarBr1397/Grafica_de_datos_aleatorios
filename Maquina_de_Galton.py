import random
import matplotlib.pyplot as plt

canicas = 3001
num_niveles = 12

puntos_x = [i for i in range(canicas)]
puntos_y = []

for movimientos in range (canicas):
    posicion = 0

    for i in range (num_niveles):
        direcciones = random.choice([-1,1])
        posicion += direcciones

    puntos_y.append(posicion)

resultados = [puntos_y.count(i) for i in range(-num_niveles, num_niveles + 1)]

def graficar_histograma(resultados):
    plt.bar(range(len(resultados)), resultados)
    plt.xlabel('Contenedor Final')
    plt.ylabel('Número de Canicas')
    plt.title('Simulación de Máquina de Galton - Histograma')
    plt.show()
graficar_histograma(resultados)
