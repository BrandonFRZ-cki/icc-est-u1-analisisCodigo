# Ejecutar BenchMarking

import matplotlib.pyplot as plt
import random
import time

from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    resultados = []
    tamanios = [500, 1000, 2000]

    for tam in tamanios:
        benchM = Benchmarking()
        metodosOr = MetodosOrdenamiento()

        arreglo = benchM.build_arreglo(tam)

        metodos = {  # Diccionario
            "burbuja": metodosOr.sortByBubble,
            "seleccion": metodosOr.sort_seleccion,
        }

        for nombre, metodo in metodos.items():  
            tiempo = benchM.medir_tiempo(metodo, arreglo)  
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)

        for resultado in resultados:
            tam, nombre, tiempo = resultado
            print(f"Tamaño: {tam}, Nombre: {nombre}, Tiempo: {tiempo:.6f} segundos")

    tiempos_by_metodo = {
        "burbuja": [],
        "seleccion": [],
    }

    # Clasificar los métodos según el tiempo
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    # Crear una gráfica
    plt.figure(figsize=(10, 6))

    # Gráfica de tiempos para cada método
    for nombre, tiempo in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempo, label=nombre, marker='o')

    plt.grid()
    plt.legend()
    plt.show()