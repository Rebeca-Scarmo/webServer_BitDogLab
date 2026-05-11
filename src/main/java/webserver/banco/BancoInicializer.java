package webserver.banco;
import jakarta.servlet.ServletContextListener;
import jakarta.servlet.annotation.WebListener;
import jakarta.servlet.ServletContextEvent;
import java.sql.SQLException;

@WebListener
public class BancoInicializer implements ServletContextListener {

	@Override
	public void contextInitialized(ServletContextEvent sce) {
		try {
		    BancoManager.inicializer();
		} catch (SQLException e) {
		    e.printStackTrace();
		} catch (ClassNotFoundException e) {
		    e.printStackTrace();
		}
}
}
