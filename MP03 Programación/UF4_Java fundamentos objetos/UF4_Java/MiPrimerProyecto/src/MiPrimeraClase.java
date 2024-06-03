import java.util.Scanner;

public class MiPrimeraClase {

	public static void main(String[] args) {
		
		int var = 25;
		float var1 = (float)2.34;
		double var2 = 34.345;
		String var3 = "lalalalala";
		boolean var4 = true;
		
		char caracter = 'A'; //Para definir un char tiene que ser si o si con ' en vez de "
		
		int i =1;
		i++; //suma uno siempre
		
		// resolucion problema X
		String cadena1 = "Soy la cadena1";
		String cadena2 = "Soy la cadena2";
		{
			System.out.println("var1 = "+var1);
			System.out.println("var2 = "+var1);
			System.out.println(cadena1+cadena2);
			System.out.println(cadena1+var4+var1+var2);
			System.out.println(i);
		}
		
		int x = 0;
		//System.out.println(1/x);
		if (x!=0 & 1/x > 0) {
			System.out.println("Hola");
		}
		System.out.println("Fin");
		
		int y = 0;
		int c = 0;
		c = x++ + y; // si x++ primero se hace la suma de x+y y luego se suma 1
		c = ++x + y; // si ++x primero se suma 1 y luego hace la suma de x+y
		System.out.println(c);
		System.out.println("X = "+x);
		//Comentario
		
		/*
		 * comentario
		 * comentario
		 * comentario
		 */
		
	}
}

