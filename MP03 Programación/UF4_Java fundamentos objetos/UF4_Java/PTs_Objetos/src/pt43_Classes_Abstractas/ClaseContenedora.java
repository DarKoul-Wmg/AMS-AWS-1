package pt43_Classes_Abstractas;

import java.util.ArrayList;

public class ClaseContenedora {
	private ArrayList<Empleado> empleados;

	public ClaseContenedora() {
		super();
		empleados = new ArrayList<Empleado>();
	}
	
	//se crea un metodo para meter empleados
	
	public void insertaEmpleado(Empleado e) {
		empleados.add(e);
	}
	
	//eliminar neteja (HAY QUE HACERLO DESDE ATRAS PARA QUE NO PETE)
	
	public void eliminarNeteja() {
		
		for (int i = empleados.size()-1; i>=0;i--) {
			if (empleados.get(i) instanceof Neteja) {
				empleados.remove(i);
			}
		}
	}
	
	//Quants cornella
	
	public int cuantosCornella() {
		int contador = 0;
		for (Empleado e : empleados) {
			if (e.ciutatO().equals("Cornella")) {
				contador +=1;
			}
		}
		return contador;
	}
	
	//Salario/
	
	public float costeNomina(){
		int salarios = 0;
		for (Empleado e : empleados) {
			salarios += e.salariDiari();
		}
		return salarios;
	}
	
	//Cantidad cajeros
	
	public int cantidadCajeros() {
		int contador =0;
		for (Empleado e : empleados) {
			if (e instanceof Caixer) {
				contador +=1;;
			}
		}
		return contador;
	}
	
	//sueldo promedio
	public float sueldoPromedio() {
		return (float) costeNomina()/empleados.size();
	}
	
	//mostrar nombre
	
	public void mostrarNombre() {
		for (Empleado e : empleados) {
			System.out.println(e.getNom());
		}
	}

}
