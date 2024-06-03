package pt47conexio;

import java.util.Comparator;

public class OrdenarNombre implements Comparator<Granjero> {


	public int compare(Granjero g1, Granjero g2) {
		
		return g1.getNombre().compareToIgnoreCase(g2.getNombre());
	}

}
