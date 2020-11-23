

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="css/crear.css"/>
        <title>registro</title>
    </head>
    <body>
        
        <div class="body">
            <div class="contenedor">
                <div class="registro1">
                <h1>Registro</h1>
                <div>
                <div class="form">
                    <form action="controlador?accion=insertar" method="POST" autocomplete="off">

                        <input type="text" id="id" name="id" value="" placeholder="id" /><br>
                        <input type="text" id="nombres" name="nombres" value="" placeholder="Nombres" /><br>
                        <input type="text" id="apellidos" name="apellidos" value="" placeholder="Apellidos" /><br>
                        <input type="text" id="carrera" name="carrera" value="" placeholder="Carrera" /><br>
                        <input type="text" id="calificacion1" name="calificacion1" value="" placeholder="Calificacion I" /><br>
                        <input type="text" id="calificacion2" name="calificacion2" value="" placeholder="Calificacion II" /><br>
                         
                        <input type="submit" id="Registrar" name="Registrar" value="Registrar" />
                    </form>
                    <div class="volver"><a href="controlador">Volver al inicio</div>
                </div>
            </div>
        </div>
    </body>
</html>
