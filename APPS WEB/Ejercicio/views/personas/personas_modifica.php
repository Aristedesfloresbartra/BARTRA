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

    <form id="actualizar" name="actualizar" method="POST" action="index.php?c=personas&a=actualizar" autocomplete="off">

        <input type="hidden" id="id" name="id" value="<?php echo $data["id"]; ?>"/>

        <input type="text" id="nombres" name="nombres" value="<?php echo $data["personas"]["nombres"] ?>" ><br/>
        <input type="text" id="direccion" name="direccion" value="<?php echo $data["personas"]["direccion"] ?>" ><br/>
        <input type="text" id="edad" name="edad"value="<?php echo $data["personas"]["edad"] ?>"><br>
        <input type="text" id="dni" name="dni"value="<?php echo $data["personas"]["dni"] ?>"><br>
        <input type="text" id="sexo" name="sexo"value="<?php echo $data["personas"]["sexo"] ?>"><br>

        <input type="submit" id="guardar" name="guardar" value="Guardar" >

    </form>


</body>
</html>