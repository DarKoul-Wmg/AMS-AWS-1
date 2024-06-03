package apuntesUF6;
import java.sql.*;
import java.util.ArrayList;


public class Main2 {

	private ArrayList<Player> players = null;
	public static void main(String[] args) {
		String urlDatos = "jdbc:mysql://localhost/BridgeClub?serverTimezone=UTC&autoReconnect=true&useSSL=false";
		String usuario = "root";
		String pass = "P@ssw0rd";
		
		ArrayList<Player> players = new ArrayList<Player>();
		players.add(new Player(100, "4700001T", "Juan", 100000, 108));
		players.add(new Player(157, "4700001T", "Paco", 350000, 147));
		players.add(new Player(124, "4700001T", "Ivan", 420000, 302));
		players.add(new Player(402, "4700001T", "Luis", 60000, 147));
		
		try {
									
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection conn = DriverManager.getConnection(urlDatos,usuario,pass);
			System.out.println("Conexion creada correctamente.");
			Statement stmnt = conn.createStatement();
			
			System.out.println("------------------------------------------");
			System.out.println("Ingresar Paises");
			System.out.println("------------------------------------------");

			String insert = "insert into countries(id, countryName) values(147, 'United Kingdom')";
			System.out.println(insert);
			stmnt.executeUpdate(insert);
			insert = "insert into countries(id, countryName) values(201, 'Portugal')";
			System.out.println(insert);
			stmnt.executeUpdate(insert);
			insert = "insert into countries(id, countryName) values(302, 'Finland')";
			System.out.println(insert);
			stmnt.executeUpdate(insert);
			insert = "insert into countries(id, countryName) values(108, 'Spain')";
			System.out.println(insert);
			stmnt.executeUpdate(insert);

			System.out.println("------------------------------------------");
			System.out.println("Ingresar Players");
			System.out.println("------------------------------------------");
			

			for (Player p : players) {
				int idExists, idCountryExists;
				
				String _query = "Select count(*) from players where id = " + p.getId()+ ";";
				ResultSet rs = stmnt.executeQuery(_query);
				rs.next();
				idExists = rs.getInt(1);
				_query = "Select count(*) from countries where id = " + p.getIdPais()+ ";";
				rs = stmnt.executeQuery(_query);
				rs.next();
				idCountryExists = rs.getInt(1);
				System.out.println(idExists);
				System.out.println(idCountryExists);
				if (idExists == 0) {
					if (idCountryExists == 1) {
						insert = "insert into players(id, dni, playerName, points, idCountry) "
								+ "values(" + p.getId() + ",'" + p.getDni() + "','" + p.getName() + "'," + p.getPoints() + "," + p.getIdPais()+");";
						System.out.println(insert);
						stmnt.executeUpdate(insert);
					}
					System.out.println("No existe ningun pais con esa id");
				}
				else
				{
					System.out.println("Ya existe un usuario con esa id");
				}
				
				
			}

			System.out.println(">> Insert realizado correctamente");
			
			String query = "select * from players"; 
			ResultSet rs = stmnt.executeQuery(query);
			ResultSetMetaData rsmd = rs.getMetaData();
			while (rs.next())
			{
				System.out.println(rsmd.getColumnName(1) + " := " + rs.getInt(1) + ", "
				+ rsmd.getColumnName(2) + " := " + rs.getString(2) + ", "
				+ rsmd.getColumnName(3) + " := " + rs.getString(3)+ ", "
				+ rsmd.getColumnName(4) + " := " + rs.getInt(4)+ ", "
				+ rsmd.getColumnName(5) + " := " + rs.getInt(5));
			}
			System.out.println("------------------------------------------");
			System.out.println("ID > 150");
			System.out.println("------------------------------------------");
			rs.beforeFirst();
			while (rs.next())
			{
				if(rs.getInt(1) >= 150)
				{
					System.out.println(rsmd.getColumnName(1) + " := " + rs.getInt(1) + ", "
							+ rsmd.getColumnName(2) + " := " + rs.getString(2) + ", "
							+ rsmd.getColumnName(3) + " := " + rs.getString(3)+ ", "
							+ rsmd.getColumnName(4) + " := " + rs.getInt(4)+ ", "
							+ rsmd.getColumnName(5) + " := " + rs.getInt(5));
				}
				
			}
			players.clear();
			players.add(new Player(423, "4700001T", "Pedro", 1200000, 108));
			players.add(new Player(7, "4700001T", "Alfonso", 100000, 147));
			
			String update = "INSERT INTO players(id, dni, playerName, points, idCountry) VALUES (?,?,?,?,?)";
			PreparedStatement ps = conn.prepareStatement(update);
			
			for (Player p : players) {
				ps.setInt(1, p.getId());
				ps.setString(2, p.getDni());
				ps.setString(3, p.getName());
				ps.setInt(4, p.getPoints());
				ps.setInt(5, p.getIdPais());
				ps.executeUpdate();
			}
			
			System.out.println(">> Insert realizado correctamente");
			System.out.println("------------------------------------------");
			System.out.println("Consulta puntos + UK");
			System.out.println("------------------------------------------");
			query = "Select * from players where points > ? and idCountry = ?";
			ps = conn.prepareStatement(query);
			ps.setInt(1, 10000);
			ps.setInt(2, 147);
			rs = ps.executeQuery();
			while (rs.next()) {
				System.out.println(rsmd.getColumnName(1) + " := " + rs.getInt(1) + ", "
						+ rsmd.getColumnName(2) + " := " + rs.getString(2) + ", "
						+ rsmd.getColumnName(3) + " := " + rs.getString(3)+ ", "
						+ rsmd.getColumnName(4) + " := " + rs.getInt(4)+ ", "
						+ rsmd.getColumnName(5) + " := " + rs.getInt(5));
			}
			
			System.out.println("------------------------------------------");
			System.out.println("Insert ResultSet");
			System.out.println("------------------------------------------");
			
			rs.updateRow();
			
			System.out.println("------------------------------------------");
			System.out.println("Update table players");
			System.out.println("------------------------------------------");
			
			query = "update players set points = 10000 where points > ?;";
			ps = conn.prepareStatement(query);
			ps.setInt(1, 10000);
			ps.executeUpdate();
			System.out.println(">> Update realizado correctamente");
		} catch (ClassNotFoundException e) {
			System.out.println("Error! Class Not Found");
			e.printStackTrace();
		} catch (SQLException e) {
			System.out.println("Error! SQL Exception");
			e.printStackTrace();
		}
	}

}
