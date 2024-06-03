package pt41_Implementacio_Classes;

public class Ex2_facultad {
	public static void main(String[] args) {
		

	}
}

class Persona2{
	private String nom;
	private String cognom;
	private String dni;
	private String estatCivil;
	
	public Persona2(String nom, String cognom, String dni, String estatCivil) {
		super();
		this.nom = nom;
		this.cognom = cognom;
		this.dni = dni;
		this.estatCivil = estatCivil;
	}
	
	public Persona2() {
		super();
	}
	public String getNom() {
		return nom;
	}
	public String getCognom() {
		return cognom;
	}
	public String getDni() {
		return dni;
	}
	public String getEstatCivil() {
		return estatCivil;
	}	
}

class Empleado extends Persona2{
	private int anio;
	private int num_despatx;
	
	public Empleado() {
		super();
	
	}
	public Empleado(String nom, String cognom, String dni, String estatCivil, int anio, int num_despatx) {
		super(nom, cognom, dni, estatCivil);
		this.anio = anio;
		this.num_despatx = num_despatx;
	}
	
	public int getAnio() {
		return anio;
	}
	
	public int getNum_despatx() {
		return num_despatx;
	}
	
	
}

class Estudiants extends Persona2{
	private String curs;

	public Estudiants() {
		super();
		
	}

	public Estudiants(String nom, String cognom, String dni, String estatCivil, String curs) {
		super(nom, cognom, dni, estatCivil);
		this.curs = curs;
	}

	public String getCurs() {
		return curs;
	}
}

class Professors extends Empleado{
	private String departament;

	public Professors() {
		super();
		
	}

	public Professors(String nom, String cognom, String dni, String estatCivil, int anio, int num_despatx, String departament) {
		super(nom, cognom, dni, estatCivil, anio, num_despatx);
		this.departament = departament;
	}

	public String getDepartament() {
		return departament;
	}
}

class Personal_Serveis extends Empleado{
	private String seccio;
	
	public Personal_Serveis() {
		super();
	}
	public Personal_Serveis(String nom, String cognom, String dni, String estatCivil, int anio, int num_despatx, String seccio) {
		super(nom, cognom, dni, estatCivil, anio, num_despatx);
		this.seccio = seccio;
	}
	public String getSeccio() {
		return seccio;
	}
}
