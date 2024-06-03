package pt44_ArrayList;

import java.util.ArrayList;

public abstract class Figura44 {
	private String color;
	
	
	//constructores
	public Figura44(String color) {
		super();
		this.color = color;

	}
	public Figura44() {
		super();
	}
	
	//setGet
	public String getColor() {
		return color;
	}
	
	public void setColor(String color) {
		this.color = color;;
	}
	
	//metodos
	
	public abstract float calcularArea();
}


// ===================

class Triangle extends Figura44{
	private float base;
	private float altura;
	
	// Constr
	public Triangle() {
		super();
	}
	
	public Triangle(String color, float base, float altura) {
		super(color);
		this.base = base;
		this.altura = altura;
	}

	// setGet
	public float getBase() {
		return base;
	}

	public void setBase(float base) {
		this.base = base;
	}

	public float getAltura() {
		return altura;
	}

	public void setAltura(float altura) {
		this.altura = altura;
	}

	//metodos
	public float calcularArea() {
		return (base*altura)/2;
	}
	
}


//===================

class Cercle extends Figura44{
	private float radio;
	
	//Constr
	public Cercle() {
		super();
	}
	
	public Cercle(String color, float radio) {
		super(color);
		this.radio = radio;
	}
	
	//getSet
	public float getRadio() {
		return radio;
	}

	public void setRadio(float radio) {
		this.radio = radio;
	}
	
	//metod
	public float calcularArea() {
		return (float) (Math.PI * (radio*radio));
	}
	
}

//===================
class Quadrat extends Figura44{
	private float costat;
		
	// constr
	public Quadrat(String color, float costat) {
		super(color);
		this.costat = costat;
	}

	public Quadrat() {
		super();
	}
	
	//setget
	
	public float getCostat() {
		return costat;
	}

	public void setCostat(float costat) {
		this.costat = costat;
	}
	
	// metod
	public float calcularArea() {
		
		return costat * costat;
	}
}

//===================

class FrmFigures{
	private ArrayList<Figura44> llistaFigures;
	
	private int numCercles;
	private int numTriangles;
	private int numQuadrats;
	
	// Constr
	public FrmFigures() { //inicia arraylist y contadores
		llistaFigures = new ArrayList<>(10);
		numCercles = 0;
		numTriangles = 0;
		numQuadrats = 0;
		
	}
	
	public void afegirFigura(Figura44 figura) {
		
		if (llistaFigures.size() < 10) { //si tamaño inferior a 10, añade
			llistaFigures.add(figura);
			
			//suma contadores
			if (figura instanceof Cercle) {
				numCercles++;
			} else if (figura instanceof Triangle) {
				numTriangles++;
			} else if (figura instanceof Quadrat) {
				numQuadrats++;
			}	
			System.out.println("Figura añadida");
			
		}else {
			System.out.println("Lista llena");
		}
	}
	
	public float sumarAreasCirculos() {
		float areaTotal = 0;
		
		for (Figura44 figura : llistaFigures) {
			if (figura instanceof Cercle) {
				areaTotal += figura.calcularArea();
			}
		}	
		return areaTotal;
	}
	
	//gets para obtener contadores

	public int getNumCercles() {
		return numCercles;
	}

	public int getNumTriangles() {
		return numTriangles;
	}

	public int getNumQuadrats() {
		return numQuadrats;
	}
}