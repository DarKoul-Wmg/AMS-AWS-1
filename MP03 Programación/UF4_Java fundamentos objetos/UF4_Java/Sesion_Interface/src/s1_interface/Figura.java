package s1_interface;

public abstract class Figura implements VariablesFiguras {
	public abstract float calculoArea();
	public abstract float calculoPerimetro();
}


class Cuadrado extends Figura{
	private float lado;
	

	public Cuadrado(float lado) {
		super();
		this.lado = lado;
	}

	public float calculoArea() {
		
		return lado * lado;
	}

	public float calculoPerimetro() {
	
		return lado * 4;
	}
}

class Circulo extends Figura{
	private float radio;
	
	public Circulo(float radio) {
		super();
		this.radio = radio;
	}

	public float calculoArea() {
		
		return (float) (MIPI * (radio*radio));
	}

	public float calculoPerimetro() {
		
		return (float) (2*MIPI * radio);
	}
}

class Cubo extends Figura implements Figura3D{
	private float lado;
	

	public Cubo(float lado) {
		super();
		this.lado = lado;
	}

	public float calculoArea() {
		
		return 6 * lado * lado;
	}

	public float calculoPerimetro() {
	
		return 3 * lado * 4;
	}


	public float calculoVolumen() {
		return lado * lado *lado;
	}
}

class Cilindro extends Figura implements Figura3D {
	private float radio;
	private float altura;
	
	public Cilindro(float radio, float altura) {
		super();
		this.radio = radio;
		this.altura = altura;
	}

	public float calculoArea() {
		
		return (float) (2*MIPI * radio*altura);
	}

	public float calculoPerimetro() {
	
		return (float) (2*MIPI * radio);
	}

	
	public float calculoVolumen() {
		
		return (float) (MIPI * altura * (radio * radio));
	}
	
}