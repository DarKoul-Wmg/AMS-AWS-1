package pt41_Implementacio_Classes;

public class Ex5_figures {

	public static void main(String[] args) {
		

	}

}

abstract class Figura{
	abstract float calcularArea();

}

abstract class Figures2D extends Figura{
	abstract float calcularPerimetro();

}

abstract class Figures3D extends Figura{
	abstract float calcularVolumen();
	
}

	class Cub extends Figures3D{
		private float costat;
		
		public Cub(float costat) {
			super();
			this.costat = costat;
		}

		public Cub() {
			super();
		}
		
		
		public float calcularArea(){
			return 6 * costat * costat;		
		}
		
		public float calcularVolumen(){
			return costat * costat * costat;
		}

		public float getCostat() {
			return costat;
		}

		public void setCostat(float costat) {
			this.costat = costat;
		}
		
		
	}

	class Cilindre extends Figures3D{
		private float radi;
		private float altura;
		
		
		
		public Cilindre() {
			super();
		}

		public Cilindre(float radi, float altura) {
			super();
			this.radi = radi;
			this.altura = altura;
		}

		public float calcularArea(){
			 return (float) (2 * Math.PI * radi * radi + 2 * Math.PI * radi * altura);	
		}
		
		public float calcularVolumen(){
			 return (float) (Math.PI * radi * radi * altura);
		}

		public float getRadi() {
			return radi;
		}

		public void setRadi(float radi) {
			this.radi = radi;
		}

		public float getAltura() {
			return altura;
		}

		public void setAltura(float altura) {
			this.altura = altura;
		}
		
		
	}
	
	class Rectangle extends Figures2D{
		private float ample;
		private float altura;
		
		
		public Rectangle() {
			super();
		}

		public Rectangle(float ample, float altura) {
			super();
			this.ample = ample;
			this.altura = altura;
		}

		public float getAmple() {
			return ample;
		}

		public void setAmple(float ample) {
			this.ample = ample;
		}

		public float getAltura() {
			return altura;
		}

		public void setAltura(float altura) {
			this.altura = altura;
		}

		public float calcularArea(){
			 return ample * altura;	
		}
		
		public float calcularPerimetro(){
			 return 2 * (ample + altura);
		}
	}
	
	class Cercle extends Figures2D{
		private float radi;
		
		
		public Cercle() {
			super();
		}

		public Cercle(float radi) {
			super();
			this.radi = radi;
		}
		

		public float getRadi() {
			return radi;
		}

		public void setRadi(float radi) {
			this.radi = radi;
		}

		public float calcularArea(){
			 return (float) (Math.PI * radi * radi);	
		}
		
		public float calcularPerimetro(){
			 return (float) (2 * Math.PI * radi);
		}
	}