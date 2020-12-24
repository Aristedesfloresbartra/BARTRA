<%-- 
    Document   : registrar
    Created on : 27-nov-2020, 17:17:24
    Author     : arist
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="css/crear.css"/>
        <title>JSP Page</title>
    </head>
    
    <body>
       
       <div class="contenedor">
            <div class="form">
               
                <form action="CProductos?accion=insertar" method="POST" autocomplete="off" >
                     <h1>REGISTRAR</h1>
                    <p>
                        <input type="text" id="nombre" name="nombre" placeholder="Nombre" required=""/> 
                    </p>
                    <p>
                        <input type="text" id="categoria" name="categoria" placeholder="Categoria" required="" /> 
                    </p>
                    <p>
                        <input type="text" id="cantidad" name="cantidad" placeholder="Cantidad" required="" /> 
                    </p>
                    <p>
                        <input type="text" id="precio" name="precio" placeholder="Precio" required="" /> 
                    </p>

                    <input type="submit" name="guardar" value="REGISTRAR" />
                    <a class="cancelar" href="CProductos">CANCELAR</a>

                </form>
            </div>
        </div>
        
    </body>
</html>
