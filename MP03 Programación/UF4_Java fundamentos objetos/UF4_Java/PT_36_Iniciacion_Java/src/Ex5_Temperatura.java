import java.util.Scanner;
public class Ex5_Temperatura {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Introduce una temperatura en grados Fahrenheit: ");
		float faren = Float.parseFloat(sc.nextLine());
		
		float celsi = (5f/9f) * (faren-32); 
		
		System.out.println("La temperatura en Celsius es: "+celsi);
	}

}
