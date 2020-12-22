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
   
    <a href="index.php?c=usuarios&a=nuevo">Registar</a>


    <table border="1">
        <thead>
        <tr>
            <th>USUARIO</th>
            <th>EMAIL</th>
            <th>PASSWORD</th>
            <th colspan="2">OPCIONES</th>
        </tr>
        
        </thead>

        <tbody>
            <?php
             
            foreach($data['usuarios'] as $dato){
                echo "<tr>";
                    echo "<td>".$dato["nombre_usuario"]."</td>";
                    echo "<td>".$dato["email"]."</td>";
                    echo "<td>".$dato["contrasena"]."</td>";
                    echo "<td><a href='index.php?c=usuarios&a=modificar&id=".$dato["id"]."'>Editar</a></td>";
                    echo "<td><a href='index.php?c=usuarios&a=eliminar&id=".$dato["id"]."'>Eliminar</a></td>";
                echo "</tr>";
             
            }
            ?>
        
        </tbody>
    
    </table>
    
</body>
</html>