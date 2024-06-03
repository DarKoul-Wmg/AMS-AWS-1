package pt48modificacio;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

import pt47conexio.Granjero;

public class Main48 {

    public static void main(String[] args) {
        Main48 myclass = new Main48();
        String urlDatos = "jdbc:mysql://localhost/farmville?serverTimezone=UTC&autoReconnect=true&useSSL=false";
        String usuario = "root";
        String pass = "P@ssw0rd";

        Scanner sc = new Scanner(System.in);
        int opcion;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(urlDatos, usuario, pass);
            Statement stmnt = conn.createStatement();
            String query = "";

            do {
                System.out.println("PT48");
                System.out.println("");
                System.out.println("1. Alta de personas");
                System.out.println("2. Baja de personas");
			    System.out.println("3. Modificar persona");
			    System.out.println("4. Consultar datos...");
                System.out.println("0. Exit");
                System.out.print("Option: ");

                while (!sc.hasNextInt()) {
                    System.out.println("Error: Enter a number option.");
                    System.out.print("Option: ");
                    sc.nextLine(); // Limpiar el búfer de entrada
                }

                opcion = sc.nextInt();
                sc.nextLine(); // Limpiar el búfer

                switch (opcion) {
                    case 0:
                        System.out.println("Saliendo...");
                        break;

                    case 1:
                        myclass.insertarPersona(conn, sc);
                        break;
                        
                    case 2:

			        	System.out.println("Introduce el dni de la persona a borrar:");			        	
			        	String dniBorrar = sc.nextLine();	
			        	
			            query = "DELETE FROM personas WHERE DNI = ?";			            
			            PreparedStatement ps = conn.prepareStatement(query);			         			            
			            ps.setString(1, dniBorrar);
			            
			            ps.executeUpdate();
			            System.out.println("Persona borrada correctamente");
			            break;
			            
			        case 3:
			        	myclass.modificarPersona(conn,sc);			        	
			            break;
			            
			        case 4:
			        	myclass.mostrarPersonas(conn,sc);
			        	
			        	break;

                    default:
                        System.out.println("Introduce una opción válida");
                }
            } while (opcion != 0);

            conn.close();

        } catch (ClassNotFoundException e) {
            System.out.println("Driver no se ha cargado correctamente");

        } catch (SQLException e) {
            System.out.println("Error en la conexion");
        }

