package pt50_excepciones;

public class Pixel {
	private int x;
	private int y;
	private ColorRGB color;
	
	
	//Se anade throws para asegurar que pueda lanzar una excepcion a la hora de crear un color
	public Pixel(int x, int y, int r, int g, int b) throws ColorRGBException {
		super();
		this.x = x;
		this.y = y;
		this.color = new ColorRGB(r,g,b); // Se crea el ColorRGB
	}
	
	//asignar posicion
	public void asignarPosicion(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public void asignarPosicionX(int x) {
		this.x = x;
		
	}
	
	public void asignarPosicionY(int y) {
		this.y = y;
		
	}
	
	
	//obtener posicion
	
	public int[] obtenerPosicion() {
		
		return new int[] {x,y};
	}
	
	public int obtenerPosicionX() {
			
		return x;
	}
	
	public int obtenerPosicionY() {
		
		return y;
}
	
	//Metodos relacionados con ColorRGB
	
	public void assignarColor(int r, int g, int b) throws ColorRGBException {
		this.color.assignarColor(r, g, b);
	}
	
	public void assignarColorR(int r) throws ColorRGBException{
		this.color.assignarR(r);
	}
	
	public void assignarColorG(int g) throws ColorRGBException{
		this.color.assignarG(g);
	}
	
	public void assignarColorB(int b) throws ColorRGBException{
		this.color.assignarB(b);
	}
	
	public int[] obtenerColor(){
		return this.color.obtenerColor();
	}
	
	public int obtenerColorR(){
		return this.color.obtenerColorR();
	}
	
	public int obtenerColorG(){
		return this.color.obtenerColorG();
	}
	
	public int obtenerColorB(){
		return this.color.obtenerColorB();
	}

}
