
public class ClaseA { //definicion de la variable que vpy a crear (las variables de dentro son atributos)
	String atributo1 = "valor1";
	String atributo2 = "valor2";
	
	//Constructor es lo primero que se ejecuta al instanciar una clase:
	
//	ClaseA(){
//		
//	}
//	
//	ClaseA(String atributo1,String atributo2){ //Constructor, cuando se crea uno siempre tiene que estar el que hay por defecto
//		this.atributo1 = atributo1;
//		this.atributo2 = atributo2;
//		
//	}
	
//	ClaseA(String atributo1){
//		this.atributo1 = atributo1;
//		
//	}
	
	public void metodo1(String atributo1) { //funcion que no devuelve nada "void"
		this.atributo1 = atributo1; //this señala el atributo1 de la clase, el segundo es el que pasa la funcion
		
	}
	
//---------------------------------------------------------------------------------------------------------------------------------------------
		//SOURCE-GENERATE-CONSTRUCTOR USING FIELDS
	public ClaseA() {
		super();
	}
	
	public ClaseA(String atributo1, String atributo2) {
		super();
		this.atributo1 = atributo1;
		this.atributo2 = atributo2;
	}


	public void metodo2(String atributo2) { 
		this.atributo2 = atributo2; 

		//SOURCE-GENERATE-GETTERS AND SETTERS
	}
	public String getAtributo1() {
		return atributo1;
	}

	public void setAtributo1(String atributo1) {
		this.atributo1 = atributo1;
	}

	public String getAtributo2() {
		return atributo2;
	}

	public void setAtributo2(String atributo2) {
		this.atributo2 = atributo2;
	}
//_________________________________________________________________________________________________________________________________
	public String metodo_muestra_estados() {
		String cadenita = "Atributo1 = "+atributo1+"\nAtributo2 = "+atributo2+"\n";
		return cadenita;
	}
	
}
