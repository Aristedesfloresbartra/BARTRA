<?php

// Aristedes flores bartra
//senati 3 ciclo
    class UsuariosController {

        public function __construct(){
            
            require_once "models/UsuariosModel.php";
        }

        public function index(){
     
            $usuarios = new Usuarios_model();

            $data['titulos'] = 'Usuarios';
            $data['usuarios'] = $usuarios->get_Usuarios();      

            require_once "views/usuarios/usuarios.php";
        }
        public function nuevo(){
            $data['titulos'] = 'Usuarios';
            require_once "views/usuarios/registrar.php";
        }

        public function guarda(){

            $nombre_usuario = $_POST['nombre_usuario'];
            $email = $_POST['email'];
            $contrasena = $_POST['contrasena'];
            $confirmar_contrasena = $_POST['confirmar_contrasena'];



            if($contrasena == $confirmar_contrasena){

                $contrasena_encyptada = password_hash($contrasena,PASSWORD_BCRYPT);

                $usuarios = new Usuarios_model();
                $usuarios->insertar($nombre_usuario,$email,$contrasena_encyptada);

            }
                 
            $data['titulos'] = 'Usuarios';
            $this->nuevo();
        }

        public function modificar($id){

            $usuarios = new Usuarios_model();
            $data['id'] = $id;
            $data['usuarios'] = $usuarios->get_Usuario($id);
            $data['titulos'] = 'Usuarios';

            require_once "views/usuarios/editar.php";

        }

        public function actualizar(){

            $id = $_POST['id'];
            $nombre_usuario = $_POST['nombre_usuario'];
            $email = $_POST['email'];

            $usuarios = new Usuarios_model();
            $usuarios->modificar($id, $nombre_usuario, $email);    

            $data['titulos'] = 'Usuarios';
            $this->index();
        }

        public function eliminar($id){

            $usuarios = new Usuarios_model();
            $usuarios->eliminar($id);  

            $data['titulos'] = 'Usuarios';
            $this->index();
        }



    }
       
?>