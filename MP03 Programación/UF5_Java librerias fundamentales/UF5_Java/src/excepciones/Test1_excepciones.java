package excepciones;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.Scanner;


//ArithmeticException
//InputMismatchException
public class Test1_excepciones {
	
	public static void main(String[] args) {
		Test1_excepciones te = new Test1_excepciones();
		
		try {
			te.metodoB(); //Propagación de excepciones, del metodo A pasa al metodo B, y del B pasa al main 
			} catch (MiExcepcion e) {
			
			System.out.println("--------------------");	
			System.out.println(e.getMessage());	
			System.out.println("--------------------");	
		}
		
//		try { //como el metodo peude lanzar excepciones, hay que meterlo en un bloque try catch
//			te.metodoA();
//		} catch (MiExcepcion e) {
//			
//			System.out.println("--------------------");	
//			System.out.println(e.getMessage());	
//			System.out.println("--------------------");	
//		}

//		try {
//			Scanner sc = new Scanner(System.in);
//			System.out.println("Dame un numero:\n");
//			int n = sc.nextInt();
//			System.out.println("Has introducido "+n);
//			System.out.println("Vamos a dividir 1 entre "+n);
//			
//			if (n < 10) {
//				throw new MiExcepcion("El numero es menos que 10"); // new ppara instanciar la clase mi exception
//			}
//			System.out.println("Resultado = "+1/n);
//			System.out.println("Fin de bloque try");
//		
//		}catch (InputMismatchException e) {
//			
//			System.out.println("Ha ocurrido un error del tipo InputMismatch exceprion");
//
//		
//		}catch (Exception e) {
//			
//		
//		//e.printStackTrace();
//		System.out.println("Ha ocurrido un generico Exception error");
//		System.out.println("Mensaje = "+ e.getMessage());
//	
//		
//		}finally { //Siempre entramos en el bloque finally
//			System.out.println("Entramos en el bucle finally");
//		}
		
		System.out.println("Fin del programa");
		
	}
	public void metodoC() throws FileNotFoundException { //Te pide si o si declarar el FileFoundException
		File f = new File("Fichero.txt");
		Scanner sc = new Scanner(f);
	}
	
	
	public void metodoB() throws MiExcepcion { //Como llama al metodo A, hay que indicar que puede lanzar excepciones
		metodoA();
	}
	
	public void metodoA() throws MiExcepcion{ //Sin el try catch, hay que indicar que el metodo lanza excepciones
		Scanner sc = new Scanner(System.in);
		System.out.println("Dame un numero:\n");
		int n = sc.nextInt();
		System.out.println("Has introducido "+n);
		System.out.println("Vamos a dividir 1 entre "+n);
		
		if (n < 10) {
			
			throw new MiExcepcion("El numero es menos que 10"); // new para instanciar la clase mi exception
		}
		System.out.println("Resultado = "+1/n);
		System.out.println("Fin de bloque try");
	};

}

class MiExcepcion extends Exception{
	
	public MiExcepcion(String message){
		super(message);
		
	}
	
	public MiExcepcion(){
		System.out.println("Mensaje de MiExcepcion indeterminado");
		
	}
	
}
