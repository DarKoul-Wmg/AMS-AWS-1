package pt43_Classes_Abstractas;

public class Ex1_classesAbstractes {
	
}

abstract class Empleado{
	private String nom;
	private String ciutat;
	private String lloc;
	
	//CONSTRUCTORES
	public Empleado(String nom, String ciutat, String lloc) {
		super();
		this.nom = nom;
		this.ciutat = ciutat;
		this.lloc = lloc;
	}

	public Empleado() {
		super();
	}

	//GETTERS Y SETTERS
	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getCiutat() {
		return ciutat;
	}

	public void setCiutat(String ciutat) {
		this.ciutat = ciutat;
	}

	public String getLloc() {
		return lloc;
	}

	public void setLloc(String lloc) {
		this.lloc = lloc;
	}
	
	//	METODOS
	
	public abstract String lloc();
	
	public abstract String ciutatO();
	
	public abstract float salariDiari();

	
	public String toString() {
		return "Nombre = " + nom + "\nCiutat de origen = " + ciutat + "\nlloc = " + lloc + "\n";
	}
	
	

}


class Caixer extends Empleado{
	private int hores_treballades;

	//CONSTRUCTORES
	public Caixer() {
		super();
		
	}

	public Caixer(String nom, String ciutat, String lloc, int hores_treballades) {
		super(nom, ciutat, lloc);
		this.hores_treballades = hores_treballades;
	}
	
	//GETTERS AND SETTERS
	
	public int getHores_treballades() {
		return hores_treballades;
	}

	public void setHores_treballades(int hores_treballades) {
		this.hores_treballades = hores_treballades;
	}
	
	//METODOS
	public float horesTreballades(){
		return hores_treballades;
	}
	
	public float salariDiari() {
		float salari = hores_treballades* 15; 
		return salari;
	}

	public String lloc() {
		return getLloc();
	}

	public String ciutatO() {
		return getCiutat();
	}
	
	
	public String toString() {
		return super.toString()+"Hores_treballades = " + hores_treballades + "\n";
	}

}

class Neteja extends Empleado{

	//CONSTRUCTORES
	public Neteja() {
		super();
		
	}

	public Neteja(String nom, String ciutat, String lloc) {
		super(nom, ciutat, lloc);
		
	}
	//GETTERS AND SETTERS
	
	
	
	//METODOS
	public float salariDiari() {
		return (float) 35.00;
	}

	
	public String lloc() {
		// TODO Auto-generated method stub
		return getLloc();
	}


	public String ciutatO() {
		// TODO Auto-generated method stub
		return getCiutat();
	}
	
	
}

class Mostrador extends Empleado{
	private float vendes;
	
	
	//CONSTRUCTORES
	public Mostrador() {
		super();
		
	}

	public Mostrador(String nom, String ciutat, String lloc,float vendes) {
		super(nom, ciutat, lloc);
		this.vendes = vendes;
	}
	
	
	//GETTERS AND SETTERS
	
	public float getVendes() {
		return vendes;
	}

	public void setVendes(float vendes) {
		this.vendes = vendes;
	}
	
	//METODOS
	
	public float salariDiari() {
		float salari = (float) (50 + (vendes * 0.15));
		return salari;
	}

	public String lloc() {
		// TODO Auto-generated method stub
		return getLloc();
	}

	
	public String ciutatO() {
		// TODO Auto-generated method stub
		return getCiutat();
	}
	
	public String toString() {
		return super.toString()+"Vendes =" + vendes + "\n";
	}

	
}



