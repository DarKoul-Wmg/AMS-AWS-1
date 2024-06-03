
public class Bateria {
	private String modelo;
	private int capacidad;
	private int nivelBateria;
	private int precio;
	
	//Constr
	public Bateria(String modelo, int capacidad, int nivelBateria, int precio) {
		super();
		this.modelo = modelo;
		this.capacidad = capacidad;
		this.nivelBateria = nivelBateria;
		this.precio = precio;
	}
	
	//GetSet
	public String getModelo() {
		return modelo;
	}
	
	public void setModelo(String modelo) {
		this.modelo = modelo;
	}
	public int getCapacidad() {
		return capacidad;
	}
	public void setCapacidad(int capacidad) {
		this.capacidad = capacidad;
	}
	public int getNivelBateria() {
		return nivelBateria;
	}
	public void setNivelBateria(int nivelBateria) {
		this.nivelBateria = nivelBateria;
	}
	public int getPrecio() {
		return precio;
	}
	public void setPrecio(int precio) {
		this.precio = precio;
	}

	//toString
	public String toString() {
		return "\nBATERIA \n\nCapacidad=" + capacidad + "\nNivelBateria=" + nivelBateria+ "\nModelo=" + modelo +"\nPrecio="
				+ precio+"\n";
	}
	
	
	
	
	
}
