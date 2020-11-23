package Modelo;


public class Alumnos {
    
    private int id;
    private String nombres,apellidos,carrera,estado;
    private Double nota1,nota2,promedio;

    public Alumnos(int id, String nombres, String apellidos, String carrera, Double nota1, Double nota2, Double promedio,String estado) {
        this.id = id;
        this.nombres = nombres;
        this.apellidos = apellidos;
        this.carrera = carrera;
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.promedio = promedio;
        this.estado = estado;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombres() {
        return nombres;
    }

    public void setNombres(String nombres) {
        this.nombres = nombres;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public Double getNota1() {
        return nota1;
    }

    public void setNota1(Double nota1) {
        this.nota1 = nota1;
    }

    public Double getNota2() {
        return nota2;
    }

    public void setNota2(Double nota2) {
        this.nota2 = nota2;
    }

    public Double getPromedio() {
        return promedio;
    }

    public void setPromedio(Double promedio) {
        this.promedio = promedio;
    }

    
    
    
}
