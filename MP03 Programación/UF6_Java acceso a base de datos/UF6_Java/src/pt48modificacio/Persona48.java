package pt48modificacio;

import java.util.Date;

public class Persona48 {
	private String dni;
    private String nombre;
    private Date fechaNacimiento;
    private String direccion;
    private int telefono;

    // Constructor
    public Persona48(String dni, String nombre, Date fechaNacimiento, String direccion, int telefono) {
        this.dni = dni;
        this.nombre = nombre;
        this.fechaNacimiento = fechaNacimiento;
        this.direccion = direccion;
        this.telefono = telefono;
    }

    // Getters y setters

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Date getFechaNacimiento() {
        return fechaNacimiento;
    }

    public void setFechaNacimiento(Date fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }


	public String toString() {
		return "Dni = " + dni + "\nnombre =" + nombre + "\nfechaNacimiento=" + fechaNacimiento + "\ndireccion="
				+ direccion + "\nTelefono=" + telefono + "\n";
	}
    
    

}
