import java.util.Scanner;

public class Ex1_Calculadora {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int opc = 0;
		boolean salir = false;
		
		
		while (salir != true) {
			System.out.println("CALCULADORA\nMenu Principal\n\n1-Sumar\n2-Restar\n"
					+ "3-Multiplicar\n4-Dividir\n0-Sortir\n\nOpció: ");
			
			//valida que el input sea num
			while (!sc.hasNextInt()){
				System.out.println("No has introducido un numero, mete uno nuevo:");
				sc.nextLine();
				}
			
			opc = sc.nextInt();
			if (opc == 0){
				System.out.println("Adios");
				salir = true;
			
			} else if(opc == 1){
				int num1 = 0;
				int num2 = 0;
				int suma = 0;
			System.out.println("Introduce un numero: ");
			num1 = sc.nextInt();
			
			System.out.println("Introduce el segundo numero: ");
			num2 = sc.nextInt();
			
			suma = num1 + num2;
			System.out.println("La suma es: "+suma+"\n");
			
			} else if(opc == 2){
				int num1 = 0;
				int num2 = 0;
				int resta = 0;
			System.out.println("Introduce un numero: ");
			num1 = sc.nextInt();
			System.out.println("Introduce el segundo numero: ");
			num2 = sc.nextInt();
			
			resta = num1 - num2;
			System.out.println("La resta es: "+resta+"\n");
			
			} else if(opc == 3){
				int num1 = 0;
				int num2 = 0;
				int multi = 0;
			System.out.println("Introduce un numero: ");
			num1 = sc.nextInt();
			System.out.println("Introduce el segundo numero: ");
			num2 = sc.nextInt();
			
			multi = num1 * num2;
			System.out.println("La multiplicacion es: "+multi+"\n");
			
			} else if(opc == 4) {
				int num1 = 0;
				int num2 = 0;
				int div = 0;
			System.out.println("Introduce un numero:\n");
			num1 = sc.nextInt();
			System.out.println("Introduce el segundo numero:\n");
			num2 = sc.nextInt();
			while (num2 == 0) {
				System.out.println("No se puede dividir entre 0, mete otro valor:\n");
				sc.nextLine();
				num2 = sc.nextInt();
				}
			
			div = num1 / num2;
			System.out.println("La division es: "+div+"\n");
			
			}else {
				System.out.println("Elige una opcion del menu");
			}
		}
	}
}

