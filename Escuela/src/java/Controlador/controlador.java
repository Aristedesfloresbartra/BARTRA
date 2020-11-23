
package Controlador;

import Modelo.Alumnos;
import ModeloDAO.AlumnosDAO;
import java.awt.Color;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class controlador extends HttpServlet {


    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
       
        AlumnosDAO alumnosDAO = new AlumnosDAO();
        
        String accion;
        RequestDispatcher dispatcher=null;
        
        accion = request.getParameter("accion");
        
        if(accion == null || accion.isEmpty()){
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Alumnos>listaAlumnos = alumnosDAO.listarAlumnos();
            request.setAttribute("lista",listaAlumnos);
               
        }
        else if("nuevo".equals(accion)){
            dispatcher = request.getRequestDispatcher("vistas/registrar.jsp");  
        }
        else if("insertar".equals(accion)){
            int id = Integer.parseInt(request.getParameter("id"));
            String nombres = request.getParameter("nombres");
            String apellidos = request.getParameter("apellidos");
            String carrera = request.getParameter("carrera");
            Double calificacion1 = Double.parseDouble(request.getParameter("calificacion1"));
            Double calificacion2 = Double.parseDouble(request.getParameter("calificacion2"));          
            Double promedio = (calificacion1+calificacion2)/2;           
            String estado;           
            if(promedio<=10.49){
               estado="Reprobado";   
              
            }
            else{
                estado="Aprobado";
            }          
            Alumnos alumno = new Alumnos(id, nombres, apellidos, carrera, calificacion1 , calificacion2, promedio,estado);
            alumnosDAO.insertar(alumno);       
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Alumnos>listaAlumnos = alumnosDAO.listarAlumnos();
            request.setAttribute("lista",listaAlumnos);         
        }
        
        else if("modificar".equals(accion)){
            dispatcher = request.getRequestDispatcher("vistas/editar.jsp"); 
            int id = Integer.parseInt(request.getParameter("id"));
            Alumnos alumno = alumnosDAO.mostrarAlumnos(id);
            request.setAttribute("alumno",alumno); 
            
        }
        
        else if("actualizar".equals(accion)){
            
            int id = Integer.parseInt(request.getParameter("id"));
            String nombres = request.getParameter("nombres");
            String apellidos = request.getParameter("apellidos");
            String carrera = request.getParameter("carrera");
            Double calificacion1 = Double.parseDouble(request.getParameter("calificacion1"));
            Double calificacion2 = Double.parseDouble(request.getParameter("calificacion2"));          
            Double promedio = (calificacion1+calificacion2)/2;           
            String estado;           
            if(promedio<=10.49){
                estado="Reprobado";
            }
            else{
                estado="Aprobado";
            }          
            Alumnos alumno = new Alumnos(id, nombres, apellidos, carrera, calificacion1 , calificacion2, promedio,estado);
            alumnosDAO.actualizar(alumno);       
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Alumnos>listaAlumnos = alumnosDAO.listarAlumnos();
            request.setAttribute("lista",listaAlumnos);         
        }
        
        
        
        else if("eliminar".equals(accion)){
            
            int id = Integer.parseInt(request.getParameter("id"));        
            alumnosDAO.eliminar(id);
            
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Alumnos>listaAlumnos = alumnosDAO.listarAlumnos();
            request.setAttribute("lista",listaAlumnos);         
        }
        else{
            dispatcher = request.getRequestDispatcher("index.jsp");  
            List<Alumnos>listaAlumnos = alumnosDAO.listarAlumnos();
            request.setAttribute("lista",listaAlumnos);
            
        }
        dispatcher.forward(request, response);
    }
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
    
        
        doGet(request, response);
        
        
    }

  
    @Override
    public String getServletInfo() {
        return "Short description";
    }

}
