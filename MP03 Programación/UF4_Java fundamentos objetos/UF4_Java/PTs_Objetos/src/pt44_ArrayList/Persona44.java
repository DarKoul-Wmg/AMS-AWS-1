package pt44_ArrayList;

import java.util.ArrayList;
import java.util.Scanner;

public class Persona44 {
	private String nom;
	private int edad;
	private double altura;
	private char sexe;
	private boolean casat;
	
	//constr
	public Persona44(String nom, int edad, double altura, char sexe, boolean casat) {
		this.nom = nom;
		this.edad = edad;
		this.altura = altura;
		this.sexe = sexe;
		this.casat = casat;
	}

	public Persona44() {
	}
	
	public Persona44(String nom, int edad, double altura, char sexe) {
		this.nom = nom;
		this.edad = edad;
		this.altura = altura;
		this.sexe = sexe;
	}
	
	
	//getset
	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public double getAltura() {
		return altura;
	}

	public void setAltura(double altura) {
		this.altura = altura;
	}

	public char getSexe() {
		return sexe;
	}

	public void setSexe(char sexe) {
		this.sexe = sexe;
	}

	public boolean isCasat() {
		return casat;
	}

	public void setCasat(boolean casat) {
		this.casat = casat;
	}

	// toString datos de persona
	public String toString() {
		return "Nom = " + nom + "\n Edad = " + edad + "\n Altura ="  + altura + "\n Sexe = " + sexe 
				+ "\n Casat = " + casat+ "\n";
	}
	
}

class FrmPersona{
	private Scanner scanner = new Scanner(System.in);
	private ArrayList<Persona44> listaPersonas = new ArrayList<>();
	
	
	public void menuPersona() {
		int opc;

	    do {
	    	System.out.println("\nMenú de opciones:");
	        System.out.println("1. Introducir datos de una persona");
	        System.out.println("2. Mostrar los datos de las personas almacenadas");
	        System.out.println("3. Eliminar una persona de la lista");
	        System.out.println("4. Salir");
	        System.out.print("opción: ");
	        
	        while (!scanner.hasNextInt()) {
	            System.out.println("Error: Por favor, introduzca un número.");
	            System.out.print("Seleccione una opción: ");
	            scanner.next(); // Limpiar el búfer de entrada
	        }
	        
	        opc = scanner.nextInt();
	
	        switch (opc) {
	            case 1:
	                introducirDatos();
	                break;
	                
	            case 2:
	                mostrarDatos();
	                break;
	                
	            case 3:
	            	
	                eliminarPersona();
	                break;
	            case 0:
	                System.out.println("Saliendo...");
	                break;
	                
	            default:
	                System.out.println("Opción no válida. Inténtelo de nuevo.");
	        }
	    } while (opc != 0);
	}
	
	private void introducirDatos() {
		System.out.println("\nIntroducir datos de la persona:");
		
		 System.out.print("Nombre: ");
		 String nombre = scanner.next();
		 scanner.nextLine();
		 
		 System.out.print("Edad: ");
		 int edad = scanner.nextInt();
		 scanner.nextLine();
		 System.out.print("Altura: ");
		 double altura = scanner.nextDouble();
		 scanner.nextLine();
		 System.out.print("Sexe: ");
		 char sexe = scanner.nextLine().charAt(0);
		 scanner.nextLine();
		 System.out.print("Casat: (true/false)");
		 boolean casat = scanner.nextBoolean();
		 scanner.nextLine();
		
		 Persona44 nuevaPersona = new Persona44(nombre,edad,altura,sexe,casat);
		 listaPersonas.add(nuevaPersona);
		 System.out.println("Datos de la persona almacenados correctamente.");
	}
	private void mostrarDatos() {
		System.out.println("\nDatos de las personas almacenadas:");
        for (Persona44 persona : listaPersonas) {
            System.out.println(persona.toString());
        }
	}
	private void eliminarPersona() {
		System.out.println("\nEliminar una persona de la lista:");
        System.out.print("Ingrese el nombre de la persona a eliminar: ");
        String nombreEliminar = scanner.next();
        scanner.nextLine();
        
        for (Persona44 persona : listaPersonas) {
            if (persona.getNom().equals(nombreEliminar)) {
                listaPersonas.remove(persona);
                System.out.println("Se ha eliminado a la persona");
                break;
            }else {
            	System.out.println("No se ha encontrado a la persona con nombre "+ nombreEliminar);
            }
        }
    }
}


