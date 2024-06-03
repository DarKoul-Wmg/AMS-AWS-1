
public class Ex6_IntercanviValors {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// Inicialización de las variables
        int numA = 5;
        int numB = 17;

        // Mostrar los valores iniciales por pantalla
        System.out.println("Valores iniciales:");
        System.out.println("numA: " + numA);
        System.out.println("numB: " + numB);

        // Intercambio de valores usando una variable temporal
        int temp = numA; // Guardamos el valor original de numA en una variable temporal
        numA = numB;     // Asignamos el valor de numB a numA
        numB = temp;     // Asignamos el valor original de numA (guardado en temp) a numB

        // Mostrar los valores después del intercambio por pantalla
        System.out.println("\nValores después del intercambio:");
        System.out.println("numA: " + numA);
        System.out.println("numB: " + numB);

	}

}
