package pt50_excepciones;

public class Main50 {

	
	public static void main(String[] args) {
		
		//------------------------
		//------------------------
		 	try {
	            // colores fuera de rango    x y r g b
	            Pixel pixel1 = new Pixel(0, 300, 300, 300, -50);
	            System.out.println("Pixel 1 creado correctamente.");
	            
	        } catch (ColorRGBException e) {
	            System.out.println("Error al crear el pixel 1: " + e.getMessage());
	        }

	        try {
	            // color R fuera de rango
	            Pixel pixel2 = new Pixel(20, 30, 260, 100, 50);
	            System.out.println("Pixel 2 creado correctamente.");
	        } catch (ColorRGBException e) {
	            System.out.println("Error al crear el pixel 2: " + e.getMessage());
	        }

	        try {
	            // color G fuera de rango
	            Pixel pixel3 = new Pixel(30, 40, 100, 260, 70);
	            System.out.println("Pixel 3 creado correctamente.");
	        } catch (ColorRGBException e) {
	            System.out.println("Error al crear el pixel 3: " + e.getMessage());
	        }

	        try {
	            // color B fuera de rango
	            Pixel pixel4 = new Pixel(40, 50, 80, 120, -10);
	            System.out.println("Pixel 4 creado correctamente.");
	        } catch (ColorRGBException e) {
	            System.out.println("Error al crear el pixel 4: " + e.getMessage());
	        }

	        	// colores dentro de rango
	        try {
	            Pixel pixel5 = new Pixel(50, 60, 100, 200, 50);
	            System.out.println("Pixel 5 creado correctamente.");
	        } catch (ColorRGBException e) {
	            System.out.println("Error al crear el pixel 5: " + e.getMessage());
	        }
	}

}



