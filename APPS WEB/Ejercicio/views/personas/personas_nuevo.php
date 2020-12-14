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

    <form action="index.php?c=personas&a=guarda" id="nuevo" name="nuevo" method="POST" autocomplete="off" >
    
        <input type="text" id="nombres" name="nombres" placeholder="Nombres"><br>
        <input type="text" id="direccion" name="direccion" placeholder="Direccion"><br>
        <input type="text" id="edad" name="edad" placeholder="Edad"><br>
        <input type="text" id="dni" name="dni" placeholder="Dni"><br>
        <input type="text" id="sexo" name="sexo" placeholder="Sexo"><br>

        <input type="submit" id="guardar" name="guardar" value="guardar" >

    </form>


</body>
</html>