
package ModeloDAO;

import Conexion.Conexion;
import Modelo.Productos;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;


public class ProductosDAO {
    
    Connection conexion;
    
    public ProductosDAO(){
        
        Conexion con = new Conexion();
        conexion=con.getConexion();
        
    }
    
     public List<Productos>listarProductos(){
        
        PreparedStatement ps;
        ResultSet rs;    
        List<Productos> lista = new ArrayList<>();
        
        try {
            ps = conexion.prepareStatement("SELECT * FROM productos");
            rs = ps.executeQuery();
            
            while(rs.next()){     
                int id = rs.getInt("id");
                String nombre = rs.getString("nombre");
                String categoria = rs.getString("categoria");
                int cantidad = rs.getInt("cantidad");
                Double precio = rs.getDouble("precio");
                Productos producto = new Productos(id, nombre, categoria, cantidad, precio);
                lista.add(producto);
            }
            return lista;
            
        }catch(SQLException e){
            System.err.println("Error en la consulta: " + e);
        }
        return null;
             
    }
    
     public Productos mostrarProductos(int _id){
        
        PreparedStatement ps;
        ResultSet rs;    
        Productos producto=null;
        
        try {
            ps = conexion.prepareStatement("SELECT * FROM productos WHERE id=?");
            ps.setInt(1, _id);
            rs = ps.executeQuery();
            
            while(rs.next()){     
                int id = rs.getInt("id");
                String nombre = rs.getString("nombre");
                String categoria = rs.getString("categoria");
                int cantidad = rs.getInt("cantidad");
                Double precio = rs.getDouble("precio");
                producto = new Productos(id, nombre, categoria, cantidad, precio);
               
            }
            return producto;
            
        }catch(SQLException e){
            System.err.println("Error al traer los datos: " + e);
        }
        return null;
             
    }
    
     public boolean insertar(Productos producto){
        
        PreparedStatement ps;
        
        try {
            ps = conexion.prepareStatement("INSERT INTO productos(nombre,categoria,cantidad,precio) VALUES (?,?,?,?)");
            ps.setString(1,producto.getNombre());
            ps.setString(2,producto.getCategoria());
            ps.setInt(3,producto.getCantidad());
            ps.setDouble(4,producto.getPrecio());
            ps.executeUpdate();
            return true;
                           
        }catch(SQLException e){
            System.err.println("Error al insertar los datos : " + e);
        }
        return false;
             
    }

     public boolean actualizar(Productos producto){
        
        PreparedStatement ps;
        
        try {
            ps = conexion.prepareStatement("UPDATE productos SET nombre=?,categoria=?,cantidad=?,precio=? WHERE id=?");
            ps.setString(1,producto.getNombre());
            ps.setString(2,producto.getCategoria());
            ps.setInt(3,producto.getCantidad());
            ps.setDouble(4,producto.getPrecio());
            ps.setInt(5,producto.getId());
            ps.executeUpdate();
            return true;
                           
        }catch(SQLException e){
            System.err.println("Error al intentar editar: " + e);
        }
        return false;
             
    }
     
     public boolean eliminar(int _id){
        
        PreparedStatement ps;
        
        try {
            
            ps = conexion.prepareStatement("DELETE FROM productos WHERE id=?"); 
            ps.setInt(1, _id);
            ps.executeUpdate();       
            return true;
            
        }catch(SQLException e){
            System.err.println("Error al intentar eliminar: " + e);
        }
        return false;
             
    }
     
     public List Buscar(String datos){
         PreparedStatement ps;
         ResultSet rs;
         
         List<Productos>lista = new ArrayList<>();
         String sql;
         sql = "SELECT * FROM productos WHERE categoria LIKE '%" + datos + "%'";
         try{
            ps = conexion.prepareStatement(sql);
            rs = ps.executeQuery(); 
            while(rs.next()){
                int id = rs.getInt("id");
                String nombre = rs.getString("nombre");
                String categoria = rs.getString("categoria");
                int cantidad = rs.getInt("cantidad");
                Double precio = rs.getDouble("precio");
                Productos producto = new Productos(id, nombre, categoria, cantidad, precio);
                lista.add(producto);
            }
             
         }catch(SQLException e){
             System.err.println("No se encontro datos correspondientes: " + e);
         }
         return lista;
         
     }
    
}
