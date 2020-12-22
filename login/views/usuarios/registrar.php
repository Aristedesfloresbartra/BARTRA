<?php

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $data['titulos']; ?></title>
</head>
<body>

    <form action="index.php?c=usuarios&a=guarda" id="nuevo" name = "nuevo" method="POST" autocomplete="off" >
        <input type="text" id="nombre_usuario" name="nombre_usuario" placeholder="Nombre de usuario" required ><br>
        <input type="text" id="email" name="email" placeholder="Correo electronico" required><br>
        <input type="password" id="contrasena" name="contrasena" placeholder="Contraseña" required><br>
        <input type="password" id="confirmar_contrasena" name="confirmar_contrasena" placeholder="Confirmar contraseña" required ><br>
        <input type="submit" id="guardar" name="guardar" value="Registrar" ><br>
        <a href="index.php">Volver</a>
        
    <?php
        if(isset($_POST['guardar'])){

            $contrasena = $_POST['contrasena'];
            $confirmar_contrasena = $_POST['confirmar_contrasena'];

            if($contrasena!=$confirmar_contrasena){

                echo "<p style='color:red'>Las contraseñas no coinciden</p>";

             }else{
                echo "<p style='color:green'>Registro creado con exito</p>";
             }
        }
       
    ?>
    
    </form>

    
</body>
</html>