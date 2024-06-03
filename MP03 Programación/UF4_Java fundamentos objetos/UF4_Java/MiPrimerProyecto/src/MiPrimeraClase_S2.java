import java.util.Scanner;

public class MiPrimeraClase_S2 {

	public static void main(String[] args) {
		
		// CLASE 2-----------------
		
		int numero = 1000; //declarar para que no pete en el if
		
		Scanner sc = new Scanner(System.in); //import java.util.Scanner;
		
		System.out.println("Introduce algo:\n");
		String consola =" ";
		//System.out.println("Introduce un numero:\n");
		
		//System.out.println(sc.hasNextInt());
//		while (!sc.hasNextInt()) {
//			System.out.println("No has introducido un numero");
//			System.out.println("Introduce un numero");
//			sc.nextLine();//Consumimos buffer para salir del bucle infinito (hay que volver a pedir un valor)
//		}
//		numero = sc.nextInt();
		
		/*
		 * if (sc.hasNextInt()) { numero = sc.nextInt(); } else {
		 * System.out.println("No has introducido un numero"); }
		 */
		// int numero = sc.nextInt(); pedir datos, el dato tiene que ser del mismo tipo, sino error
		
		consola = sc.next();
		System.out.println("En consola "+consola);
		consola = sc.next();
		System.out.println("En consola "+consola);
		consola = sc.next();
		System.out.println("En consola "+consola);
		//System.out.println("Has introducido "+numero);
		System.out.println("FIN PROGRAMA");
	}
}

