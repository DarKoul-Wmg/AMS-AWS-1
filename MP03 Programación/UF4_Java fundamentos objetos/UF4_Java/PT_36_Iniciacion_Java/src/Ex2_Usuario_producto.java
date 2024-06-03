import java.util.Scanner;

public class Ex2_Usuario_producto {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Introdueix el teu nom: ");
		String nom = sc.nextLine();
		System.out.println("Bon dia, "+ nom+"\nIntrodueix dos numeros separats per un espai :");
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		
		System.out.println("El producte dels dos nuemros donats es: "+ (num1*num2));
		
	}

}
