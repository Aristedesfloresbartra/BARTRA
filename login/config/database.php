
<?php
    class Conectar{

        public static function conexion(){
            
            $conexion = new mysqli("localhost","root","","usuarios_login");
            return $conexion;
        }

    }
?>