

package Conexion;
 
import com.mysql.jdbc.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;


public class Conexion {
    
    public Connection getConexion(){
        
        try{
            
            Class.forName("com.mysql.jdbc.Driver");
            Connection conexion = (Connection) DriverManager.getConnection("jdbc:mysql://localhost:3306/escuela?serverTimezone=UTC","root","");
            System.out.println("Conexion exitosa");
            return conexion;
            
        }catch(SQLException e){
            
            System.err.println("Error en la conexion: " + e);
            
        }
        
        catch (ClassNotFoundException ex) {
            Logger.getLogger(Conexion.class.getName()).log(Level.SEVERE, null, ex);
            
        }
        return null;
    }
   
}
