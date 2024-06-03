package apuntesUF6;

public class Player {
	private int id;
	private String dni;
	private String name;
	private int points;
	private int idPais;
	public Player(int id, String dni, String name, int points, int idPais) {
		super();
		this.id = id;
		this.dni = dni;
		this.name = name;
		this.points = points;
		this.idPais = idPais;
	}
	
	
	public Player()
	{
		
	}


	public int getId() {
		return id;
	}


	public void setId(int id) {
		this.id = id;
	}


	public String getDni() {
		return dni;
	}


	public void setDni(String dni) {
		this.dni = dni;
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public int getPoints() {
		return points;
	}


	public void setPoints(int points) {
		this.points = points;
	}


	public int getIdPais() {
		return idPais;
	}


	public void setIdPais(int idPais) {
		this.idPais = idPais;
	}
	
	
	
	
	
}
