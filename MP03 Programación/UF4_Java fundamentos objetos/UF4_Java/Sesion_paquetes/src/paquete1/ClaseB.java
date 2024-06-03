package paquete1;

public class ClaseB extends ClaseA{

    public void imprimeAtributos() {
        //System.out.println(atributo1);
        System.out.println(atributo2);
        System.out.println(atributo3);
        System.out.println(atributo4);
    }
    
    private void metodoClaseBPrivado() {
        System.out.println("Soy el metodo privado");
    }
    protected void metodoClaseBProtected() {
        System.out.println("Soy el metodo protected");
    }
    void metodoClaseBDefault() {
        System.out.println("Soy el metodo default");
    }
    
    public void metodoClaseBPublico() {
        System.out.println("Soy el metodo publico");

    }
    
    public void prueba() {
        atributo4 = "jdjdj";
        //metodoClaseA;
    }
}
