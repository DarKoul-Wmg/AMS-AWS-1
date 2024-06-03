package statement_PreparedStatement;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

public class TestJDBC2 {

	public static void main(String[] args) {
		
		String urlDatos = "jdbc:mysql://localhost/farmville?serverTimezone=UTC";
		String usuario = "root";
		String pass = "P@ssw0rd";
		
		ArrayList<Construcciones> construcciones = new ArrayList<Construcciones>();
		Construcciones c1 = new Construcciones(201,"establo",200,35);
		Construcciones c2 = new Construcciones(202,"granja",300,25);
		Construcciones c3 = new Construcciones(203,"palomar",400,15);
		construcciones.add(c1);
		construcciones.add(c2);
		construcciones.add(c3);
		

		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection conn = DriverManager.getConnection(urlDatos,usuario,pass);
			Statement stmnt = conn.createStatement();
			
			
			for (Construcciones c : construcciones) {
				String update = "INSERT INTO construcciones ( id, nombre  , precio, id_granjero ) VALUES ("+c.getId()+
						", \""+c.getNombre()+" \" ,"+c.getPrecio()+","+c.getId_granjero()+")";
				// se usa \" para que el sistema detecte la comilla
				
				System.out.println(update);
				stmnt.executeUpdate(update); // metodo para actualziar la tabla con el insert
			}
			
			
			String query = "Select * from construcciones"; 
			ResultSet rs = stmnt.executeQuery(query);
			while (rs.next()) {
				System.out.println("ID = "+rs.getInt(1)+" Nombre = "+rs.getString(2)+ " Precio = "+rs.getInt(3));
			}
			
			
			//borrar construcciones del arraylist
			for (Construcciones c : construcciones) {
				String update = "delete  from construcciones where id="+c.getId();
				System.out.println(update);
				stmnt.executeUpdate(update); //borrar registros tambien es una actualizacion
			}
			
			
			System.out.println("PREPARED STATEMENT:");
			
			
			
			
			// Insercion registros mediante PreparedStatement
			
			String update = "INSERT INTO construcciones ( id, nombre  , precio, id_granjero ) VALUES (?,?,?,?)";
			PreparedStatement ps = conn.prepareStatement(update);
			
			for (Construcciones c : construcciones) { //asigna los valores correspondientes a los parametros ?
					    //x ese es el parametro
				ps.setInt(1, c.getId());
				ps.setString(2, c.getNombre());
				ps.setInt(3, c.getPrecio());
				ps.setInt(4, c.getId_granjero());
				ps.executeUpdate();
			}
			
			// Consulta de registros mediante PreparedStatement
			
			query = "Select * from construcciones where id > ?";
			ps = conn.prepareStatement(query);
				    //(parametro ?, valor)
			ps.setInt(1, 100);
			
			rs = ps.executeQuery(); //porque es consulta
			
			while (rs.next()) {
				System.out.println("ID = "+rs.getInt(1)+" Nombre = "+rs.getString(2)+ " Precio = "+rs.getInt(3));
			}
			
			
			// Borrar registros de la BBDD cuyo id coincide con el id de los registros del array List.
				
			for (Construcciones c : construcciones) {
				update = "delete  from construcciones where id=? ";
				ps = conn.prepareStatement(update);
				ps.setInt(1, c.getId());// sustituye id por cada elemento en la arrayList para borrarlo
				ps.executeUpdate();
			}
			
			
			
		} catch (ClassNotFoundException e) {
			System.out.println("Driver no se ha cargado correctamente!!");		
		} catch (SQLException e) {
			System.out.println("Se ha lanzado una SQLException!!");
			e.printStackTrace();
		}
		

	}

}

/*

	Statement: Cuando queramos hacer consultas simples y que solo sea una vez:
	 - (select * from construcciones), no suele usar parametros.
	
	
	
	PreparedStatement: Cuando tengamos que parametrizar y realizar varias veces una misma
		consulta:
		
		String update = "INSERT INTO construcciones ( id, nombre  , precio, id_granjero ) VALUES (?,?,?,?)";
			PreparedStatement ps = conn.prepareStatement(update);
			
			for (Construcciones c : construcciones) { //asigna los valores correspondientes a los parametros ?
					    //x ese es el parametro
				ps.setInt(1, c.getId());
				ps.setString(2, c.getNombre());
				ps.setInt(3, c.getPrecio());
				ps.setInt(4, c.getId_granjero());
				ps.executeUpdate();
			}
		--> (mejor rendimiento porque guarda la cpnsulta en cache para el resto)

*/
class Construcciones{
	private int id;
	private String nombre;
	private int precio;
	private int id_granjero;
	public Construcciones(int id, String nombre, int precio, int id_granjero) {
		super();
		this.id = id;
		this.nombre = nombre;
		this.precio = precio;
		this.id_granjero = id_granjero;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getPrecio() {
		return precio;
	}
	public void setPrecio(int precio) {
		this.precio = precio;
	}
	public int getId_granjero() {
		return id_granjero;
	}
	public void setId_granjero(int id_granjero) {
		this.id_granjero = id_granjero;
	}
	
	
	
}

