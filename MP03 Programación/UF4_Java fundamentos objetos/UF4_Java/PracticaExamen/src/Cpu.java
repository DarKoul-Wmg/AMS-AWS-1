
public class Cpu {
	
	private String modelo;
	private int velocidad;
	private int numeroNucleos;
	private int precio;
	
	//Constr
	
	public Cpu(String modelo, int velocidad, int numeroNucleos, int precio) {
		this.modelo = modelo;
		this.velocidad = velocidad;
		this.numeroNucleos = numeroNucleos;
		this.precio = precio;
	}
	
	//GetSet
	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public int getVelocidad() {
		return velocidad;
	}

	public void setVelocidad(int velocidad) {
		this.velocidad = velocidad;
	}

	public int getNumeroNucleos() {
		return numeroNucleos;
	}

	public void setNumeroNucleos(int numeroNucleos) {
		this.numeroNucleos = numeroNucleos;
	}

	public int getPrecio() {
		return precio;
	}

	public void setPrecio(int precio) {
		this.precio = precio;
	}
	
	//toString

	public String toString() {
		return "\nCPU \n\nVelocidad=" + velocidad + "\nNumeroNucleos=" + numeroNucleos + "\nModelo=" + modelo +"\nPrecio="
				+ precio+"\n";
	}
	
	
	
	
	
}
