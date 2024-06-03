import java.util.Scanner;
public class Ex3_decimals {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		double[] decimals = new double[10];
		double num = 0;
		
		for (int i = 0; i < decimals.length; i++) {
			
			System.out.println("Introduce un numero decimal");
			num = sc.nextDouble();
			decimals[i] = num;
			sc.nextLine();
			//System.out.println(i);
		}
		
		for (int i = 0; i < decimals.length; i++) {
			//System.out.println(i);
			System.out.println(decimals[i]);
		}
		
		
//		// EX4
		double buscar = 0;
		double sus = 0;
		System.out.println("Introduce un numero a buscar:");
		buscar = sc.nextDouble();
		sc.nextLine();
		
		for (int i = 0; i<decimals.length;i++) {
			if (buscar == decimals[i]){
				System.out.println("El numero " + buscar + " se encuentra en la lista de decimales");
				System.out.println("Introduce el numero para sustituir:");
				sus = sc.nextDouble();
				sc.nextLine();	
				decimals[i] = sus;
			}
		}
		

	}

}

