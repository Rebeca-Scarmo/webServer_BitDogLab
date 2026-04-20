package config;

import jakarta.servlet.ServletContextEvent;
import jakarta.servlet.ServletContextListener;
import jakarta.servlet.annotation.WebListener;
import utils.ConexaoDB;

@WebListener
public class Inicializador implements ServletContextListener {
    @Override
    public void contextInitialized(ServletContextEvent sce) {
        ConexaoDB.inicializarBanco();
        System.out.println("Banco de dados verificado/inicializado com sucesso!");
    }
}