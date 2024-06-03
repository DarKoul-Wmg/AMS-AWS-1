package PT46_compare;

public class Persona implements Comparable<Persona> {
	String nombre;
	int edad;
	int altura;
	public Persona(String nombre, int edad, int altura) {
		this.nombre = nombre;
		this.edad = edad;
		this.altura = altura;
	}
	
	public String toString() {
		return "Nombre = " + nombre + ", altura = " + altura + ", edad = " + edad +  "\n";
	}
	
	public int getEdad() {
		return edad;
	}
	public void setEdad(int edad) {
		this.edad = edad;
	}
	public int getAltura() {
		return altura;
	}
	public void setAltura(int altura) {
		this.altura = altura;
	}
	
	public int compareTo(Persona p) {
		return  p.getAltura() - this.altura;
	}
	
	
	
	
	
}
