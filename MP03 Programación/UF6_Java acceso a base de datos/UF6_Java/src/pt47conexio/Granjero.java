package pt47conexio;

public class Granjero implements Comparable<Granjero> {
	private int id;
	private String nombre;
	private String descripcion = "estandar";
	private int dinero;
	private int puntos;
	private int nivel;
	
	public Granjero(int id, String nombre, String descripcion, int dinero, int puntos, int nivel) {
		super();
		this.id = id;
		this.nombre = nombre;
		this.descripcion = descripcion;
		this.dinero = dinero;
		this.puntos = puntos;
		this.nivel = nivel;
	}

	
	// getset
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public int getDinero() {
		return dinero;
	}

	public void setDinero(int dinero) {
		this.dinero = dinero;
	}

	public int getPuntos() {
		return puntos;
	}

	public void setPuntos(int puntos) {
		this.puntos = puntos;
	}

	public int getNivel() {
		return nivel;
	}

	public void setNivel(int nivel) {
		this.nivel = nivel;
	}


	//comparable
	public int compareTo(Granjero g) {
		return this.getDinero() - g.getDinero() ;
	}
	
}

