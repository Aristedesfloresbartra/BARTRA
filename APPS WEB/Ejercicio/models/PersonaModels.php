<?php

class Personas_model{

    private $db;
    private $personas;

    public function __construct(){
        $this->db = Conectar::conexion();
        $this->personas = array();
    }

    public function get_personas(){

        $sql = "SELECT * FROM personas";
        $resultado = $this->db->query($sql);
        while($row = $resultado->fetch_assoc()){
            $this->personas[]=$row;
        }
        return $this->personas;

    }


    public function insertar($nombres,$direccion,$edad,$dni,$sexo){
        $resultado = $this->db->query("INSERT INTO personas(nombres,direccion,edad,dni,sexo)VALUES('$nombres','$direccion','$edad','$dni','$sexo')");
        return $resultado;
    }

    public function modificar($id,$nombres,$direccion,$edad,$dni,$sexo){
        $resultado = $this->db->query("UPDATE personas SET nombres='$nombres',direccion='$direccion',edad='$edad',dni='$dni',sexo='$sexo' WHERE id='$id'");
        return $resultado;
    }

    

    public function eliminar($id){
        $resultado = $this->db->query("DELETE FROM personas WHERE id='$id'");
        return $resultado;
    }


    public function get_persona($id){

        $sql = "SELECT * FROM personas WHERE id='$id'";
        $resultado = $this->db->query($sql);
        $row = $resultado->fetch_assoc();

        return $row;

    }



}

?>