package pt49resultSet;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

import pt48modificacio.Main48;

public class Main49 {

	public static void main(String[] args) {
		Main49 myclass = new Main49();
        String urlDatos = "jdbc:mysql://localhost/farmville?serverTimezone=UTC&autoReconnect=true&useSSL=false";
        String usuario = "root";
        String pass = "P@ssw0rd";
       
        Scanner sc = new Scanner(System.in);
        
        //query con los datos pedidos (a)
        String query = "Select id, nombre, nivel from granjeros";

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(urlDatos, usuario, pass);
            
            Statement stmnt = conn.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE);
            
                        
            // almacenar consulta en result set (a)
            ResultSet rs = stmnt.executeQuery(query);
            
            //Meta datos de rs
            ResultSetMetaData rsmd = rs.getMetaData();
            
            /*
            // datos almacenados (a)
            while(rs.next()) {
            	System.out.println("ID = "+ rs.getInt(1) + " Nombre = "+rs.getString(2)+ " Nivel = "+rs.getInt(3));
            }
            System.out.println("\n--------------------------------\n");
            
            
            //Reseteo del ResultSet para volver a printear todos los resultados (b)
            rs.absolute(0);
            */
            
            while(rs.next()) {
            	System.out.println(rsmd.getColumnName(2)+": = "+rs.getString(2)+", "+rsmd.getColumnName(3)+": = "+rs.getInt(3));         
            }
            
            System.out.println("\n--------------------------------\n");
            
            
            //(c)  PARA HACERLO CONFIGURAR EL STATEMENT: ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE 
           
            /*
            rs.absolute(0);
            System.out.println(rs.getRow());
            System.out.println("Usuarios modificados:");
            
            while(rs.next()) {            	  	
            	if(rs.getInt(3) > 8) {
            		System.out.println(rs.getRow());  
            		rs.updateInt("nivel", rs.getInt(3)+1);
            		rs.updateRow();
            		
            		System.out.println(rsmd.getColumnName(2)+": = "+rs.getString(2)+", "+rsmd.getColumnName(3)+": = "+rs.getInt(3));
            	}           	         
            }
            */
            
            
            // d
            rs.absolute(0);
            System.out.println(rs.getRow());
            System.out.println("Usuarios cada 5:");
            
            while(rs.next()) {            	  	
            	
	    		System.out.println(rs.getRow());                		
	    		System.out.println(rsmd.getColumnName(2)+": = "+rs.getString(2)+", "+rsmd.getColumnName(3)+": = "+rs.getInt(3));
            	rs.relative(4);          	         
            }

            
            // e Crear una nueva consulta para almacenar todos los datos de la tabla granjer
            	query = "Select * FROM granjeros";
            
            stmnt = conn.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE);
            rs = stmnt.executeQuery(query);
            rsmd = rs.getMetaData();
            
            
            
            System.out.println("Datos de la tabla granjeros:");
            while (rs.next()) {
                System.out.println(rsmd.getColumnName(1)+ " = " + rs.getInt(1) + 
                					rsmd.getColumnName(2) + " = "+ rs.getString(2) +
                					rsmd.getColumnName(3) + " = "+ rs.getString(3)+ 
                					rsmd.getColumnName(4) + " = "+ rs.getInt(4)+
                					rsmd.getColumnName(5) + " = "+ rs.getInt(5)+ 
                					rsmd.getColumnName(6) + " = "+rs.getInt(6));
            }
            System.out.println("\n--------------------------------\n");
            
            //f anadir tres registros en la base de datos
            
            rs.moveToInsertRow();
            rs.updateInt(1, 200);
            rs.updateString(2, "Willy1");
            rs.updateString(3, "Rabioso");
            rs.updateInt(4, 2000);
            rs.updateInt(5, 666);
            rs.updateInt(5, 66);
            rs.insertRow();

            rs.moveToInsertRow();
            rs.updateInt(1, 300);
            rs.updateString(2, "Willy2");
            rs.updateString(3, "Tranquilo");
            rs.updateInt(4, 2000);
            rs.updateInt(5, 666);
            rs.updateInt(5, 66);
            rs.insertRow();

            rs.moveToInsertRow();
            rs.updateInt(1, 400);
            rs.updateString(2, "Willy3");
            rs.updateString(3, "Dormido");
            rs.updateInt(4, 2000);
            rs.updateInt(5, 666);
            rs.updateInt(5, 66);
            rs.insertRow();
            
            
            //Comprobar que queda reflejado en la abse de datos
            rs.absolute(0);
            System.out.println("Después de la inserción:");
            while (rs.next()) {
            	System.out.println(rsmd.getColumnName(1)+ " = " + rs.getInt(1) + 
    					rsmd.getColumnName(2) + " = "+ rs.getString(2) +
    					rsmd.getColumnName(3) + " = "+ rs.getString(3)+ 
    					rsmd.getColumnName(4) + " = "+ rs.getInt(4)+
    					rsmd.getColumnName(5) + " = "+ rs.getInt(5)+ 
    					rsmd.getColumnName(6) + " = "+rs.getInt(6));
            }
            System.out.println("\n--------------------------------\n");
            
            
            //g borrar resulset con registro ID = 200 (tambien el resto creaados):
            
            rs.absolute(0);
            
            while(rs.next()) {            	  	
            	if(rs.getInt(1) == 200) {
            		
            		rs.deleteRow();           		            		
            		System.out.println("Registro 200 eliminado correctamente");
            	} 
            }
            
            rs.absolute(0);
            System.out.println("Después de Borrar ID 200:");
            while (rs.next()) {
            	System.out.println(rsmd.getColumnName(1)+ " = " + rs.getInt(1) + 
    					rsmd.getColumnName(2) + " = "+ rs.getString(2) +
    					rsmd.getColumnName(3) + " = "+ rs.getString(3)+ 
    					rsmd.getColumnName(4) + " = "+ rs.getInt(4)+
    					rsmd.getColumnName(5) + " = "+ rs.getInt(5)+ 
    					rsmd.getColumnName(6) + " = "+rs.getInt(6));
            }
            System.out.println("\n--------------------------------\n");
            
            
            //conn.close();
        } catch (ClassNotFoundException e) {
            System.out.println("Driver no se ha cargado correctamente");

        } catch (SQLException e) {
            System.out.println("Error en la conexion");
            e.printStackTrace();
        }

        //sc.close(); // Cerrar scanner al finalizar

	}

}
