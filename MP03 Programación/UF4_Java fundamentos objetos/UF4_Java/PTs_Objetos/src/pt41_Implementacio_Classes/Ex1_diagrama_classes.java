package pt41_Implementacio_Classes;


public class Ex1_diagrama_classes {

	public static void main(String[] args) {
		Persona[] instituto = new Persona[5];
		instituto[0] = new Alumno("Alguien", "Algo alguno", "11111111h", "AWS1", "AWS1.1");
		instituto[1] = new Profesor("Lucas", "Algo alguno", "11111111h",30000, "AWS1",35);
		instituto[2] = new Administrativo("Esther", "rrrrr ñññññ", "11111111h",40000);
		for (int i =0; i< instituto.length;i++) {
			if (instituto[i] != null) {
				System.out.println(instituto[i]);
			}
		}
		System.out.println("Solo profes");
		for (int i =0; i< instituto.length;i++) {
			if (instituto[i] instanceof Profesor) {
				System.out.println(instituto[i]);
				System.out.println("Sueldo = "+((Profesor)instituto[i]).getSueldo()); //Se necesita parsear para acceder a getsueldo de profesor
			}
		}
	}
}

class Persona{
	private String nombre;
	private String apellidos;
	private String nif;
	
	public Persona(String nombre, String apellidos, String nif) {
		super();
		this.nombre = nombre;
		this.apellidos = apellidos;
		this.nif = nif;
	}

	public String toString() {
		return "Nombre = " + nombre + "\nApellidos = " + apellidos +", \nNIF=" + nif + "\n";
	}

	public String getNombre() {
		return nombre;
	}

	public String getApellidos() {
		return apellidos;
	}

	public String getNif() {
		return nif;
	}
	
	
}

class Alumno extends Persona{
	private String ciclo;
	private String curso;
	public Alumno(String nombre, String apellidos, String nif, String ciclo, String curso) {
		super(nombre, apellidos, nif);
		this.ciclo= ciclo;
		this.curso= curso;
	}
	public Alumno(String nombre, String apellidos, String nif) {
		super(nombre, apellidos, nif);
	}
	
	
	public String getCiclo() {
		return ciclo;
	}
	public void setCiclo(String ciclo) {
		this.ciclo = ciclo;
	}
	public String getCurso() {
		return curso;
	}
	public void setCurso(String curso) {
		this.curso = curso;
	}
	
	public String toString() {
		return super.toString()+"Ciclo = "+ciclo+"\nCurso = "+curso+"\n";
	}
}

class Profesor extends Persona{
	private float sueldo;
	private String curso;
	private int numeroHoras;
	private String[] modulos = {"M1","M2","M3"};
	
	public Profesor(String nombre, String apellidos, String nif,float sueldo,String curso) {
		super(nombre, apellidos, nif);
		this.sueldo = sueldo;
		this.curso = curso;
		
	}
	public Profesor(String nombre, String apellidos, String nif,float sueldo,String curso,int numeroHoras) {
		super(nombre, apellidos, nif);
		this.sueldo = sueldo;
		this.curso = curso;
		this.numeroHoras = numeroHoras;
		
	}
	public float getSueldo() {
		return sueldo;
	}
	public String getCurso() {
		return curso;
	}
	public int getNumeroHoras() {
		return numeroHoras;
	}
	public void setNumeroHoras(int numeroHoras) {
		this.numeroHoras = numeroHoras;
	}
	public String toString() {
		String m = "Modulos = ";
		for(int i =0; i<modulos.length; i++) {
			if(i!=modulos.length-1) {
				m += modulos[i]+" - ";
			}else {
			m += modulos[i]+"\n";
		}
	}
		return super.toString()+m+"\nSueldo = "+sueldo+"\nNumero Horas = "+numeroHoras+"\n";
	}
}

class Administrativo extends Persona{
	private float sueldo;

	public Administrativo(String nombre, String apellidos, String nif) {
		super(nombre, apellidos, nif);
		// TODO Auto-generated constructor stub
	}
	
	public Administrativo(String nombre, String apellidos, String nif, float sueldo) {
		super(nombre, apellidos, nif);
		this.sueldo = sueldo;
	}

	public float getSueldo() {
		return sueldo;
	}
	public String toString() {
		return super.toString()+"Sueldo: "+sueldo+"\n";
	}
}