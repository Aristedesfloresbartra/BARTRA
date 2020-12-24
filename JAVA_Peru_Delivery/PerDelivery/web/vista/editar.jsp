<%-- 
    Document   : editar
    Created on : 27-nov-2020, 17:13:16
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
        
        <div class="contenedor">
            <div class="form">
                <form action="CProductos?accion=actualizar" method="POST" autocomplete="off" >
                    <h1>EDITAR</h1>
                    <p>
                    <input type="hidden" id="id" name="id" value="<c:out value="${producto.id}"/>"/>
                    </p>

                    <p>
                    <input type="text" id="nombre" name="nombre" value="<c:out value="${producto.nombre}"/>"/> 
                    </p>
                    <p>
                    <input type="text" id="categoria" name="categoria" value="<c:out value="${producto.categoria}"/>"/>
                    </p>
                    <p>
                    <input type="text" id="cantidad" name="cantidad" value="<c:out value="${producto.cantidad}"/>"/> 
                    </p>
                    <p>
                    <input type="text" id="precio" name="precio" value="<c:out value="${producto.precio}"/>"/> 
                    </p>
                    <p></p>
                    <input type="submit" id="editar" name="editar" value="EDITAR" />
                    <a class="cancelar" href="CProductos">CANCELAR</a>
                </form>
            </div>
        </div>
                    
    </body>
</html>
