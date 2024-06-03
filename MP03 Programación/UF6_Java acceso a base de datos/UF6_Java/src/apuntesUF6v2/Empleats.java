package apuntesUF6v2;

public class Empleats {
	private int id;
	private String nombre;
	private String descripcion = " ";
	private int dinero;
	private int puntos;
	private int nivel;
	
	public Empleats(int id, String nombre, String descripcion, int dinero, int puntos, int nivel) {
		super();
		this.id = id;
		this.nombre = nombre;
		this.descripcion = descripcion;
		this.dinero = dinero;
		this.puntos = puntos;
		this.nivel = nivel;
	}

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

	
	public String toString() {
		return "id=" + id + "\nnombre=" + nombre + "\ndescripcion=" + descripcion + "\ndinero=" + dinero
				+ "\npuntos=" + puntos + "\nnivel=" + nivel + "\n";
	}
	
	
	
}
