# Ejecutar BenchMarking
#import benchmarking as Ben

from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    size = 10000
    
    benchM = Benchmarking
    metodosOr = MetodosOrdenamiento

    arreglo = benchM.build_arreglo(size)

    
    metodos = { # Diccionario 
        "bubuja": metodosOr.sortByBubble,
        "seleccion": metodosOr.sort_seleccion,
    }
    resultados = []
    
    for nombre, metodo in metodos.items():# como un foreach que devuelve la clave,  valor
        tiempo = Benchmarking.medir_tiempo(metodo, arreglo)
        tuplaResultado = (size,nombre,tiempo)
        resultados.append(tuplaResultado)
    for resultado in resultados:
        size, nombre, tiempo = resultado
        print(f"Tamaño: {size}, Nombre: {nombre}, Tiempo: {tiempo:.6f} segundos")

