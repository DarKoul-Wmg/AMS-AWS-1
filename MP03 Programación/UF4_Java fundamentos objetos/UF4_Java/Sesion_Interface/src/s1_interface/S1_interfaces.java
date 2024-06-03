package s1_interface;

import java.util.ArrayList;

public class S1_interfaces {

	public static void main(String[] args) {
		
		ArrayList<Figura> figuras= new ArrayList<Figura>();
		figuras.add(new Cuadrado(1));
		figuras.add(new Circulo(1));
		figuras.add(new Cuadrado(2));
		figuras.add(new Circulo(2));
		figuras.add(new Cilindro(2,2));
		figuras.add(new Cubo(2));
		
		Cubo c = new Cubo(2);
		System.out.println(c instanceof Figura3D);
		System.out.println(c instanceof Figura);
		
		
		Circulo ci = new Circulo(2);
		System.out.println(ci instanceof Figura3D);
		System.out.println(ci instanceof Figura);
		
		for (Figura figura : figuras) {
			System.out.println("**********************");
			//System.out.println("Area = "+figura.calculoArea());
			//System.out.println("Perimetro = "+figura.calculoPerimetro());
			Figura3D.print("Area = "+figura.calculoArea());
			Figura3D.print("Area = "+figura.calculoPerimetro());
			if (figura instanceof Figura3D) {
				System.out.println("Volumen = "+((Figura3D) figura).calculoVolumen());
			}
			
				
		}
	}

}
