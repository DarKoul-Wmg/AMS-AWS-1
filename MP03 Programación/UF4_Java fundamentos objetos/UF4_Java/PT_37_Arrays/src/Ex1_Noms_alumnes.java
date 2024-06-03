import java.util.Scanner;
public class Ex1_Noms_alumnes {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] alumnes = new String[10];
		String nom = "";
		
		for (int i = 0; i < alumnes.length; i++) {
			
			System.out.println("Introduce un nombre");
			nom = sc.nextLine();
			alumnes[i] = nom;
			//System.out.println(i);
		}
		
		for (int i = 0; i < alumnes.length; i++) {
			//System.out.println(i);
			System.out.println(alumnes[i]);
		}
		
		
		// EX2
		String buscar ="";
		System.out.println("Introduce un nombre a buscar:");
		buscar = sc.nextLine();
		
		for (int i = 0; i<alumnes.length;i++) {
			if (buscar.equalsIgnoreCase(alumnes[i])){
				System.out.println("El nombre " + buscar + " se encuentra en la lista de nombres");
				
			}
		}
		

	}

}
