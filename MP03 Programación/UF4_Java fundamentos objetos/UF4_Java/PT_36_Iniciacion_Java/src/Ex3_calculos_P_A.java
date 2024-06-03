import java.util.Scanner;
import java.lang.Math;

public class Ex3_calculos_P_A {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//A
		{
			System.out.println("Introduce la base y la altura del rectangulo separadas por un espacio: ");
			int base = sc.nextInt();
			int altura = sc.nextInt();
			sc.nextLine();
			
			System.out.println("El perimetro del rectangulo es: "+ (2*base + 2*altura));
			System.out.println("El area del rectangulo es: "+ (base*altura));
			}
		
		//B
		{
			System.out.println("\nIntroduce el radio de un circulo: ");
			float radio = sc.nextFloat();	
			
			System.out.println("El perimetro del circulo es: "+ (2*Math.PI*radio));
			System.out.println("El area del circulo es: "+ (Math.PI*(radio*radio)));
			
		}
		
		{// C/D
			System.out.println("\nIntroduce el radio de una esfera: ");
			float radio = sc.nextFloat();	
			
			System.out.println("El volumen de la esfera es: "+(4/3*Math.PI*(Math.pow(radio, 3)))); //Para hacer potencias: Math.pow(num,potencia)
		}
		
		
	}

}
