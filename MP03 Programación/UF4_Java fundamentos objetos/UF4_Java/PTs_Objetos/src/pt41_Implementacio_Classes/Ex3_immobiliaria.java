package pt41_Implementacio_Classes;

public class Ex3_immobiliaria {

	public static void main(String[] args) {

	}
}

class Inmoble{
	
	private String adreça;
	private float metres;
	private String estat;
	private float preu;
	private int edadInmueble;
	
	public Inmoble(String adreça, float metres, String estat, float preu,int edadInmueble) {
		super();
		this.adreça = adreça;
		this.metres = metres;
		this.estat = estat;
		this.preu = preu;
		this.edadInmueble = edadInmueble;
		
	}
	
	public Inmoble() {
		super();
	}

	public String getAdreça() {
		return adreça;
	}

	public float getMetres() {
		return metres;
	}

	public String getEstat() {
		return estat;
	}

	public float getPreu() {
		return preu;
	}

	public int getEdadInmueble() {
		return edadInmueble;
	}
	
	public float PrecioInmoble(int edadInmueble, float preu) {
		float precioBase = preu;
		
		if (edadInmueble < 15) {
			precioBase = (float) (precioBase - (precioBase * 0.01));
			
		}if (edadInmueble > 15) {
			precioBase = (float) (precioBase - (precioBase * 0.02));
			
		}
		return precioBase;
	}
	
}

class Local extends Inmoble{
	private int finestres;

	public Local() {
		super();
		
	}

	public Local(String adreça, float metres, String estat,float preu,int edadInmueble, int finestres) {
		super(adreça, metres, estat, preu, edadInmueble);
		this.finestres = finestres;
	}

	public int getFinestres() {
		return finestres;
	}
	
	public float PrecioLocal(float preu, int finestres, float metres) {
		float precioLocal = preu;
		
		if (metres > 50) {
			precioLocal = (float) (precioLocal + (precioLocal * 0.01));
			
		}if (finestres > 4) {
			precioLocal = (float) (precioLocal + (precioLocal * 0.02));
			
		}if (finestres <= 1){
			precioLocal = (float) (precioLocal - (precioLocal * 0.02));
		}
		return precioLocal;
	}
	
}

class Pisos extends Inmoble{
	private String piso;

	public Pisos() {
		super();
		
	}

	public Pisos(String adreça, float metres, String estat, float preu, int edadInmueble, String piso) {
		super(adreça, metres, estat, preu, edadInmueble);
		this.piso = piso;
	}

	public String getPiso() {
		return piso;
	}
	
	
	
}
