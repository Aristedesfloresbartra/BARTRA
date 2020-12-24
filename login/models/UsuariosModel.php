
<?php

    class Usuarios_model{

        private $db;
        private $usuarios;

        public function __construct(){
            
            $this->db = Conectar::conexion();
            $this->usuarios = array();
        }

        public function get_Usuarios(){

            $sql = "SELECT * FROM usuarios";
            $resultado = $this->db->query($sql);

            while($row = $resultado->fetch_assoc()){

                $this->usuarios[] = $row;
            }
            return $this->usuarios;
        }

        public function insertar($nombre_usuario,$email,$contrasena){
            $resultado = $this->db->query("INSERT INTO usuarios (nombre_usuario,email,contrasena) VALUES ('$nombre_usuario','$email','$contrasena')");

        }

        public function modificar($id,$nombre_usuario,$email){
            $resultado = $this->db->query("UPDATE usuarios SET nombre_usuario='$nombre_usuario',email='$email' WHERE id='$id'");

        }

        public function eliminar($id){
            $resultado = $this->db->query("DELETE FROM usuarios WHERE id='$id'");

        }

        public function get_Usuario($id){

            $sql = "SELECT * FROM usuarios WHERE id='$id'";
            $resultado = $this->db->query($sql);

            $row = $resultado->fetch_assoc();
            return $row;

    }

}
?>