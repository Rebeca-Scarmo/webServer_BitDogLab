package app;

import java.io.BufferedReader;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.PreparedStatement;
import utils.ConexaoDB;

public class ImportadorCSV {
    public static void main(String[] args) {
        String arquivoCSV = "C:\\Users\\alves\\Downloads\\dadosCSV.csv"; //onde fica o arquivo baixado dos dados em csv
        
        ConexaoDB.inicializarBanco(); 

        String sql = "INSERT INTO LEITURAS (temperatura, umidade) VALUES (?, ?)";

        try (BufferedReader br = new BufferedReader(new FileReader(arquivoCSV));
             Connection conn = ConexaoDB.getConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            String linha;
            int contador = 0;

            while ((linha = br.readLine()) != null) {
                String[] colunas = linha.split(",");
                if (colunas.length >= 2) {
                    try {
                        double temp = Double.parseDouble(colunas[0].trim().replace(",", "."));
                        double umid = Double.parseDouble(colunas[1].trim().replace(",", "."));

                        stmt.setDouble(1, temp);
                        stmt.setDouble(2, umid);
                        stmt.executeUpdate();
                        contador++;
                    } catch (NumberFormatException e) {
                        
                    }
                }
            }
            System.out.println(contador + "registros importados do CSV para o banco");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}