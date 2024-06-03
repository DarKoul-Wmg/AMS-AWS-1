package pt47conexio;

import java.util.Comparator;

public class OrdenarDinero implements Comparator<Granjero>{

	
	public int compare(Granjero g1, Granjero g2) {
	
		return g2.getDinero() - g1.getDinero();
	}

}
