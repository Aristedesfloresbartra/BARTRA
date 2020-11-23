
package ModeloDAO;

import Conexion.Conexion;
import Modelo.Alumnos;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;


public class AlumnosDAO{
    
    Connection conexion;
    
    public AlumnosDAO(){
        
        Conexion con = new Conexion();
        conexion=con.getConexion();
        
    }
    
    public List<Alumnos>listarAlumnos(){
        
        PreparedStatement ps;
        ResultSet rs;    
        List<Alumnos> lista = new ArrayList<>();
        
        try {
            ps = conexion.prepareStatement("SELECT * FROM alumnos");
            rs = ps.executeQuery();
            
            while(rs.next()){
                
                int id = rs.getInt("id");
                String nombres = rs.getString("nombres");
                String apellidos = rs.getString("apellidos");
                String carrera = rs.getString("carrera");
                Double nota1 = rs.getDouble("nota1");
                Double nota2 = rs.getDouble("nota2");
                Double promedio = rs.getDouble("promedio");
                String estado = rs.getString("estado");
                Alumnos alumno = new Alumnos(id, nombres, apellidos, carrera, nota1, nota2, promedio, estado);
                
                lista.add(alumno);
                
            }
            return lista;
            
        }catch(SQLException e){
            System.err.println("Error al obteber los datos: " + e);
        }
        return null;
             
    }
        
    public Alumnos mostrarAlumnos(int _id){
        
        PreparedStatement ps;
        ResultSet rs;    
        Alumnos alumno = null;
        
        try {
            ps = conexion.prepareStatement("SELECT * FROM alumnos WHERE id=?");
            ps.setInt(1, _id);
            rs = ps.executeQuery();
            
            while(rs.next()){
                
                int id = rs.getInt("id");
                String nombres = rs.getString("nombres");
                String apellidos = rs.getString("apellidos");
                String carrera = rs.getString("carrera");
                Double nota1 = rs.getDouble("nota1");
                Double nota2 = rs.getDouble("nota2");
                Double promedio = rs.getDouble("promedio");
                String estado = rs.getString("estado");
                alumno = new Alumnos(id, nombres, apellidos, carrera, nota1, nota2, promedio,estado);  
                
            }
            return alumno;
            
        }catch(SQLException e){
            System.err.println("Error al obteber los datos del id: " + e);
        }
        return null;
             
    }
    
    public boolean insertar(Alumnos alumnos){
        
        PreparedStatement ps;
        
        try {
            
            ps = conexion.prepareStatement("INSERT INTO alumnos(id,nombres,apellidos,carrera,nota1,nota2,promedio,estado) VALUES (?,?,?,?,?,?,?,?)");
            ps.setInt(1, alumnos.getId());
            ps.setString(2, alumnos.getNombres());
            ps.setString(3, alumnos.getApellidos());
            ps.setString(4, alumnos.getCarrera());
            ps.setDouble(5, alumnos.getNota1());
            ps.setDouble(6, alumnos.getNota2());
            ps.setDouble(7, alumnos.getPromedio());  
            ps.setString(8, alumnos.getEstado());
            ps.execute();
            
            return true;
            
        }catch(SQLException e){
            System.err.println("Error al intentar registrar: " + e);
        }
        return false;
             
    }
    
    public boolean actualizar(Alumnos alumnos){
        
        PreparedStatement ps;
        
        try {
            
            ps = conexion.prepareStatement("UPDATE alumnos SET nombres=?,apellidos=?,carrera=?,nota1=?,nota2=?,promedio=?,estado=? WHERE id=?");
            ps.setString(1, alumnos.getNombres());
            ps.setString(2, alumnos.getApellidos());
            ps.setString(3, alumnos.getCarrera());
            ps.setDouble(4, alumnos.getNota1());
            ps.setDouble(5, alumnos.getNota2());
            ps.setDouble(6, alumnos.getPromedio());  
            ps.setString(7, alumnos.getEstado());
            ps.setInt(8,alumnos.getId());
            ps.execute();
            
            return true;
            
        }catch(SQLException e){
            System.err.println("Error al intentar editar: " + e);
        }
        return false;
             
    }
    
    public boolean eliminar(int _id){
        
        PreparedStatement ps;
        
        try {
            
            ps = conexion.prepareStatement("DELETE FROM alumnos WHERE id=?"); 
            ps.setInt(1,_id);
            ps.execute();
            
            return true;
            
        }catch(SQLException e){
            System.err.println("Error al intentar eliminar: " + e);
        }
        return false;
             
    }
    
    
}