        sc.close(); // Cerrar scanner al finalizar
    }

	public boolean insertarPersona(Connection conn, Scanner sc) {
        try {
            System.out.println("Introduce el DNI (9 caracteres, números y una letra al final): ");
            String dni = sc.nextLine();

            if (!validarDNI(dni)) {
                System.out.println("DNI incorrecto");
                return false;
            }

            System.out.println("Introduce el nombre: ");
            String nombre = sc.nextLine();

            System.out.println("Introduce la fecha de nacimiento (formato: dd/MM/yyyy): ");
            String fechaStr = sc.nextLine();
            boolean fechaNac = validarFecha(fechaStr);
            if (!fechaNac) {
                System.out.println("Formato de fecha incorrecto");
                return false;
            }

            System.out.println("Introduce la dirección: ");
            String direccion = sc.nextLine();

            System.out.println("Introduce el teléfono (9 dígitos): ");
            int telefono = sc.nextInt();
            
            sc.nextLine(); // Limpiar el búfer
            
            

            // QUERY SQL
            String query = "INSERT INTO personas (DNI, NOMBRE, FECNAC, DIR, TFNO) VALUES (?, ?, ?, ?, ?)";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setString(1, dni);
            ps.setString(2, nombre);
            ps.setDate(3, new java.sql.Date(new SimpleDateFormat("dd/MM/yyyy").parse(fechaStr).getTime()));
            ps.setString(4, direccion);
            ps.setInt(5, telefono);
            
            
            // Ejecutar la consulta
            ps.executeUpdate();
            return true;

        } catch (SQLException | ParseException e) {
            System.out.println("Error al insertar la persona en la base de datos");
            //e.printStackTrace(); // Imprimir detalles del error
            return false;
        }
    }

    public boolean validarDNI(String dni) {
    	    	
        if (dni.length() != 9) {
            return false;
        }
        
        String digitos = dni.substring(0, 8);

        try {
            // Intentar convertir la subcadena en un numero
            int num = Integer.parseInt(digitos);
            
            // Verificar que ultimo caracter sea una letra
            String letra = dni.substring(8);
            if (!Character.isLetter(letra.charAt(0))) {
            	return false;
            }

            
        } catch (NumberFormatException e) {
            // DNI no es valido
        	return false;
        }
    	//valido
        return true;
    }

    public boolean validarFecha(String fechaStr) {
        DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
        dateFormat.setLenient(false); // No permitir fechas inválidas (por ejemplo, 2022-02-30)

        try {
            dateFormat.parse(fechaStr); // Intentar parsear la fecha
            return true; // La fecha tiene el formato correcto
        } catch (ParseException e) {
            return false; // La fecha no tiene el formato correcto
        }
    }
    
    public void modificarPersona(Connection conn, Scanner sc) {
        try {
            System.out.println("DNI de la persona a modificar: ");
            String dni = sc.nextLine();

            // Consulta para obtener los datos de la persona
            String queryMod = "SELECT * FROM personas WHERE DNI = ?";
            PreparedStatement ps = conn.prepareStatement(queryMod);
            ps.setString(1, dni);
            ResultSet rs = ps.executeQuery();

            if (rs.next()) {
                String nombreActual = rs.getString("NOMBRE");
                String direccionActual = rs.getString("DIR");
                int telefonoActual = rs.getInt("TFNO");
                Date fechaNac = rs.getDate("FECNAC");

                System.out.println("Nombre actual: " + nombreActual);
                System.out.println("Introduce el nuevo nombre: ");
                String nuevoNombre = sc.nextLine();

                System.out.println("Direccion actual: " + direccionActual);
                System.out.println("Introduce la nueva Direccion: ");
                String nuevaDireccion = sc.nextLine();

                System.out.println("Telefono actual: " + telefonoActual);
                System.out.println("Introduce el nuevo telefono: ");
                int nuevoTelefono = sc.nextInt();
                sc.nextLine(); // Limpiar el búfer

                // Consulta para actualizar los datos
                String queryUpdate = "UPDATE personas SET NOMBRE = ?, DIR = ?, TFNO = ? WHERE DNI = ?";
                PreparedStatement psUpdate = conn.prepareStatement(queryUpdate);
                psUpdate.setString(1, nuevoNombre);
                psUpdate.setString(2, nuevaDireccion);
                psUpdate.setInt(3, nuevoTelefono);
                psUpdate.setString(4, dni);
                
                Persona48 persmod = new Persona48(dni, nuevoNombre, fechaNac, nuevaDireccion, nuevoTelefono);
                psUpdate.executeUpdate();
                
                System.out.println("Datos actualizados correctamente:\n"+persmod.toString());
               

            } else {
                System.out.println("No existe una persona con ese DNI.");
            }

        } catch (SQLException e) {
            System.out.println("Error al modificar la persona.");
            e.printStackTrace();
        }
    }
    
    private void mostrarPersonas(Connection conn, Scanner sc) {
    	ArrayList<Persona48> personas = new ArrayList<Persona48>();		
		try {
			String query = "Select * FROM personas";
			PreparedStatement ps = conn.prepareStatement(query);
			ResultSet rs = ps.executeQuery();
			
			while (rs.next()) {
				String dni = rs.getString("DNI");
				String nombre = rs.getString("NOMBRE");
				Date fecha = rs.getDate("FECNAC");
				String direccion = rs.getString("DIR");
				int telefono = rs.getInt("TFNO");
				
				Persona48 persona = new Persona48(dni,nombre,fecha,direccion,telefono);
				personas.add(persona);
			}
			System.out.println("===========================================");
			System.out.println("======= PERSONAS =======");
			System.out.println("===========================================");
			for (Persona48 p : personas) {
				System.out.println("--------------");
				System.out.println(p.toString());
			}
			
			
		} catch (SQLException e) {
			
			System.out.println("Error al recuperar los datos de las personas");
			e.printStackTrace();
		}
		
	}
}

