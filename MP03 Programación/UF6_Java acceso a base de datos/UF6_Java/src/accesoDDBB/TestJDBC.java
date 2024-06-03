package accesoDDBB;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Timer;
import java.util.TimerTask;

public class TestJDBC {

	public static void main(String[] args) {
		
		String urlDatos = "jdbc:mysql://localhost/farmville?serverTimezone=UTC";
		String usuario = "root";
		String pass = "P@ssw0rd";
		
		try {
			
			//cargar driver
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//Crear conexion con  BBDD
			Connection conn = DriverManager.getConnection(urlDatos,usuario,pass);
			
			//Crear consulta
			String query = "Select * from construcciones where precio > 400";
			
			//Instanciar objeto de la clase consulta
			Statement stmnt = conn.createStatement();
			
			//Ejecutar la consultaa
			ResultSet rs = stmnt.executeQuery(query);
			
			while(rs.next()) { //Mientras haya un registro, el apuntador sigue recorrriendo por todos los registros
				
				System.out.println("ID = "+rs.getInt(1) + " Nombre = "+rs.getString(2) + " Precio = "+rs.getInt(3));
			}
			
		} catch (ClassNotFoundException e) {
			System.out.println("Driver no se ha cargado correctamente");
			
			
		} catch (SQLException e) {
			System.out.println("Error en la conexion");
		}
	}
	
	public static void actualizarMoatrarRegistros(ResultSet rs) {
		Timer t = new Timer();
		int i = 0;
		t.scheduleAtFixedRate(new TimerTask() {
			
			public void run() {
				
				
				
			}
		}, 1*10*1000, 1*10*1000);
		//minutos * segundos * milisegundos
		
	}
}