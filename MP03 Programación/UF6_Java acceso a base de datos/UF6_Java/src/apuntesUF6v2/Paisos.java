package apuntesUF6v2;

public class Paisos {
    private int id;
    private String nombre;

    public Paisos(int id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    // Setters y Getters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

   
    public String toString() {
        return "id=" + id +", nombre =" + nombre + "\n";
    }
}

