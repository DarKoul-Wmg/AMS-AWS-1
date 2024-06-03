
public class PersonalServicio extends Personas { //hijo de persona (herencia)

	private String tipoServicio;
	
	public PersonalServicio() {
		super();
		
	}
	
	public PersonalServicio(String dni, String nombre, String apellido,String tipoServicio) {
		super(dni, nombre, apellido);
		this.tipoServicio = tipoServicio;
		
	}

//	@Override
//	public String toString() { //polimorfismo: reescribir metodos que se heredan
//		return super.toString() + "tipoServicio: "+tipoServicio;
//		
//	}
	
	@Override
	public String toString() { //polimorfismo: reescribir metodos que se heredan
		return super.toString() + "		"+tipoServicio;
		
	}
}
