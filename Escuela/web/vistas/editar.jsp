<%-- 
    Document   : editar
    Created on : 20-nov-2020, 14:10:28
    Author     : arist
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %> 
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="css/editar.css"/>
        <title>JSP Page</title>
    </head>
    <body>
        
        <div class="body_cont">
            <div class="contenedor">

                <div class="form1">

                    <div class="form">

                        <form action="controlador?accion=actualizar" method="POST" autocomplete="off">

                            <div class="separe">
                            <input type="hidden" id="id" name="id" value="<c:out value="${alumno.id}"/>"/><br>

                            <p>NOMBRES </p>
                             <input type="text" id="nombres" name="nombres" value="<c:out value="${alumno.nombres}"/>"/><br>
                             
                            <p>APELLIDOS</p>
                             <input type="text" id="apellidos" name="apellidos" value="<c:out value="${alumno.apellidos}"/>" /><br>
                            
                            <p>CARRERA </p>
                             <input type="text" id="carrera" name="carrera" value="<c:out value="${alumno.carrera}"/>"/><br>
                            
                             <p>CALIFICACION I</p>
                            <input type="text" id="calificacion1" name="calificacion1" value="<c:out value="${alumno.nota1}"/>" /><br>
                            
                            <p>CALIFICACION II</p>
                            <input type="text" id="calificacion2" name="calificacion2" value="<c:out value="${alumno.nota2}"/>"/><br>
                            

                            <input type="submit" id="Editar" name="Registrar" value="Actualizar" />
                            </div>
                        </form>
                            
                    </div>
                  </div>
                            <div class="volver_i">
                                <a href="controlador">Volver al inicio</a>
                            </div>
            </div>          
        </div>         
    </body>
</html>
