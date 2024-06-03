
public class Hdd {
	private int capacidad;
	private String tipo;
	private int precio;
	
	//Constr
	
	public Hdd(String tipo, int capacidad, int precio) {
		this.capacidad = capacidad;
		this.tipo = tipo;
		this.precio = precio;
	}
	
	//GetSet
	public int getCapacidad() {
		return capacidad;
	}

	public void setCapacidad(int capacidad) {
		this.capacidad = capacidad;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public int getPrecio() {
		return precio;
	}

	public void setPrecio(int precio) {
		this.precio = precio;
	}

	//toString
	public String toString() {
		return "\n\nHDD \n\nCapacidad=" + capacidad + "\nTipo=" + tipo + "\nPrecio=" + precio+"\n";
	}
	
	
	
}
