package paquete2;

public class ClaseC {
    private String atributo1;
    protected String atributo2;
    String atributo3;
    public String atributo4;

    private void metodoClaseAPrivado() {
        System.out.println("Soy el metodo privado");
    }
    protected void metodoClaseAProtected() {
        System.out.println("Soy el metodo protected");
    }
    void metodoClaseADefault() {
        System.out.println("Soy el metodo default");
    }
    
    public void metodoClaseAPublico() {
        System.out.println("Soy el metodo publico");
    }

}