
public class Ram {
	private int capacidad;
	private String modelo;
	private int precio;
	
	//Constr
	
	public Ram(String modelo, int capacidad, int precio) {
		this.capacidad = capacidad;
		this.modelo = modelo;
		this.precio = precio;
	}
	
	
	//GetSet
	public int getCapacidad() {
		return capacidad;
	}

	public void setCapacidad(int capacidad) {
		this.capacidad = capacidad;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public int getPrecio() {
		return precio;
	}

	public void setPrecio(int precio) {
		this.precio = precio;
	}


	//toString
	public String toString() {
		return "\nRAM \n\nCapacidad=" + capacidad + "\nModelo=" + modelo + "\nPrecio=" + precio+"\n";
	}
	
	
	
	
}
