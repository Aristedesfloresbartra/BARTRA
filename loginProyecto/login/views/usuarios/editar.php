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

    <form action="index.php?c=usuarios&a=actualizar" id="nuevo" name = "nuevo" method="POST" autocomplete="off" >

        <input type="hidden" id="id" name="id" value="<?php echo $data['id']; ?>" ><br>

        <input type="text" id="nombre_usuario" name="nombre_usuario" value = "<?php echo $data['usuarios']['nombre_usuario'] ?>"><br>
        <input type="text" id="email" name="email" placeholder="Correo electronico" value = "<?php echo $data['usuarios']['email'] ?>"><br>

        <input type="submit" id="guardar" name="guardar" value="Editar" ><br>
        <a href="index.php">Inicio</a>

    </form>

    
</body>
</html>