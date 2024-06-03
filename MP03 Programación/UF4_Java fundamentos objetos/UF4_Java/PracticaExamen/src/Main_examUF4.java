import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main_examUF4 {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		ArrayList <Dispositivo> carritoCompra = new ArrayList<>();
		int opcion;
		
		//Generamos los objetos correspondioentes y la arrayList carrito compra
		carritoCompra = cargarDatos();
		
		
		do {
		    System.out.println("Menu");
		    System.out.println("");
		    System.out.println("1. Mostrar carrito de compra");
		    System.out.println("2. Dispositivos ordenados por precio (Comparable)");
		    System.out.println("3. Dispositivos ordenados por almacenamiento (Comparator)");
		    System.out.println("4. Exit");
		    System.out.print("Option: ");
		   
		    
		    while (!sc.hasNextInt()) {
		        System.out.println("Error: Enter a number option.");
		        System.out.print("Option: ");
		        sc.nextLine(); 
		    }
		    
		    opcion = sc.nextInt();
		
		    switch (opcion) {
		        case 1:
		            mostrarCarritoCompra(carritoCompra);
		            break;
		            
		        case 2:
		        	Collections.sort(carritoCompra);
		            System.out.println("******************************************");
		        	System.out.println("Dispositivos por Almacenamiento Total");
		        	System.out.println("******************************************\n");
		        	for (Dispositivo dispositivo : carritoCompra) {
		        		String print = String.format("%-20s - Precio Total: %d", dispositivo.getClass().getCanonicalName(),dispositivo.getPrecioTotal());
		                System.out.println(print);
		            }
		        	System.out.println("------------------------------------------");
		            break;
		            
		        case 3:
		            Collections.sort(carritoCompra, new SortAlmacenamiento());
		            System.out.println("******************************************");
		        	System.out.println("Dispositivos por Almacenamiento Total");
		        	System.out.println("******************************************\n");
		        	for (Dispositivo dispositivo : carritoCompra) {
		        		String print = String.format("%-20s - Almacenamiento: %d", dispositivo.getClass().getCanonicalName(),dispositivo.getDiskCapacity());
		                System.out.println(print);
		            }
		        	System.out.println("------------------------------------------");
		        	
		            break;
		            
		        case 4:
		            System.out.println("Saliendo...");
		            break;
		            
		        default:
		            System.out.println("Introduce una opción valida");
		    }
		} while (opcion != 4);
		
		
	}
	
	private static ArrayList<Dispositivo> cargarDatos() {
		// Objetos de componenetes creados
				Cpu cpu1 = new Cpu("i9-10910",5000,10, 500);
				Cpu cpu2 = new Cpu("i7-4900MQ",3800,4, 270);
				Cpu cpu3 = new Cpu("Qualcomm Snapdragon 865",1800,8, 120);
				Cpu cpu4 = new Cpu("MediaTek Dimensity 1000+",2000,8, 130);
				Ram ram1 = new Ram("Crucial Ballistix BL2K8G36C16U4R", 16, 112);
				Ram ram2 = new Ram("Viper Elite DDR4 2666", 8, 57);
				Ram ram3 = new Ram("LPDDR5", 6, 40);
				Ram ram4 = new Ram("LPDDR4X", 8, 50);
				Hdd hdd1 = new Hdd("SATA2", 500, 55);
				Hdd hdd2 = new Hdd("SSD", 250, 110);
				Hdd hdd3 = new Hdd("UFS 3.1", 128, 60);
				Hdd hdd4 = new Hdd("UFS 3.1", 256, 90);
				Bateria b2 = new Bateria("Green Cell® L16M2PB1 L16C2PB2 ", 3500, 100,40);
				Bateria b3 = new Bateria("Li-Polymer", 4250, 100,55);
				Bateria b4 = new Bateria("Li-Polymer", 5000, 100,65);
				
				//Discos
				ArrayList <Hdd> discos1 = new ArrayList<>();
				discos1.add(hdd1);
				ArrayList <Hdd> discos2 = new ArrayList<>();
				discos2.add(hdd2);
				ArrayList <Hdd> discos3 = new ArrayList<>();
				discos3.add(hdd3);
				ArrayList <Hdd> discos4 = new ArrayList<>();
				discos4.add(hdd4);
				
				//Dispositivos creados
				Tablet tablet = new Tablet(cpu1,ram1,b2,discos1,100);
				Movil movil = new Movil(cpu2,ram2,b3,discos2,50);
				Portatil portatil = new Portatil(cpu3,ram3,b4,discos3,200);
				PCMesa pcMesa = new PCMesa(cpu4,ram4,discos4,300);
				
				//rellenar carrito
				ArrayList <Dispositivo> carritoCompra = new ArrayList<>();
				carritoCompra.add(tablet);
				carritoCompra.add(movil);
				carritoCompra.add(portatil);
				carritoCompra.add(pcMesa);
				
		return carritoCompra;
	}

	private static void mostrarCarritoCompra(ArrayList<Dispositivo> carritoCompra) {
		Scanner sc2 = new Scanner(System.in);
		
		for (Dispositivo dispositivo : carritoCompra) {
			System.out.println("------------------------------------------");
			System.out.println(dispositivo.toString());
			System.out.println("------------------------------------------");
			sc2.nextLine();
		}
		
	}



	private static void dispositivoPrecio() {
		
		
	}


	
	
	
	
	

}
