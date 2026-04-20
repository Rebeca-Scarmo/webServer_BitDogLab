package servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import com.google.gson.Gson;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import model.Leitura;
import utils.ConexaoDB;

@WebServlet("/api/dados")
public class PainelServlet extends HttpServlet {
    
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        ArrayList<Leitura> lista = new ArrayList<>();
        
        try (Connection conn = ConexaoDB.getConexao(); 
             PreparedStatement stmt = conn.prepareStatement("SELECT * FROM LEITURAS ORDER BY id DESC");
             ResultSet rs = stmt.executeQuery()) {
            
            while(rs.next()) {
                lista.add(new Leitura(
                    rs.getInt("id"), 
                    rs.getDouble("temperatura"), 
                    rs.getDouble("umidade")
                ));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");
        PrintWriter saida = response.getWriter();
        saida.print(new Gson().toJson(lista));
        saida.flush();
    }
}