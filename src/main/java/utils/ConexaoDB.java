package utils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class ConexaoDB {
    
	private static final String URL = "jdbc:h2:file:D:/FACULDADE/PROJETOS/INICIAÇÃO CIENTIFICA/coleta-de-dados/banco_sensores;AUTO_SERVER=TRUE";
    private static final String USER = "sa";
    private static final String PASS = "";

    public static Connection getConexao() throws SQLException {
        try {
            Class.forName("org.h2.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        return DriverManager.getConnection(URL, USER, PASS);
    }

    public static void inicializarBanco() {
        try (Connection conn = getConexao(); Statement stmt = conn.createStatement()) {
            String sql = "CREATE TABLE IF NOT EXISTS LEITURAS (" +
                         "id INT AUTO_INCREMENT PRIMARY KEY, " +
                         "temperatura DOUBLE, " +
                         "umidade DOUBLE)";
            stmt.execute(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}