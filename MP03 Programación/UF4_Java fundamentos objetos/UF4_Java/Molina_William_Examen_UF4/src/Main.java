import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		ArrayList <MotorizedVehicle> vehiculos = new ArrayList<>();
		Scanner sc = new Scanner(System.in);
		int opcion;
		
		//datos 
		ElectricEngine me1 = new ElectricEngine("Magnetic Protection IP54",20, 700, 40, 20);
		ElectricEngine me2 = new ElectricEngine("Vectorial Brusatori Protection VL132X",25, 800, 30, 25);
		ElectricEngine me3 = new ElectricEngine("Vectorial Brusatori Protection VL315L",30, 900, 45, 30);
		
		CombustionEngine mc1 = new CombustionEngine("Volkswagen 1.5 TFSI de 150 CV",150, 5000, 150, 1500, 5.6f);
		CombustionEngine mc2 = new CombustionEngine("BMW PHEV xDrive25e X1",220, 8700,190, 1700, 3.9f);
		CombustionEngine mc3 = new CombustionEngine("Ford Gasolina 1.0 EcoBoost 125 CV",120, 4300, 150, 1350, 3.5f);
		
		Wheel w1 = new Wheel("Michelin Pilot Sport 5",100,20,65);
		Wheel w2 = new Wheel("Pirelli Suv Scorpion R19",88,23,65);
		Wheel w3 = new Wheel("Goodyear Efficient Grip Performance 195-65 ",75,25,85);
		Wheel w4 = new Wheel("Bridgestone Trail Wing TW202 ",84,39,15);
		
		ArrayList<Wheel> aw1 = new ArrayList<Wheel>();
		for (int i=0; i<4 ; i++) {
			aw1.add(w1);
		}
		
		ArrayList<Wheel> aw2 = new ArrayList<Wheel>();
		for (int i=0; i<4 ; i++) {
			aw2.add(w2);
		}
		
		Battery b1 = new Battery("Battery Moto Yuasa",34,150,12);
		Battery b2 = new Battery("Battery Moto Bosch Yb5lb",29,160,12);
		Battery b3 = new Battery("Battery Optima Redtop Rtc42",198,650,12);
		Battery b4 = new Battery("Battery Tudor 55ah",80,475,12);
		
		CombustionVehicle cv1 = new CombustionVehicle("Seat Arroba", 4, 9000, mc1, 50);
		cv1.setWheels(aw1);
		
		CombustionVehicle cv2 = new CombustionVehicle("Ford Apofis", 4, 11000, mc3, 54);
		cv2.setWheels(aw2);
		
		ElectricVehicle ev1 = new ElectricVehicle("BMW Serie 200",4, 14000, me1,30);
		ArrayList<Wheel> aw3 = new ArrayList<Wheel>();
		for (int i=0; i<4 ; i++) {
			aw3.add(w3);
		}
		ev1.setWheels(aw3);
		ArrayList<Battery> ab3 = new ArrayList<Battery>();
		for (int i=0; i<4 ; i++) {
			ab3.add(b1);
		}
		ev1.setBatteries(ab3);
		
		
		ElectricVehicle ev2 = new ElectricVehicle("Honda TZR",2, 8000, me2,10);
		ev2.addWheels(w4);
		ev2.addWheels(w4);
		ArrayList<Battery> ab4 = new ArrayList<Battery>();
		for (int i=0; i<4 ; i++) {
			ab4.add(b3);
		}
		ev2.setBatteries(ab4);
		
		
		vehiculos.add(cv1);
		vehiculos.add(cv2);
		vehiculos.add(ev1);
		vehiculos.add(ev2);
		

		
		do {
		    System.out.println("Menu");
		    System.out.println("");
		    System.out.println("1. Mostrar vehiculos disponibles");
		    System.out.println("2. Vehiculos ordenados por precio");
		    System.out.println("3. Vehiculos ordenados por velocidad maxima");
		    System.out.println("4. Exit");
		    System.out.print("Opcion: ");
		   
		    
		    while (!sc.hasNextInt()) {
		        System.out.println("Error: Introduce una opcion numerica.");
		        System.out.print("Opcion: ");
		        sc.nextLine(); 
		    }
		    
		    opcion = sc.nextInt();
		
		    switch (opcion) {
		        case 1:
		     
		        	for (MotorizedVehicle vehiculo : vehiculos) {
		    			System.out.println("------------------------------------------");
		    			System.out.println(vehiculo.toString());
		    			System.out.println("------------------------------------------");
		    			}
		            break;
		        case 2:

		        	Collections.sort(vehiculos);
		            System.out.println("******************************************");
		        	System.out.println("Vehiculos por Precio");
		        	System.out.println("******************************************\n");
		        	
		        	for (MotorizedVehicle vehiculo : vehiculos) {
		        		String print = String.format("%-20s - Precio Total: %d", vehiculo.getModel(),vehiculo.getPrice());
		                System.out.println(print);
		            }
		        	System.out.println("------------------------------------------");
		        	
		            break;
		            
		        case 3:
		        	
		        	Collections.sort(vehiculos, new SortByMaxSpeed());
		            System.out.println("******************************************");
		        	System.out.println("Vehiculos por Velocidad Maxima");
		        	System.out.println("******************************************\n");
		        	for (MotorizedVehicle vehiculo : vehiculos) {
		        		String print = String.format("%-20s - Vel Maxima: %d", vehiculo.getModel(),vehiculo.getEngine().getMaxSpeed());
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
	
}

