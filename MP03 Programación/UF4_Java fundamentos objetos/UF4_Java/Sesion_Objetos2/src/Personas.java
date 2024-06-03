
public class Personas {
	public static String variable = "lalalala"; //static hace que aunque no se instancie la clase, se puede llamar desde otras clases
	private String dni;
	private String nombre;
	private String apellido;
	
	//CONSTRUCTORES
	
	public Personas() {
		super();
	}
	public Personas(String dni, String nombre, String apellido) {
		super();
		this.dni = dni;
		this.nombre = nombre;
		this.apellido = apellido;
	}
	
	public static void Saludar() {
		System.out.println("Holaaaa");
		variable = "lelelele";
	}
	
	//SETS Y GETS
	public String getDni() {
		return dni;
	}
	public void setDni(String dni) {
		this.dni = dni;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getApellido() {
		return apellido;
	}
	public void setApellido(String apellido) {
		this.apellido = apellido;
	}
//	@Override
//	public String toString() {
//		return "Persona: "+ nombre+"\n"+"apellido: "+apellido+"\n"+"dni: "+dni+"\n";
//	}
	@Override
	public String toString() {
		return String.format("%-10s",nombre);
	}
	//return String.format(%npmbre,nombre)
	
}
