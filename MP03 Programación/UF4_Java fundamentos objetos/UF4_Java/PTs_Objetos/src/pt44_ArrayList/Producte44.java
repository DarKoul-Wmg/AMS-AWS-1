package pt44_ArrayList;

import java.util.ArrayList;
import java.util.Scanner;

public class Producte44 {
	private int codi;
	private String nom;
	private String tipus;
	private double preu;
	private int stock;
	
	public Producte44(int codi, String nom, String tipus, double preu, int stock) {
		this.codi = codi;
		this.nom = nom;
		this.tipus = tipus;
		this.preu = preu;
		this.stock = stock;
	}
	
	public Producte44() {
	}
	
	//getters y setters

	public int getCodi() {
		return codi;
	}

	public String getNom() {
		return nom;
	}

	public String getTipus() {
		return tipus;
	}

	public double getPreu() {
		return preu;
	}

	public int getStock() {
		return stock;
	}

	public void setPreu(double preu) {
		this.preu = preu;
	}
	
	
}


class ArrayProducte{
	
	private ArrayList <Producte44> llistaProductes;
	
	
	public ArrayProducte(ArrayList<Producte44> llistaProductes) {
		super();
		this.llistaProductes = llistaProductes;
	}

//	public void setLlistaProductes(ArrayList<Producte44> llistaProductes) {
//		this.llistaProductes = llistaProductes;
//	}
	
	public ArrayList<Producte44> getLlistaProductes(){ 
		return llistaProductes;
	}

	public void agregar(Producte44 producte) {
		llistaProductes.add(producte);
	}
	
	public void eliminar(int codi) {	
		llistaProductes.remove(codi);
	}
	
	public Producte44 obtenir(int codi) {
		return llistaProductes.get(codi);
	}
	
	public int buscar(int codi) {
		for (int i = 0; i < llistaProductes.size(); i++) {
			if (llistaProductes.get(i).getCodi()== codi){
				return i;
			}
		}
		return -1;
	} 
	
	
	public int grandaria() {
		return llistaProductes.size();
	}
	

}

class FrmProducte {
	
	private ArrayProducte arrayProducte;
	private Scanner scanner;
	
	public FrmProducte(){
		arrayProducte = new ArrayProducte(new ArrayList<>());
		scanner = new Scanner(System.in);
	}
	
	public void menu() {
		int opc;
		do {
			System.out.println("\nMenú:");
            System.out.println("1. Afegir producte");
            System.out.println("2. Augmentar preu dels productes d'Oficina en un 10%");
            System.out.println("3. Eliminar productes amb estoc zero");
            System.out.println("4. Mostrar tots els productes");
            System.out.println("0. Sortir");
            System.out.print("Selecciona una opció: ");
            opc = scanner.nextInt();
            
            switch (opc) {
            	case 1:
            		afegirProducte();
            		break;
            		
            	case 2:
            		aumentarPrecioOf();
            		break;
            		
            	case 3:
            		eliminarStockZero();
            		break;
            		
            	case 4:
            		mostrarProductes();
            		break;
            		
            	case 0:
            		System.out.println("Saliendo...");
            		break;
            		
            	default:
            		System.out.println("Opción no valida");
            }
			
		} while(opc != 0);
		
	}
	
	private void afegirProducte() {
		System.out.println("Codigo del producto");
		scanner.nextLine();
		int codi = scanner.nextInt();
		
		System.out.println("Nombre del producto");
		scanner.nextLine();
		String nom = scanner.next();
		
		System.out.println("Tipo del producto");
		scanner.nextLine();
		String tipo = scanner.next();
		
		System.out.println("Precio del producto");
		scanner.nextLine();
		double precio = scanner.nextDouble();
		
		System.out.println("Stock del producto");
		scanner.nextLine();
		int stock = scanner.nextInt();
		
		Producte44 producte = new Producte44(codi,nom,tipo,precio,stock);
		
		//PRODUCTOS NO REPETIDOS, usamos buscar para comprobar que no esta en la array (-1):
		if (arrayProducte.buscar(codi) == -1) {
			arrayProducte.agregar(producte);
			System.out.println("Producto agrergado...");
			} else {
				System.out.println("Producto con el codigo ya existe");
		}
	}
	
	private void eliminarStockZero() {
		for (Producte44 producte : arrayProducte.getLlistaProductes()){
			if (producte.getStock() == 0) {
				arrayProducte.eliminar(producte.getCodi());
			}
		}
	}
	
	
	private void aumentarPrecioOf() {
		for (Producte44 producte : arrayProducte.getLlistaProductes()){
			if (producte.getTipus().equals("Oficina")){
				
				double newPrecio = producte.getPreu() * 1.10;
				producte.setPreu(newPrecio);
			}
		}
		
		System.out.println("S'ha augmentat el preu dels productes d'Oficina en un 10%.");	
	}
	
	
	private void mostrarProductes() {
		System.out.println("Lista de productos: ");
		for (Producte44 producte : arrayProducte.getLlistaProductes()){
			System.out.println(producte.getCodi() + " - " + producte.getNom() + " - " + producte.getTipus() +
					" - " + producte.getPreu() + " - " + producte.getStock());
		}
	}
	
}
