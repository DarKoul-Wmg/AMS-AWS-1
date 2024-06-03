import java.util.Scanner;

public class ScannerRepaso {
	public static void main(String[] args) {
		int numero;
		Scanner sc = new Scanner(System.in);
		
//		System.out.println("Dame un numero:\n");
//		System.out.println(sc.hasNextInt());
//		numero = sc.nextInt();
//		System.out.println(numero);
//		System.out.println("***************");
//		System.out.println(sc.hasNextInt());
//		numero = sc.nextInt();
//		System.out.println(numero);
		
		
//		System.out.println("Dame un numero:\n");
//		while(!sc.hasNextInt()) {
//			System.out.println("Dame un numero:\n");
//			sc.nextLine();
//			
//		}
//		numero = sc.nextInt();
//		System.out.println(numero);
		
		do {
			System.out.println("Dame un numero:\n");
			if (!sc.hasNextInt()) {
				sc.nextLine();
			}
		} while(!sc.hasNextInt());
		numero = sc.nextInt();
		System.out.println(numero);	
		
	}
}

