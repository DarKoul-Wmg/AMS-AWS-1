import java.util.Scanner;

public class Ex6_operaciones {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Introduce dos enteros separados por un espacio");
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		sc.nextLine();
		while (num2 == 0) {
			System.out.println("No se puede dividir entre 0, mete otro valor para num 2:\n");
			sc.nextLine();
			num2 = sc.nextInt();
			}
		
		System.out.println("La suma de los numeros da: "+(num1+num2));
		System.out.println("La resta de los numeros da: "+(num1-num2));
		System.out.println("La multiplicación de los numeros da: "+(num1*num2));
		System.out.println("La división de los numeros da: "+(float)num1/(float)num2);
		
	}
}
