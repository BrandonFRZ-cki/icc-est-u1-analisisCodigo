import java.util.Random;

public class Benchmarking {
    private MetodosOrdenamiento metodosOrdenamiento;
    public Benchmarking() {
        long inicioMillis = System.currentTimeMillis();
        long inicioNano = System.nanoTime();
        System.out.println(inicioMillis);
        System.out.println(inicioNano);

        metodosOrdenamiento = new MetodosOrdenamiento();

        int[] arreglo = generarArregloAleatorio(1000000);
        Runnable tarea = () -> metodosOrdenamiento.burbujaTradicional(arreglo);

        double nanoTime = medirConNanoTime(tarea);
        System.out.println("Medicion con nano →  "+nanoTime + " segundos");
        double currentTime= medirCurrentTime(tarea);
        System.out.println("Medicion con Current → " +currentTime + " segundos");
    }
    // // Tiempo usando nanoTime (en segundos)
    public double medirConNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio)/1_000_000_000.0;
    }
    public double medirCurrentTime(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio)/1000.0;
    }
    private int[] generarArregloAleatorio(int tam) {
        int[] arreglo = new int[tam];
        Random random = new Random();
        for (int j = 0; j < tam; j++) {
            arreglo[j] = random.nextInt( 100_000);
        }
        return arreglo;
    }
}
