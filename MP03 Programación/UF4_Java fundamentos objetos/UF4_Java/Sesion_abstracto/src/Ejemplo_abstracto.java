
public class Ejemplo_abstracto {
	public static void main(String[] args) {
		
		Figura[] misFiguras = new Figura[5];
		misFiguras[0] = new Cuadrado(10);
		misFiguras[1] = new Circulo(2);
		
//		Figura a = new Figura(); // NO DEJA INSTANCIAR UNA CLASE ABSTRACTA 
	}
}

abstract class Figura{
	private int posx;
	private int posy;
	
	public abstract float CalculoArea();
}

class Cuadrado extends Figura{
	float lado;
	public float getPerimetro(){
		return 4*lado;
	}
	
	public float getArea(){
		return lado * lado;
	}

	public Cuadrado(float lado) {
		super();
		this.lado = lado;
	}

	//METODO NO IMPLEMENTADO (OBLIGA PARA QUE FUNCIONE)
	public float CalculoArea() {
		return lado * lado;
	}
	
}

class Circulo extends Figura{
	float radio;
	public float permietroCirculo(){
		return (float) (2*Math.PI*radio);
	}
	
	public float areaCirculo(){
		return (float) (2*Math.PI*radio*radio);
	}

	public Circulo(float radio) {
		super();
		this.radio = radio;
	}

	//METODO NO IMPLEMENTADO (OBLIGA PARA QUE FUNCIONE)
	public float CalculoArea() {
		return (float) (2*Math.PI*radio*radio);
	}
	
}