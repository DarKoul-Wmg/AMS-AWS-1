package pt_Automoviles_Comparator;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Main_Automoviles {

	public static void main(String[] args) {
		 automovil a1 = new automovil(2000,180,4000);
		 automovil a2 = new automovil(1500,140,3600);
		 automovil a3 = new automovil(2500,220,2000);
		 automovil a4 = new automovil(2300,130,6000);
		 ArrayList<automovil> automoviles = new ArrayList<automovil>();
		 automoviles.add(a1);
		 automoviles.add(a2);
		 automoviles.add(a3);
		 automoviles.add(a4);
		 System.out.println(automoviles);
		 Collections.sort(automoviles);
		 System.out.println("**********cilindrada***********");
		 System.out.println(automoviles);
		 Collections.sort(automoviles, new SortBySpeed());
		 System.out.println("**********velocidad***********");
		 System.out.println(automoviles);
		 
		 
		 Comparator c = new Comparator<automovil>() {
			 public int compare(automovil arg0, automovil arg1) {
				 return arg0.capacidadMaletero - arg1.capacidadMaletero;
			 }
		 };
		 
		 Collections.sort(automoviles,c);
		 System.out.println("**********Maletero***********");
		 System.out.println(automoviles);

	}

}

class SortBySpeed implements Comparator<automovil>{
	public int compare(automovil  arg0, automovil arg1) {
		return arg0.velMaxima - arg1.velMaxima;
	}
}




//la clase automovil implementa Comparable, para establecer un criterio de ordenacion, que en este caso será la cilindrada
class automovil implements Comparable<automovil>{
	public int cilindrada;
	public int velMaxima;
	public int capacidadMaletero;
 
	public automovil(int cilindrada, int velMaxima, int capacidadMaletero) {
		super();
		this.cilindrada = cilindrada;
		this.velMaxima = velMaxima;
     	this.capacidadMaletero = capacidadMaletero;
	}

	public String toString() {
     return "Cilindrada = " + cilindrada + ", velMaxima = " + velMaxima + " capacidadMaletero = "
             + capacidadMaletero + "\n";
	}

 // ordenaremos los automoviles por cilindrada
	public int compareTo(automovil au) {
     return this.cilindrada - au.cilindrada;
	}
}
