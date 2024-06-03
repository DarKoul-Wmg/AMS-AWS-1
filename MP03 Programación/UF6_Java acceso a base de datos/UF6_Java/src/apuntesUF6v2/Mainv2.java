package apuntesUF6v2;

import java.util.Scanner;

public class Mainv2 {

	public static void main(String[] args) {
		String urlDatos = "jdbc:mysql://localhost/farmville?serverTimezone=UTC&autoReconnect=true&useSSL=false";
		String usuario = "root";
		String pass = "P@ssw0rd";
		try {
			// Crear objeto de la clase ConnectionBDD
			
			Class.forName("com.mysql.cj.jdbc.Driver");
			ConnectionBDD connectionBDD = new ConnectionBDD(urlDatos, usuario, pass);

	        // Menú de opciones
	        Scanner scanner = new Scanner(System.in);
	        int opcion;
	        do {
	            System.out.println("\n----- Menú de Opciones -----");
	            System.out.println("1. Insertar Empleado");
	            System.out.println("2. Eliminar Empleado por ID");
	            System.out.println("3. Mostrar Empleados Ordenados por Ciudad");
	            System.out.println("4. Realizar Operaciones con ResultSet");
	            System.out.println("5. Salir");
	            System.out.print("Ingrese su opción: ");
	            opcion = scanner.nextInt();

	            switch (opcion) {
	                case 1:
	                    connectionBDD.insertEmpleat();
	                    break;
	                case 2:
	                    System.out.print("Ingrese el ID del empleado a borrar: ");
	                    int dni = scanner.nextInt();
	                    connectionBDD.deleteEmpleat(dni);
	                    break;
	                case 3:
	                    connectionBDD.orderByName();
	                    break;
	                case 4:
	                    connectionBDD.operacionsResultSet();
	                    break;
	                case 5:
	                    System.out.println("Saliendo del programa. ¡Hasta luego!");
	                    break;
	                default:
	                    System.out.println("Opción no válida. Intente nuevamente.");
	            }

	        } while (opcion != 5);
		
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}    
}
