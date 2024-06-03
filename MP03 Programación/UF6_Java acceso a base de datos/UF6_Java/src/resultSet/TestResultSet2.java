package resultSet;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Timer;
import java.util.TimerTask;

public class TestResultSet2 {

	public static void main(String[] args) {
		String urlDatos = "jdbc:mysql://localhost/farmville?serverTimezone=UTC&autoReconnect=true&useSSL=false";
		String usuario = "root";
		String pass = "P@ssw0rd";
		String query = "Select * from construcciones";
		try {			
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection conn = DriverManager.getConnection(urlDatos,usuario,pass);
			
//			Statement stmnt = conn.createStatement(); //por defecto es TYPE_FORWARD_ONLY y CONCUR_READ_ONLY
			
			Statement stmnt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_UPDATABLE);
			ResultSet rs = stmnt.executeQuery(query);
			
/*			//Tipos de resultset:
 * 
 *				- TYPE_FORWARD_ONLY: tipo por defecto, solo se puede navegar por este hacia adelante
 *				- TYPE_SCROLL_INSENSITIVE: puede navegar hacia adelante y hacia atras, no refleja los cambios en la base de datos
				- TYPE_SCROLL_SENSITIVE: refleja los cambios en la base de datos
				
			//tipos de concurrencia en los ResultSet:
			  	- CONCUR_READ_ONLY: si ejecuto una query en el resultSet, muestra los datos de la bbdd pero NO se pueden MODIFICAR
			  	- CONCUR_UPDATABLE: si ejecutas la query y modificas el ResultSet, se ve reflejado en la base de datos
*/			
			
			
			//Para comprobar que esta pasando con los TYPE Y CONCUR de resultSet | nos da mas info de la base de datos
			DatabaseMetaData metaData = conn.getMetaData();
			
			
			//Comprobar si mi base de datos soporta los tipos de ResultSet:
			
			//boolean estaSoportado = metaData.supportsResultSetType(ResultSet.TYPE_SCROLL_SENSITIVE);
			boolean estaSoportado = metaData.supportsResultSetConcurrency(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_UPDATABLE);
			if (estaSoportado) {
				System.out.println("Esta base de datos soporta este tipo de result set");
			}else {
				System.out.println("Esta base de datos NO soporta este tipo de result set");
			}
			

			
			
			
			rs.next(); // cursor en primera fila del resultSet
			
			System.out.println("ID = "+rs.getInt(1) + " Nombre = "+rs.getString(2)+ " Precio = "+rs.getInt(3));	
			
			//RSMetaData = nos da información acerca de nuestro Result Set			
			ResultSetMetaData rsmd = rs.getMetaData();
			
			
			//actualizarMostrarRegistros(rs);
			//insertarRegistro(rs);
			//eliminarRegistro(rs);
			
		} catch (ClassNotFoundException e) {
			System.out.println("Driver no se ha cargado correctamente");
			
			
		} catch (SQLException e) {
			System.out.println("Error en la conexion");
		}
	}
	
	
	
	public static void actualizarMostrarRegistros(ResultSet rs) {
		Timer t = new Timer();
		int i = 0;
		t.scheduleAtFixedRate(new TimerTask() {
			
			public void run() {
				try {
					rs.absolute(5);
					
					rs.updateInt("precio", rs.getInt(3)+1);// Actualizar registros de la base de datos directamente
					rs.updateRow();
					
					System.out.println("ID = "+rs.getInt(1) + " Nombre = "+rs.getString(2)+ " Precio = "+rs.getInt(3));
					
										
					
				} catch (SQLException e) {
					e.printStackTrace();
				}
				
				
			}
		}, 1*10*1000, 1*10*1000);
		//minutos * segundos * milisegundos		
	} 
	
	public static void insertarRegistro(ResultSet rs) {
		try {
			//primero ponemos el apuntador en el ultimo registro
			rs.moveToInsertRow();					 
			     //columna, valor
			rs.updateInt(1, 200);
			rs.updateString(2,"Invernadero");
			rs.updateInt(3, 5000);
			rs.updateInt(4, 10);			
			rs.insertRow();// esto es apra realizar el insert en la base de datos
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	public static void eliminarRegistro(ResultSet rs) {
		
		try {
			rs.last(); //se posiciona en el ultimo registro
			rs.deleteRow(); //borra el registro en el puntero
								
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
