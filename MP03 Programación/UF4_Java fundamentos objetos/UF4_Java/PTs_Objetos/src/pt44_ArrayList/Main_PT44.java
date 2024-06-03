package pt44_ArrayList;

import java.util.Scanner;

public class Main_PT44 {
	
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\nMenú de Ejercicios PT44:");
            System.out.println("1. Productes");
            System.out.println("2. Figura");
            System.out.println("3. personas");
            System.out.println("0. Salir");
            System.out.print("Seleccione una opción: ");
            
            while (!scanner.hasNextInt()) {
                System.out.println("Error: Por favor, introduzca un número.");
                System.out.print("Seleccione una opción: ");
                scanner.next(); // Limpiar el búfer de entrada
            }
            
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    ejecutarEjercicio1();
                    break;
                case 2:
                    ejecutarEjercicio2();
                    break;
                case 3:
                    ejecutarEjercicio3();
                    break;
                case 0:
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción no válida. Inténtelo de nuevo.");
            }
        } while (opcion != 0);
    }

    public static void ejecutarEjercicio1() {
        System.out.println("Ejecutando Ejercicio 1...");
        FrmProducte frmProducte = new FrmProducte();
		frmProducte.menu();
    }

    public static void ejecutarEjercicio2() {
        System.out.println("Ejecutando Ejercicio 2...");
        FrmFigures gestorFiguras = new FrmFigures();

        // Crear algunas figuras y agregarlas al gestor
        Cercle c1 = new Cercle("rojo", 2);
        Cercle c2 = new Cercle("azul", 2);
        Cercle c3 = new Cercle("verde", 4);
        Quadrat q1 = new Quadrat("verde", 4);
        Triangle t1 = new Triangle("azul", 3, 4);
        Quadrat q2 = new Quadrat("verde", 4);
        Triangle t2 = new Triangle("azul", 3, 4);
        Quadrat q3 = new Quadrat("verde", 4);
        Triangle t3 = new Triangle("azul", 3, 4);
        Cercle c4 = new Cercle("amarillo", 4);
        //Cercle c5 = new Cercle("rojo", 2);

        gestorFiguras.afegirFigura(c1);
        gestorFiguras.afegirFigura(c2);
        gestorFiguras.afegirFigura(c3);
        gestorFiguras.afegirFigura(q1);
        gestorFiguras.afegirFigura(t1);
        gestorFiguras.afegirFigura(q2);
        gestorFiguras.afegirFigura(t2);
        gestorFiguras.afegirFigura(q3);
        gestorFiguras.afegirFigura(t3);
        gestorFiguras.afegirFigura(c4);
        //gestorFiguras.afegirFigura(c5);

        // Imprimir el número de figuras de cada tipo y la suma de las áreas de los círculos
        System.out.println("Número de Círculos: " + gestorFiguras.getNumCercles());
        System.out.println("Número de Triángulos: " + gestorFiguras.getNumTriangles());
        System.out.println("Número de Cuadrados: " + gestorFiguras.getNumQuadrats());
        System.out.println("Suma de áreas de círculos: " + gestorFiguras.sumarAreasCirculos());
        
    }

    public static void ejecutarEjercicio3() {
        System.out.println("Ejecutando Ejercicio 3...");
        FrmPersona formulario = new FrmPersona();
        formulario.menuPersona();
        
    }
}

