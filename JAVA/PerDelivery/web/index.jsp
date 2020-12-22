<%-- 
    Document   : index
    Created on : 27-nov-2020, 17:08:50
    Author     : arist
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %> 

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="css/estilos.css"/>
        <title>JSP Page</title>
    </head>
    <body>
        
        <div class="main">
        <div class="contenedor">
        
            
            <div class="header">
                <div class="contheader">
                    <div class="flex">
                        <a href="CProductos?accion=nuevo">NUEVO</a>
                         <a href="CProductos">PRODUCTOS</a>
                        <form>
                            <input type="search" name="txtBuscar" placeholder="Filtar por categoria" />
                            <input type="submit" name="accion" value="Buscar" />
                        </form>
                     </div>
                </div>
            </div>
            
            
        <div class="table">
        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>NOMBRE</th>
                    <th>CATEGORIA</th>
                    <th>CANTIDAD</th>
                    <th>PRECIO</th>
                    <th>OPCIONES</th>
                </tr>
            </thead>
            <tbody>
                <c:forEach var="producto" items="${lista}">
                <tr>
                    <td><c:out value="${producto.id}"/></td>
                    <td><c:out value="${producto.nombre}"/></td>
                    <td><c:out value="${producto.categoria}"/></td>
                    <td><c:out value="${producto.cantidad}"/></td>
                    <td><c:out value=" S/ ${producto.precio}"/></td>
                    <td>
                        <a class="editar" href="CProductos?accion=modificar&id=<c:out value="${producto.id}"/>"> Editar</a>
                        <a class="eliminar" href="CProductos?accion=eliminar&id=<c:out value="${producto.id}"/>"> Eliminar</a>
                    </td> 
                </tr>
                </c:forEach>
            </tbody>
        </table>
        </div>

        </div>
        </div>
    </body>
</html>
