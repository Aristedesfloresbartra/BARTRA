<?php

    class PersonasController{

        public function __construct(){
            require_once "models/PersonaModels.php";
        }

        public function index(){

            
            $personas = new Personas_model();
            $data["titulo"] = "personas";
            $data["personas"] = $personas->get_personas();

            require_once "views/personas/personas.php";
        }

        public function nuevo(){

            $data["titulo"] = "Nuevo";
            require_once "views/personas/personas_nuevo.php";


        }

        public function guarda(){

            $nombres = $_POST['nombres'];
            $direccion = $_POST['direccion'];
            $edad = $_POST['edad'];
            $dni = $_POST['dni'];
            $sexo = $_POST['sexo'];

            $personas = new Personas_model();
            $personas->insertar($nombres,$direccion,$edad,$dni,$sexo);

            $data["titulo"] = "REGISTRAR";
            $this->index();
            

        }

        public function modificar($id){

            $personas = new Personas_model();
          
            $data["id"] = $id;
            $data["personas"] = $personas->get_persona($id);
            $data["titulo"] = "Personas";
            require_once "views/personas/personas_modifica.php";

        }

        public function actualizar(){

            $id = $_POST['id'];
            $nombres = $_POST['nombres'];
            $direccion = $_POST['direccion'];
            $edad = $_POST['edad'];
            $dni = $_POST['dni'];
            $sexo = $_POST['sexo'];

            $personas = new Personas_model();
            $personas->modificar($id,$nombres,$direccion,$edad,$dni,$sexo);

            $data["titulo"] = "REGISTRAR";
            $this->index();
            

        }

        
        public function eliminar($id){

            $personas = new Personas_model();
            $personas->eliminar($id);

            $this->index();
            

        }



    }

?>