<?php
    require_once "config/config.php";
    require_once "nucleo/rutas.php";
    require_once "config/database.php";
    require_once "controllers/Usuarios.php";

    //$control = new UsuariosController();
    //$control->index();

    if(isset($_GET['c'])){

        $controlador = cargarControlador($_GET['c']);


        if(isset($_GET['a'])){

            if(isset($_GET['id'])){

                cargarAccion($controlador,$_GET['a'],$_GET['id']);
            }else{
                cargarAccion($controlador,$_GET['a']);
            }
        
        }else{

            cargarAccion($controlador,ACCION_PRINCIPAL);
        }
       
    }else{
        
        $controlador = cargarControlador(CONTROLADOR_PRINCIPAL);
        $accionP = ACCION_PRINCIPAL;
        $controlador->$accionP();

    }
    
?>