import java.util.Scanner;

public class Ex1_Calculadora2_switch {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int opc = 0;
		boolean salir = false;
		String buffer = "";
		
		
		while (salir != true) {
			System.out.println("CALCULADORA\nMenu Principal\n\n1-Sumar\n2-Restar\n"
					+ "3-Multiplicar\n4-Dividir\n0-Sortir\n\nOpció: ");
			
			//valida que el input sea num
			while (!sc.hasNextInt()){
				System.out.println("No has introducido un numero, mete una opcion valida:");
				sc.nextLine();
				}
			opc = sc.nextInt();
			//buffer += sc.nextLine();
			int num1 = 0;
			int num2 = 0;
			float resultado;
			
			switch (opc) {
				case 0:
					sc.nextLine();
					System.out.println("Adios");
					salir = true;
					break;
				
				case 1:
					sc.nextLine();
					System.out.println("Introduce un numero: ");
					while (!sc.hasNextInt()){
						System.out.println("No has introducido un numero, mete uno nuevo:");
						sc.next();
						}
					num1 = sc.nextInt();
					sc.nextLine();
			
					System.out.println("Introduce el segundo numero: ");
					while (!sc.hasNextInt()){
						System.out.println("No has introducido un numero, mete uno nuevo:");
						sc.next();
						}
					num2 = sc.nextInt();
					sc.nextLine();
			
					resultado = num1 + num2;
					System.out.println("La suma es: "+resultado+"\n");
					break;
				
				case 2:
					sc.nextLine();
					System.out.println("Introduce un numero: ");
					while (!sc.hasNextInt()){
						System.out.println("No has introducido un numero, mete uno nuevo:");
						sc.next();
						}
					num1 = sc.nextInt();
					sc.nextLine();
					System.out.println("Introduce el segundo numero: ");
					while (!sc.hasNextInt()){
						System.out.println("No has introducido un numero, mete uno nuevo:");
						sc.next();
						}
					num2 = sc.nextInt();
					sc.nextLine();
			
					resultado = num1 - num2;
					System.out.println("La resta es: "+resultado+"\n");
					break;
					
				case 3:
					sc.nextLine();
					System.out.println("Introduce un numero: ");
					num1 = sc.nextInt();
					sc.nextLine();
					while (!sc.hasNextInt()){
						System.out.println("No has introducido un numero, mete uno nuevo:");
						sc.next();
						}
					System.out.println("Introduce el segundo numero: ");
					while (!sc.hasNextInt()){
						System.out.println("No has introducido un numero, mete uno nuevo:");
						sc.next();
						}
					num2 = sc.nextInt();
					sc.nextLine();
				
					resultado = num1 * num2;
					System.out.println("La multiplicacion es: "+resultado+"\n");
					break;
				
				case 4:
					sc.nextLine();
					System.out.println("Introduce un numero:\n");
					while (!sc.hasNextInt()){
						System.out.println("No has introducido un numero, mete uno nuevo:");
						sc.next();
						}
					num1 = sc.nextInt();
					sc.nextLine();
					System.out.println("Introduce el segundo numero:\n");
					while (!sc.hasNextInt()){
						System.out.println("No has introducido un numero, mete uno nuevo:");
						sc.next();
						}
					num2 = sc.nextInt();
					sc.nextLine();
					resultado = num1 / num2;
					System.out.println("La division es: "+resultado+"\n");
					break;
					
				default:
					System.out.println("Elige una opcion del menu");
					break;
			}	
		}
	}
}

