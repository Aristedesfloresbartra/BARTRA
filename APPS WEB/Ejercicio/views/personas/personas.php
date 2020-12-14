<?php

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $data["titulo"];  ?></title>
</head>
<body>

    <h2><?php echo $data["titulo"]; ?></h2>
    <br>
    <a href="index.php?c=personas&a=nuevo">Agregar</a>

    <table border="1">

        <thead>
            <tr>
                <th>Nombres</th>
                <th>Direccion</th>
                <th>Edad</th>
                <th>Dni</th>
                <th>Sexo</th>
                <th colspan="2">Opciones</th>
            </tr>
        </thead>

        <tbody>
            <?php foreach($data["personas"] as $dato){
                echo "<tr>";
                    echo "<td>".$dato["nombres"]."</td>";
                    echo "<td>".$dato["direccion"]."</td>";
                    echo "<td>".$dato["edad"]."</td>";
                    echo "<td>".$dato["dni"]."</td>";
                    echo "<td>".$dato["sexo"]."</td>";

                    echo "<td><a href='index.php?c=personas&a=modificar&id=".$dato["id"]."'>Editar</a></td>";
                    echo "<td><a href='index.php?c=personas&a=eliminar&id=".$dato["id"]."'>Eliminar</a></td>";

                echo "</tr>";
            }               
            ?>
        
        </tbody>


    </table>
</body>
</html>