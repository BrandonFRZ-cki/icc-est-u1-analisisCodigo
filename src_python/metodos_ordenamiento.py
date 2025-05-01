class MetodosOrdenamiento:
    def sortByBubble(self,arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i] > arreglo[j]:
                    arreglo [i],arreglo[j] = arreglo[j],arreglo[i]
        return arreglo
    
    def sort_seleccion(self, array):
        array = array.copy()
        n=len(array)
        for i in range(n):
            min = i
            for j in range(i+1,n):
                if(array[j] < array[min]):
                    min= j
            if(min!=i):
                array[i],array[min]=array[min],array[i]
        return array

