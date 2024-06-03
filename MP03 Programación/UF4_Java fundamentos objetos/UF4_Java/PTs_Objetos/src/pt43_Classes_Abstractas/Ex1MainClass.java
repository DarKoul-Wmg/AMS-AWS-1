package pt43_Classes_Abstractas;

import java.util.ArrayList;
import java.util.Iterator;

public class Ex1MainClass {

	public static void main(String[] args) {
		Caixer juan = new Caixer("Juan","Berlin","Caracas",25);
		//System.out.println(juan.ciutatO());
		//System.out.println(juan.salariDiari());
		
		Neteja amaya = new Neteja("Amaya","Burgo","Mina");
		Mostrador encarna = new Mostrador("encarna","concept","hola",25);
		Caixer rodrigo = new Caixer("rodrigo","Japon","china",25);
		
		
		//USAR METODO INSERTAR EMPLEADO
		ClaseContenedora nominas = new ClaseContenedora();
			
		nominas.insertaEmpleado(new Caixer("Juan","Berlin","Caracas",25));
		nominas.insertaEmpleado(new Mostrador("encarna","concept","hola",25));
		nominas.insertaEmpleado(new Neteja("Amaya","Burgo","Mina"));
		nominas.insertaEmpleado(new Caixer("rodrigo","Japon","china",25));

		nominas.mostrarNombre();
		nominas.eliminarNeteja();
		System.out.println(nominas.cantidadCajeros());
		System.out.println(nominas.cuantosCornella());
		
		ArrayList<Empleado> empleados = new ArrayList<Empleado>();
		
		empleados.add(encarna);
		empleados.add(juan);
		empleados.add(amaya);
		//empleados.set(3,rodrigo);
		empleados.add(2,rodrigo);
		empleados.add(new Mostrador("encarna","concept","hola",25)); //SE PUEDEN CREAR Y REFERENCIAR, PERO SOLO CON EL INDICE DEL ARRAY
		
		
		//  empleados.clear(); LIMPIA ARRAYLIST
		System.out.println(empleados.contains(encarna)); //COMO CONTIENE A ENCARNA DA TRUE
		System.out.println(empleados.indexOf(encarna));  //POSICION DE ENCARNA
		
		//empleados.remove(2); //ELIMINAR 
		//empleados.remove(encarna);
		
		
		//System.out.println(empleados.get(2));
		
		//RECORRER ARRAY CON FOR
		
//		for (int i = 0; i<empleados.size(); i++) {
//			System.out.println(empleados.get(i));
//			if (empleados.get(i) instanceof Mostrador) {
//				System.out.println(((Mostrador) empleados.get(i)).getVendes());			
//			}
//		}
		
//		Iterator i = empleados.iterator(); //contenedor de indices del array
//		while (i.hasNext()) {
//			System.out.println(i.next());
//		}
		
		
		//for (tipoCosa identificador/variable : lugarDondeRecuperarObjetos)
		for (Empleado pepe: empleados) {
			System.out.println(pepe);
		}
	}

}
