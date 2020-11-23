<%-- 
    Document   : index
    Created on : 20-nov-2020, 14:11:07
    Author     : arist
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %> 

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="css/estilos.css"/>
        <title>Alumnos</title>
    </head>
    <body>
        
        
            
        <div class="body">
        <div class="todo_enlace">
            <div class="enlaces">
                <a class="registrar" href="controlador?accion=nuevo">REGISTRAR ALUMNOS</a>
                <a class="ver_alumnos" href="controlador">VER ALUMNOS REGISTRADOS</a>
                <br>
            </div>
        </div>
         
            
        
        <div class="table">
        <table border="1">
            <thead>
                <tr>
                    <th class="ids">ID</th>
                    <th>NOMBRES</th>
                    <th>APELLIDOS</th>
                    <th>CARRERA</th>
                    <th>CALIFICACION I</th>
                    <th>CALIFICACION II</th>
                    <th>PROMEDIO</th>
                    <th>ESTADO</th>
                    <th class="option">OPCIONES</th>
                </tr>
            </thead>          
            
            <tbody>
                
             
               <c:forEach var="alumnos" items="${lista}">
                <tr>
                    <td class="id"><c:out value="${alumnos.id}"/></td>
                    <td><c:out value="${alumnos.nombres}"/></td>
                    <td><c:out value="${alumnos.apellidos}"/></td>
                    <td><c:out value="${alumnos.carrera}"/></td>
                    <td><c:out value="${alumnos.nota1}"/></td>
                    <td><c:out value="${alumnos.nota2}"/></td>
                    <td><c:out value="${alumnos.promedio}"/></td>
                    <td><c:out value="${alumnos.estado}"/></td>
                    <td>
                        <a class="editar" href="controlador?accion=modificar&id=<c:out value="${alumnos.id}"/>"> Editar</a>
                        <a class="eliminar" href="controlador?accion=eliminar&id=<c:out value="${alumnos.id}"/>"> Eliminar</a>
                    </td>
                
                </tr>
                </c:forEach>
                   
            </tbody>
        </table>

        </div>
        </div>
    </body>
</html>
