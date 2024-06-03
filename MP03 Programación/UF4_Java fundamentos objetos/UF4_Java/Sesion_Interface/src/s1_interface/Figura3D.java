package s1_interface;

public interface Figura3D {
	public abstract float calculoVolumen();
	
	static void print(String cadena) { //funciona sin instanciar la clase
		System.out.println(cadena);
	}
}

interface VariablesFiguras{
	public final float MIPI = (float) 3.14; //dentro de interfaz solo constantes
}