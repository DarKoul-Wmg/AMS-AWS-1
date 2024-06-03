package PT46_compare;

import java.util.ArrayList;
import java.util.Collections;

public class Main_46 {

	public static void main(String[] args) {
		ArrayList<Persona> Personas = new ArrayList<Persona>();
		
		Persona dani = new Persona("Dani",22,187);
		Persona pol = new Persona("Pol",52,173);
		Persona manel = new Persona("Manel",27,158);
		Persona david = new Persona("David",25,164);
		Persona pere = new Persona("Pere",80,184);
		
		Personas.add(dani);
		Personas.add(pol);
		Personas.add(manel);
		Personas.add(david);
		Personas.add(pere);
		
		System.out.println(Personas.toString());
		System.out.println("----------------------");
		
		Collections.sort(Personas);
		
		for (Persona persona : Personas) {
			System.out.println(persona);
		}

	}

}



