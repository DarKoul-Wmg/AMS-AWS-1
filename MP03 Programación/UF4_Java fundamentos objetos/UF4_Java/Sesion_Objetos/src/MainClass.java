
public class MainClass {

	public static void main(String[] args) {
		
		ClaseA c1 = new ClaseA();   		//objetoC1
//		System.out.println(c1.atributo1);
//		System.out.println(c1.atributo2);
		System.out.println(c1.metodo_muestra_estados());

		
		ClaseA c2 = new ClaseA("nuevo Valor 1", "nuevo Valor 2");			//objetoC2
//		c2.metodo1("nuevo Valor 1");
//		c2.metodo2("nuevo Valor 2");
		
//		c2.atributo1 ="nuevo Valor1"; //no usar nunca
//		c2.atributo2 ="nuevo Valor2";
//		System.out.println(c2.atributo1);
//		System.out.println(c2.atributo2);
		
		System.out.println(c2.metodo_muestra_estados());
		
		Semaforo s1 = new Semaforo("verde");
		Semaforo s2 = new Semaforo("rojo");
		
		System.out.println(s1.getEstado());
		System.out.println(s2.getEstado());
		
		s2.setEstado("ambar");
		System.out.println(s2.getEstado());
		
//		s2.estado = "<sf";//con private evitamos que se modifique, solo con metodos
		
	}

}
