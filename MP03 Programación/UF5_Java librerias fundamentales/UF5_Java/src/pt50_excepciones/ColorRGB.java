package pt50_excepciones;

public class ColorRGB{
	private int r;
	private int g;
	private int b;
	
	//Constructor
	//Se anade throws para asegurar que pueda lanzar una excepcion a la hora de crear un color
	public ColorRGB(int r, int g, int b) throws ColorRGBException {
		
		//Control de los valores dentro del rango (0-255)
		if (r < 0 || r > 255) {
			throw new ColorRGBException("Valor de R: "+ r + " fuera de rango.");
		}
		
		if (g < 0 || g > 255) {
			throw new ColorRGBException("Valor de G: "+ g + " fuera de rango.");
		}
		
		if (b < 0 || b > 255) {
			throw new ColorRGBException("Valor de B: "+ b + " fuera de rango.");
		}
		
		this.r = r;
		this.g = g;
		this.b = b;
	}
	
	
	
	//Asignar color:
	
			//conjunto
	public void assignarColor(int r, int g, int b) throws ColorRGBException{
		
		
		if (r < 0 || r > 255) {
			throw new ColorRGBException("Valor de R: "+ r + " fuera de rango.");
		}
		
		if (g < 0 || g > 255) {
			throw new ColorRGBException("Valor de G: "+ g + " fuera de rango.");
		}
		
		if (b < 0 || b > 255) {
			throw new ColorRGBException("Valor de B: "+ b + " fuera de rango.");
		}
		
		this.r = r;
		this.g = g;
		this.b = b;
		
	}
	
	
			//individuales
	public void assignarR(int r) throws ColorRGBException{
		
		if (r < 0 || r > 255) {
			throw new ColorRGBException("Valor de R: "+ r + " fuera de rango.");
		}
		this.r = r;	
	}
	
	public void assignarG(int g) throws ColorRGBException{
		
		if (g < 0 || g > 255) {
			throw new ColorRGBException("Valor de G: "+ g + " fuera de rango.");
		}
		this.g = g;	
	}
	
	public void assignarB(int b) throws ColorRGBException{
		
		if (b < 0 || b > 255) {
			throw new ColorRGBException("Valor de B: "+ b + " fuera de rango.");
		}
		this.b = b;	
	}
	
	
	// Métodos para obtener color
	
			//conjunto
    public int[] obtenerColor() {
        return new int[] { r, g, b };
    }

    		//individuales
    public int obtenerColorR() {
        return r;
    }

    public int obtenerColorG() {
        return g;
    }

    public int obtenerColorB() {
        return b;
    }
}
class ColorRGBException extends Exception{
	
	public ColorRGBException(String message){
		super(message);
		
	}
	
	public ColorRGBException(){
		System.out.println("Mensaje de MiExcepcion indeterminado");
		
	}
	
}


