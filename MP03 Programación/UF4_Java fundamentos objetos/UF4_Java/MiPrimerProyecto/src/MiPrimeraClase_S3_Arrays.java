import java.util.Scanner;


public class MiPrimeraClase_S3_Arrays {

	public static void main(String[] args) {
		
		
		
		//b entre 30 y 70: margen de 40 numeros
				//for (int i=0; i<=10; i++) { //es como un for i in range de 10
					
					//b = ((int) (40*Math.random()) + 30);
					//System.out.println(b);
				//}
		
		float a = (float) Math.random();
//		//System.out.println(a);
		int b = (int) (50*Math.random());
		int[] array = {1,2,3,4,5};
//		System.out.println(Arrays.toString(array));
		
//		
//		//b entre 30 y 70: margen de 40 numeros
//		for (int i=0; i<=10; i++) { //es como un for i in range de 10
//			
//			b = ((int) (40*Math.random()) + 30);
//			System.out.println(b);
//		}
//		int nombreDelArray[] = new int[10]; //int es el tipo de dato para almacenar,puede ser float string,...
//		System.out.println(nombreDelArray.length);
//		for (int i=0; i<nombreDelArray.length; i++) {
//			//System.out.println("Elemento "+ i +" = "+nombreDelArray[i]);
//			nombreDelArray[i] = (int) (50*Math.random());
//			
//		}
//		for (int i=0; i<nombreDelArray.length; i++) {
//			System.out.println("Elemento "+ i +" = "+nombreDelArray[i]);
//			//b = (int) (50*Math.random());
//			
//		}
//		
//		//Metodo de la burbuja en Java
//		
//		for (int pasadas=0; pasadas<nombreDelArray.length -1; pasadas++) {
//			for (int i=0; i<nombreDelArray.length-1-pasadas; i++) {
//				if (nombreDelArray[i] < nombreDelArray[i+1]) {
//					int aux = nombreDelArray[i];
//					nombreDelArray[i] = nombreDelArray[i+1];
//					nombreDelArray[i+1] = aux;	
//				}
//			}
//		}
		
//		int nombreDelArray[] = {1,2,3,4,5,6,7,8,9,10};
//		
//		int nombreDelArray1[];
//		nombreDelArray1 = nombreDelArray; //Array1 es un puntero a Array, eso quiere decir que al modificar un elemento de array1, lo hace en array 
//		
//		nombreDelArray1[0] = 5000;
		
//		
//		
//		for (int i=0; i<nombreDelArray.length; i++) {
//			//System.out.println("Elemento "+ i +" = "+nombreDelArray[i]);
//			System.out.printf("%5d",i);
//		}
		
//		int x = (int) (50*Math.random());
//		
//		//b entre 30 y 70: margen de 40 numeros
//		for (int i=0; i<=10; i++) { //es como un for i in range de 10
//			
//			b = ((int) (40*Math.random()) + 30);
//			System.out.println(b);
//		}

		
		
		
		
		int nombreDelArray[][] = new int[5][3];
//		System.out.println(nombreDelArray.length);
//		System.out.println(nombreDelArray[0].length);
		
		for (int i=0; i<nombreDelArray.length; i++) {
			for (int j=0; j<nombreDelArray[0].length; j++) {
				nombreDelArray[i][j] = (int) (50*Math.random());
			}
		}
		
// ORDENAR POR FILAS
		for (int fila=0; fila<nombreDelArray.length; fila++) {
			for (int pasada=0; pasada<nombreDelArray[0].length-1; pasada++) {
				for (int i=0; i<nombreDelArray[0].length-1-pasada; i++) {
					if (nombreDelArray[fila][i] < nombreDelArray[fila][i+1]) {
						int aux = nombreDelArray[fila][i];
						nombreDelArray[fila][i] = nombreDelArray[fila][i+1];
						nombreDelArray[fila][i+1] = aux;	
					}
				}
			}
		}

		System.out.println("\nMatriz con filas ordenadas");
		for (int i=0; i<nombreDelArray.length; i++) {
			for (int j=0; j<nombreDelArray[0].length; j++) {
				System.out.printf("%5d",nombreDelArray[i][j]);
			}
			System.out.println();
		}
// ORDENAR POR COLUMNAS
		
		for (int columna=0; columna<nombreDelArray[0].length; columna++) {
			for (int pasada=0; pasada<nombreDelArray.length-1; pasada++) {
				for (int i=0; i<nombreDelArray.length-1-pasada; i++) {
					if (nombreDelArray[i][columna] < nombreDelArray[i+1][columna]) {
						int aux = nombreDelArray[i][columna];
						nombreDelArray[i][columna] = nombreDelArray[i+1][columna];
						nombreDelArray[i+1][columna] = aux;	
					}
				}
			}
		}
		 
		System.out.println("\nMatriz con columnas ordenadas");
		for (int i=0; i<nombreDelArray.length; i++) {
			for (int j=0; j<nombreDelArray[0].length; j++) {
				System.out.printf("%5d",nombreDelArray[i][j]);
			}
			System.out.println();
		}
		
	}
}

