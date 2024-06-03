package pt_pdf_excepciones;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main_Exc_Pdf {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int opcion;
		//ArrayList <Compte> cuentas = new ArrayList<>();
		Compte cuenta = null;
		
		String nif;
		float sal;
		
		do {
		    System.out.println("Menu");
		    System.out.println("");
		    System.out.println("1. Crear compte buit.");
		    System.out.println("2. Crear comte amb saldo inicial. ");
		    System.out.println("3. Ingrés de diners");
		    System.out.println("4. Treure diners ");
		    System.out.println("5. Veure saldo ");
		    System.out.println("6. Sortir ");
		    System.out.print("Opcion: ");
		   

		    while (!sc.hasNextInt()) {
		        System.out.println("Error: Introduce una opcion numerica.");
		        System.out.print("Opcion: ");
		        sc.nextLine(); 
		    }
		    
		    opcion = sc.nextInt();
		
		    switch (opcion) {
		        case 1:
		        	sc.nextLine();
		        	System.out.println("Introduce el identificador de la cuenta: ");
		        	 
		        	 nif = sc.nextLine();
		        	
		        	// Compte con saldo 0 
		        	
		        	
		        	cuenta = new Compte(0, nif);
		            break;
		        case 2:
		        	
		        	// Compte con saldo X
		     
		        	
		        	System.out.println("Introduce el saldo inicial de la cuenta:");
		            sal = sc.nextFloat();
		            sc.nextLine();
		            
		            System.out.println("Introduce el identificador de la cuenta: ");
		        	nif = sc.nextLine();
		       
		        	cuenta = new Compte(sal, nif);		        	
		        	break;
		            
		        case 3:
		        	
		        	System.out.println("");
		        	System.out.println("Cantidad a ingresar: ");
		        	float ingr = sc.nextFloat();
		        	
		        	cuenta.ingressar(ingr);
		        	
		            break;            
		        case 4:
		        	
		        	System.out.println("Cantidad a retirar: ");
		        	float ret = sc.nextFloat();
		        	
		        	//Excepcion
		        	try {
		        		
		        		cuenta.extreure(ret);
		        		
		        	}catch(SaldoInsuficienteException e) {
		        		
		        		System.out.println("--------------------");	
		    			System.out.println(e.getMessage());	
		    			System.out.println("--------------------");
		        	}
		        	
		        	
		            break;
		        case 5:
		            
		        	System.out.println("Saldo de la cuenta: ");
		        	System.out.println(cuenta.toString());
		            break;
		        case 6:
		        	System.out.println("Saliendo...");
		            
		            break;
		            
		        default:
		            System.out.println("Introduce una opción valida");
		    }
		} while (opcion != 6);
	}
}
