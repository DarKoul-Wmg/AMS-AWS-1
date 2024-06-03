import java.util.Scanner;

public class Ex4_diners_a_pagar {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Introduce el capital inicial:");
		
		float capital = Float.parseFloat(sc.nextLine()); //Transforma la string del input en un float
		
		System.out.println("Introduce la tasa de intereses: ");
		float intereses = Float.parseFloat(sc.nextLine());
		
		System.out.println("Introduce los años a calcular");
		float anyo = Float.parseFloat(sc.nextLine());
		
		float diners_a_pagar = capital* (float)Math.pow((1 + intereses/100),anyo); //Definir resultado de math.pow como float.
		System.out.println("La cantidad a pagar es: "+diners_a_pagar);

	}
}
