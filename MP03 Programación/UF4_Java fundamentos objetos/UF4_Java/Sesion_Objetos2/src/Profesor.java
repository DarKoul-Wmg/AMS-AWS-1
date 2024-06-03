import java.util.Arrays;

public class Profesor extends Personas {
	private String cargo;
	private String[] modulos;
	private String cadena_modulos = "";
	
	
	public Profesor(String dni, String nombre, String apellido, String cargo, String[] modulos) {
		super(dni, nombre, apellido);
		
		this.cargo = cargo;
		this.modulos = modulos;	
	
		for (int i = 0; i<modulos.length;i++) {
			cadena_modulos = cadena_modulos + " " +modulos[i];
		
		}
	}


	@Override
	public String toString() {
		return super.toString() +"		"+"Cargo: "+cargo+"  		"+"Modulo: "+cadena_modulos;
	}
	
}
