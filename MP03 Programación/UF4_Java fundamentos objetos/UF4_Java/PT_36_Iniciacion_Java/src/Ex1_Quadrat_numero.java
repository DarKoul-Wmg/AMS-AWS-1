import java.util.Scanner;


public class Ex1_Quadrat_numero {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int num;
		
		System.out.println("Dona un numero per calcular el seu quadrat: ");
		num = sc.nextInt();
		
		System.out.println("El quadrat del numero donat es: " + (num*num));
	}
}
