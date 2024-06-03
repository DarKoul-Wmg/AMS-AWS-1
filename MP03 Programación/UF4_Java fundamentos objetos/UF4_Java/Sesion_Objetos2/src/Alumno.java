
public class Alumno extends Personas {
	private float uf1;
	private float uf2;
	private float uf3;
	
	//constructores
	public Alumno(String dni, String nombre, String apellido) {
		super(dni, nombre, apellido);
		
		
	}

	public Alumno() {
		super();
	}
	

	public void setUf1(float uf1) {
		this.uf1 = uf1;
	}
	public float getUf2() {
		return uf2;
	}
	public void setUf2(float uf2) {
		this.uf2 = uf2;
	}
	public float getUf3() {
		return uf3;
	}
	
	public void setUf3(float uf3) {
		this.uf3 = uf3;
	}
	
	//SOBRECARGA (definimos el mismo metodo varias veces pero con diferentes parametros, tienen comportamiento diferente)
	public void setNotas(float uf1) {
		this.uf1 = uf1;
	} 
	
	public void setNotas(float uf1,float uf2) {
		this.uf1 = uf1;
		this.uf2 = uf2;
	}
	
	public void setNotas(float uf1,float uf2,float uf3) {
		this.uf1 = uf1;
		this.uf2 = uf2;
		this.uf3 = uf3;
	} 

//	@Override
//	public String toString() {
//		return "Alumno: "+ nombre+"\n" +"apellido: "+apellido+"\n" + "dni: "+dni+"\n"+"uf1: " + uf1 + "\n" +"uf2: " + uf2+"\n"+ "uf3: " +uf3;
//	}
	@Override
	public String toString() {
		return super.toString()+"  		"+"NotaUF1: " +uf1 + "  		" + "NotaUF2: "+ uf2+"  		"+"NotaUF3: "+uf3;
	}
	
}
