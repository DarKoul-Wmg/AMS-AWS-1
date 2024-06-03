package apuntesUF6v2;

import java.sql.*;
import java.util.ArrayList;
import java.util.Scanner;

public class ConnectionBDD {
	private Connection conn;

	public ConnectionBDD(String url, String user, String password) {
		
		try {
            conn = DriverManager.getConnection(url, user, password);
            System.out.println("Conexion establecida correctamente.");
        } catch (SQLException e) {
            System.out.println("Error al conectar a la base de datos: " + e.getMessage());
        }
	}
	
	
	public void insertEmpleat() {
		try {
			Scanner scanner = new Scanner(System.in);
	        System.out.print("Ingrese el ID del empleado: ");
	        int id = scanner.nextInt();
	        scanner.nextLine();  // Consumir la nueva línea después del entero
	        System.out.print("Ingrese el nombre del empleado: ");
	        String nom = scanner.nextLine();
	        System.out.print("Ingrese el descripcion del empleado: ");
	        String desc = scanner.nextLine();
	        System.out.print("Ingrese el dinero del empleado: ");
	        int dinero = scanner.nextInt();
	        System.out.print("Ingrese el puntos del empleado: ");
	        int puntos = scanner.nextInt();
	        System.out.print("Ingrese el nivel del empleado: ");
	        int nivel = scanner.nextInt();
	     
	        String query = "INSERT INTO Empleats (id, nom, descripcio, dinero, punts, nivell) " +
	                "VALUES (" + id + ", '" + nom + "', '" + desc + "', " + dinero + ", " + puntos + ", " + nivel + ")";
			Statement stmnt = conn.createStatement();
			stmnt.executeUpdate(query);
			System.out.println("Empleado insertado correctamente.");
			
			
			
			
		} catch (SQLException e) {
			
			System.out.println("Error al conectar a la base de datos: " + e.getMessage());
		}
	}
	

	public void deleteEmpleat(int dni) {
        try {
            // Crear la consulta SQL parametrizada para eliminar el empleado por DNI
            String query = "DELETE FROM granjeros WHERE id = '" + dni + "'";

            // Crear un Statement para ejecutar la consulta
            Statement statement = conn.createStatement();

            // Ejecutar la consulta para eliminar el empleado
            int rowsAffected = statement.executeUpdate(query);

            if (rowsAffected > 0) {
                System.out.println("Empleado eliminado correctamente.");
            } else {
                System.out.println("No se encontro ningun empleado con ese DNI.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

	}


	public void orderByName() {
		try {
            String query = "SELECT * FROM granjeros ORDER BY nombre";
            
            PreparedStatement ps = conn.prepareStatement(query);
            ResultSet rs = ps.executeQuery();
            
            ResultSetMetaData rsmd= rs.getMetaData(); 
            ArrayList<Empleats> empleados = new ArrayList<>();
            
            while(rs.next()) {
            	Empleats e = new Empleats(
            			rs.getInt(1),
                        rs.getString(2),
                        rs.getString(3),
                        rs.getInt(4),
                        rs.getInt(5),
                        rs.getInt(6)
            			);
            	empleados.add(e);
            }
            
            System.out.println("Lista de empleados ordenados por nombre:");
            for (Empleats empleado : empleados) {
                System.out.println(empleado.toString());
            }
            
			
			
        } catch (SQLException e) {
            System.out.println("Error al conectar a la base de datos: " + e.getMessage());
        }
	}

	public void operacionsResultSet() {
		try {
			
            // Mostrar todos los paises de la tabla PAISOS y almacenarlos en un ArrayList
            ArrayList<Object> lista = new ArrayList<>();
            String query = "Select * from paisos"; 
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            
            while (rs.next()) {
                int id = rs.getInt("id");
                String nombre = rs.getString("nombre");
                Paisos pais = new Paisos(id, nombre);
                lista.add(pais);
            }

            System.out.println("Países en la tabla PAISOS:");
            for (Object pais : lista) {
                System.out.println(pais);
            }
            

            // 2. Mostrar los nombres de los empleados que son del "Regne Unit"
            query = "SELECT nombre FROM EMPLEADOS WHERE pais = 'Regne Unit'";
            rs = stmt.executeQuery(query);
            System.out.println("Empleados del 'Regne Unit':");
            while (rs.next()) {
                System.out.println("Nombre = "+rs.getString(1));
            }
            
            lista.clear();

            // 3. Agregar dos nuevos empleados a la base de datos utilizando la información del ArrayList
            Empleats emp1 = new Empleats(1, "Juan", "Ventas", 3000, 150, 8);
            Empleats emp2 = new Empleats(2, "Ana", "Marketing", 3500, 180, 9);
            
            lista.add(emp1);
            lista.add(emp2);
            
            query = "INSERT INTO EMPLEADOS (id, nombre, descripcion, dinero, puntos, nivel) VALUES (?, ?, ?, ?, ?, ?)";
            PreparedStatement ps = conn.prepareStatement(query);
            
            for (Object emp : lista) {
                if (emp instanceof Empleats) {
                    Empleats empleado = (Empleats) emp;
                    ps.setInt(1, empleado.getId());
                    ps.setString(2, empleado.getNombre());
                    ps.setString(3, empleado.getDescripcion());
                    ps.setInt(4, empleado.getDinero());
                    ps.setInt(5, empleado.getPuntos());
                    ps.setInt(6, empleado.getNivel());
                    ps.executeUpdate();
                } else {
                    System.out.println("El objeto no es de tipo Empleats. No se puede insertar en la base de datos.");
                }
            }
            
            
            // 4. Mostrar todos los empleados que tengan CP 46100 utilizando PreparedStatement
            query = "SELECT * FROM EMPLEADOS WHERE codigo_postal = 46100";
            ps = conn.prepareStatement(query);

            
            rs = ps.executeQuery();

            // Mostrar los resultados
            System.out.println("Empleados con código postal 46100:");
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") +
                                   ", Nombre: " + rs.getString("nombre") +
                                   ", Código Postal: " + rs.getInt("codigo_postal"));
            }

            // 5. Insertar un nuevo registro en la base de datos utilizando el ResultSet anterior
           
            // Crear un Statement con ResultSet actualizable
            stmt = conn.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE);
            
            rs.moveToInsertRow();
            rs.updateInt(1, 500);
            rs.updateString(2, "pepe");
            rs.updateString(3, "descripcion");
            rs.updateInt(4, 1000);
            rs.updateInt(5, 200);
            rs.updateInt(6, 1);
            // Insertar la fila en la base de datos
            rs.insertRow();
            System.out.println("Nuevo empleado insertado correctamente.");

            
            // 6. Modificar todos los empleados de "Roma" y establecer la ciudad a "Napoles"
            ps = conn.prepareStatement("UPDATE EMPLEADOS SET ciudad = 'Napoles' WHERE ciudad = 'Roma'");
            int rowsAffected = ps.executeUpdate();
            System.out.println("Número de empleados de Roma actualizados a Napoles: " + rowsAffected);

        } catch (SQLException e) {
            e.printStackTrace();
        }
	}
}