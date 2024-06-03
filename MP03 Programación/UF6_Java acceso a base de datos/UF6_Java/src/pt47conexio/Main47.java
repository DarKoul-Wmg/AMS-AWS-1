package pt47conexio;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main47 {

	public static void main(String[] args) {
		//para metodos NO estaticos
		Main47 myclass = new Main47();
		//
		
		String urlDatos = "jdbc:mysql://localhost/farmville?serverTimezone=UTC&autoReconnect=true&useSSL=false";
		String usuario = "root";
		String pass = "P@ssw0rd";
		Scanner sc = new Scanner(System.in);
		int opcion;
		
		
		try {
		
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection conn = DriverManager.getConnection(urlDatos,usuario,pass);
			Statement stmnt = conn.createStatement(); 
			String query = "";
			ArrayList<Granjero> granjeros = new ArrayList<Granjero>();
			
			
			do {
			    System.out.println("PT47");
			    System.out.println("");
			    System.out.println("1. Bases de datos");
			    System.out.println("2. Tablas");
			    System.out.println("3. Generar ArrayList de Granjeros ordenados por dinero.");
			    System.out.println("4. Ordenar ArrayList por...");
			    System.out.println("5. Añadir nuevo Granjero");
			    System.out.println("6. Buscar granjero por...");
			    System.out.println("7. Incrementar +1 nivel de granjero");
			    System.out.println("8. Borrar granjero");
			    System.out.println("0. Exit");
			    System.out.print("Option: ");
			    
			    while (!sc.hasNextInt()) {
			        System.out.println("Error: Enter a number option.");
			        System.out.print("Option: ");
			        sc.nextLine(); // Limpiar el búfer de entrada
			    }
			    
			    opcion = sc.nextInt();
			
			    switch (opcion) {
			    	case 0:
			    		System.out.println("Saliendo...");
			    		conn.close();
			    		break;
			    		
			        case 1:			        	
			        	query = myclass.mostrarBasesDatos();
			        	System.out.println(query);
			        	ResultSet rs = stmnt.executeQuery(query);
			        	while (rs.next()) {
							System.out.println("Database = "+rs.getString(1));
						}
			            break;
			            
			        case 2:
			        	myclass.mostrarTablas();
			        	query = myclass.mostrarTablas();
			        	System.out.println(query);
			        	rs = stmnt.executeQuery(query);
			        	while (rs.next()) {
							System.out.println("Database = "+rs.getString(1));
						}
			            break;
			        case 3:
			        	
			        	query = "Select id, nombre, descripcion, dinero, puntos, nivel FROM granjeros";
			        	
			        	PreparedStatement ps = conn.prepareStatement(query);
			        	rs = ps.executeQuery();
			        	
			        	while (rs.next()) {
							int id = rs.getInt(1);
							String nombre = rs.getString(2);
							String descripcion = rs.getString(3);
							int dinero = rs.getInt(4);
							int puntos = rs.getInt(5);
							int nivel = rs.getInt(6);
							
							Granjero granjero = new Granjero(id, nombre, descripcion, dinero, puntos, nivel);
							granjeros.add(granjero);
						}
			        	
			        	Collections.sort(granjeros);
			        	System.out.println("===========================================");
			        	System.out.println("ArrayList de Granjeros ordenada por dinero:");
			        	System.out.println("===========================================\n");
			        	for (Granjero g : granjeros) {
			        		System.out.println("id = "+g.getId() + " dinero = " + g.getDinero() + " nombre = "+g.getNombre() + "\n");
			        	}
			            break;
			            
			        case 4:
			        	if (granjeros.size() == 0) {
			        		System.out.println("Genera una arraylist con la opc 3");
			        		break;
			        	}
			        	System.out.println("1. Nombre");
			        	System.out.println("2. Dinero");
			        	System.out.println("3. Puntos");
			        	System.out.println("Opcion: ");
			        	opcion = sc.nextInt();
			        	switch (opcion) {
				             case 1:
				            	 myclass.ordenarPorNombre(granjeros);
				                 break;
				                 
				             case 2:
				            	 myclass.ordenarPorDinero(granjeros);
				                 break;
				                 
				             case 3:
				            	 myclass.ordenarPorPuntos(granjeros);
				                 break;
				                 
				             default:
				                 System.out.println("Opción no válida");
			            }

			            break;
			        case 5:
			        	
			        	sc.nextLine();
			    		System.out.println("Nombre: ");
			    		String nombre = sc.nextLine();
			    		
			    		
			    		try {
				    		query = "INSERT INTO granjeros (nombre, descripcion) VALUES (?, ?)";
				    		
				    		ps = conn.prepareStatement(query);
				    		ps.setString(1, nombre);
				    		ps.setString(2, "estandard");
				        	ps.executeUpdate();
				        	
				        	System.out.println("Inserción correcta");
				        	
			    		} catch (SQLException e) {
			    	        System.out.println("Error al ejecutar la consulta: " + e.getMessage());
			    		}
			            break;
			            
			        case 6:
			        	sc.nextLine();
			        	System.out.println("Nombre o descripcion: ");
			    		String busqueda = sc.nextLine();
			        	
			    		query = "Select * FROM granjeros WHERE nombre LIKE ? OR descripcion LIKE ?";
			    		ps = conn.prepareStatement(query);
			    		
			    		ps.setString(1, "%"+busqueda+"%");
			    		ps.setString(2, "%"+busqueda+"%");
			    		
			    		rs = ps.executeQuery();
			    		
			    		while (rs.next()) {
							System.out.println("Nombre = "+rs.getString(2)+" Description = "+rs.getString(3) + " Id = "+rs.getInt(1));
						}
			    		
			            break;
			            
			        case 7:
			        	sc.nextLine();
			        	System.out.println("Nombre: ");
			    		String nom = sc.nextLine();
			        	
			    		String queryNom = "SELECT * FROM granjeros WHERE nombre = ?";
			    		ps = conn.prepareStatement(queryNom);
			    		ps.setString(1, nom);
			    		rs = ps.executeQuery();
			    		
			    		if (rs.next()) {
			    			int idGranjero = rs.getInt(1);
			    			int nivelGranjero = rs.getInt(6);
			    			int nuevoNivel = nivelGranjero +1;
			    			
			    			query = "UPDATE granjeros SET nivel = ? WHERE id = ?";
				    		ps = conn.prepareStatement(query);
				    		ps.setInt(1, nuevoNivel);
				    		ps.setInt(2, idGranjero);
				    		
				    		ps.executeUpdate();
				    		System.out.println("Nivel subido");
			    			
			    		} else {
			    			System.out.println("No existe un granjero con ese nombre");
			    		}
			    		
			    		break;
			            
			        case 8:
			        	sc.nextLine(); // Consumir salto de línea pendiente
			            
			            System.out.println("ID del granjero a borrar: ");
			            int idBorrar = sc.nextInt();
			            
			            query = "DELETE FROM granjeros WHERE id = ?";			            
			            ps = conn.prepareStatement(query);			         			            
			            ps.setInt(1, idBorrar);
			            
			            ps.executeUpdate();
			            System.out.println("Granjero borrado correctamente");
			            break;
			            
			        default:
			            System.out.println("Enter a valid option");
			    }
			} while (opcion != 0);
			
		} catch (ClassNotFoundException e) {
			System.out.println("Driver no se ha cargado correctamente");
			
			
		} catch (SQLException e) {
			System.out.println("Error en la conexion");
		}
		
		
	}

	//metodos
	
		
	private String mostrarBasesDatos() {
		String query = "show databases;";
		return query;
	}
	
	private String mostrarTablas() {
		String query = "show tables;";
		return query;
		
	}
	
	private void ordenarPorNombre(ArrayList<Granjero> granjeros) {
		Collections.sort(granjeros, new OrdenarNombre());
        System.out.println("===========================================");
   	 	System.out.println("Granjeros ordenados por Nombre:");
   	 	System.out.println("===========================================\n");
   	 	for (Granjero g : granjeros) {
   	 		System.out.println("id = "+g.getId() + " nombre = "+g.getNombre() + " dinero = " + g.getDinero()  + "\n");
   	 	}
	}
	
	private void ordenarPorPuntos(ArrayList<Granjero> granjeros) {
		Collections.sort(granjeros, new OrdenarPuntos());
        System.out.println("===========================================");
        System.out.println("Granjeros ordenados por Puntos:");
   	 	System.out.println("===========================================\n");
   	 	for (Granjero g : granjeros) {
   	 		System.out.println("id = "+g.getId() + " puntos = " + g.getPuntos() + " nombre = "+g.getNombre() + "\n");
   	 	}
	}
	
	private void ordenarPorDinero(ArrayList<Granjero> granjeros) {
		Collections.sort(granjeros, new OrdenarDinero());
        System.out.println("===========================================");
        System.out.println("Granjeros ordenados por Dinero:");
   	 	System.out.println("===========================================\n");
   	 	for (Granjero g : granjeros) {
   		 System.out.println("id = "+g.getId() + " dinero = " + g.getDinero() + " nombre = "+g.getNombre() + "\n");
   	 	}
			
	}
	
}

