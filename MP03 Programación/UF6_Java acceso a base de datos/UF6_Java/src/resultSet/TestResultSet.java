package resultSet;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;

public class TestResultSet {

	public static void main(String[] args) {
		String urlDatos = "jdbc:mysql://localhost/farmville?serverTimezone=UTC";
		String usuario = "root";
		String pass = "P@ssw0rd";
		String query = "Select * from construcciones";
		try {			
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection conn = DriverManager.getConnection(urlDatos,usuario,pass);
			Statement stmnt = conn.createStatement();
			ResultSet rs = stmnt.executeQuery(query);
			
			rs.next(); // cursor en primera fila del resultSet
			
			System.out.println("ID = "+rs.getInt(1) + " Nombre = "+rs.getString(2)+ " Precio = "+rs.getInt(3));

/*
			rs.next();
			
			System.out.println("ID = "+rs.getInt(1) + " Nombre = "+rs.getString(2)+ " Precio = "+rs.getInt(3));
			
			
			//ver el primer registro otra vez:
			
			rs.previous();
			System.out.println("ID = "+rs.getInt(1) + " Nombre = "+rs.getString(2)+ " Precio = "+rs.getInt(3));
			
			
			//ver registro X
			
			rs.absolute(10);
			System.out.println("ID = "+rs.getInt(1) + " Nombre = "+rs.getString(2)+ " Precio = "+rs.getInt(3));
			
			
			//avanzar x registros hacia deltante (en este caso 5) da el rs 15
			
			rs.relative(5); 
			System.out.println("ID = "+rs.getInt(1) + " Nombre = "+rs.getString(2)+ " Precio = "+rs.getInt(3));
			
			
			//registro donde estamos    rs.getRow();
			System.out.println("Fila: = "+rs.getRow());
*/	
			
			
			//RSMetaData = nos da información acerca de nuestro Result Set
			
			ResultSetMetaData rsmd = rs.getMetaData();
			
			System.out.println("Metadatos del resultSet:");
			System.out.println(rsmd.toString());
			
			//Bucle para mostrar los nombres de columna y el tipo de datos que almacena
			
			
//	       1 porque no hay columna 0	     .Sirve para sacar el total de columnas
			for (int i = 1 ; i <= rsmd.getColumnCount() ; i++) {
				
//									Obtener el nombre de la columna   Obtener el tipo de la columna
				System.out.println(rsmd.getColumnName(i)+" --> "+rsmd.getColumnType(i));
			}
			
			
//			En vez de introducir el nombre de la columna a mano, podemos usar los .GetColumnName()
			System.out.println(rsmd.getColumnName(1)+" = "+rs.getInt(1) + "  "+
							  	rsmd.getColumnName(2)+" = "+rs.getString(2)+ "  "+
							  	 rsmd.getColumnName(3)+" = "+rs.getInt(3));
			
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
