
package Controlador;

import Modelo.Productos;
import ModeloDAO.ProductosDAO;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet(name = "CProductos", urlPatterns = {"/CProductos"})
public class CProductos extends HttpServlet {

   
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
        
        ProductosDAO productosDAO = new ProductosDAO();
        String accion;
        RequestDispatcher dispatcher = null;
        accion = request.getParameter("accion");
        
        if(accion == null || accion.isEmpty()){
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Productos>listarProductos = productosDAO.listarProductos();
            request.setAttribute("lista",listarProductos);
        }else if(accion.equalsIgnoreCase("nuevo")){
            dispatcher = request.getRequestDispatcher("vista/registrar.jsp");  
           
        }
        else if(accion.equalsIgnoreCase("insertar")){
            String nombre = request.getParameter("nombre");
            String categoria = request.getParameter("categoria");
            int cantidad = Integer.parseInt(request.getParameter("cantidad"));
            Double precio = Double.parseDouble(request.getParameter("precio"));
            
            Productos producto = new Productos(0, nombre, categoria, cantidad, precio);
            productosDAO.insertar(producto);
            
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Productos>listarProductos = productosDAO.listarProductos();
            request.setAttribute("lista",listarProductos);
            
        }else if(accion.equalsIgnoreCase("modificar")){
            dispatcher = request.getRequestDispatcher("vista/editar.jsp");  
            int id = Integer.parseInt(request.getParameter("id"));
            Productos producto = productosDAO.mostrarProductos(id);
            request.setAttribute("producto",producto); 
            
        }else if(accion.equalsIgnoreCase("actualizar")){
            int id = Integer.parseInt(request.getParameter("id"));
            String nombre = request.getParameter("nombre");
            String categoria = request.getParameter("categoria");
            int cantidad = Integer.parseInt(request.getParameter("cantidad"));
            Double precio = Double.parseDouble(request.getParameter("precio"));
            
            Productos producto = new Productos(id, nombre, categoria, cantidad, precio);
            productosDAO.actualizar(producto);
            
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Productos>listarProductos = productosDAO.listarProductos();
            request.setAttribute("lista",listarProductos);
            
        }else if(accion.equalsIgnoreCase("eliminar")){
            int id = Integer.parseInt(request.getParameter("id"));
            productosDAO.eliminar(id);
            
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Productos>listarProductos = productosDAO.listarProductos();
            request.setAttribute("lista",listarProductos);
            
        }else if(accion.equalsIgnoreCase("Buscar")){
              String datos = request.getParameter("txtBuscar");
              List<Productos>lista=productosDAO.Buscar(datos);
              request.setAttribute("lista",lista);
              dispatcher = request.getRequestDispatcher("index.jsp");  
              
        }
        else{
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Productos>listarProductos = productosDAO.listarProductos();
            request.setAttribute("lista",listarProductos);
            
        }     
        
        dispatcher.forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
        doGet(request,response);
    }

 
    @Override
    public String getServletInfo() {
        return "Short description";
    }

}
