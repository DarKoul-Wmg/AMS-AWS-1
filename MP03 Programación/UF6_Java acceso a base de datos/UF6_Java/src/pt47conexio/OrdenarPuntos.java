package pt47conexio;

import java.util.Comparator;

public class OrdenarPuntos implements Comparator<Granjero> {

	
	public int compare(Granjero g1, Granjero g2) {
		
		return g1.getPuntos() - g2.getPuntos();
	}

}
